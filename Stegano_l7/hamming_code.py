from __future__ import annotations

from math import ceil
from pathlib import Path
from typing import Tuple

import numpy as np
from PIL import Image

__all__ = ["sokr", "extract"]

_HEADER_BITS = 32 
_method = b"HAMM"
_method_bits = np.unpackbits(np.frombuffer(_method, dtype=np.uint8))

H = np.array([[((j + 1) >> r) & 1 for j in range(15)] for r in range(4)], dtype=np.uint8)  # shape (4,15)


def _open_rgb_bmp(path: str | Path) -> Tuple[Image.Image, np.ndarray]:
    img = Image.open(path)
    if img.format != "BMP":
        raise ValueError(f"Это не BMP")
    if img.mode != "RGB":
        try:
            img = img.convert("RGB")
        except Exception:
            raise ValueError("Это не РГБ")
    arr = np.array(img, dtype=np.uint8)
    return img, arr


def _bits_from_bytes(data: bytes) -> np.ndarray:
    return np.unpackbits(np.frombuffer(data, dtype=np.uint8))


def _bytes_from_bits(bits: np.ndarray) -> bytes:
    if len(bits) % 8 != 0:
        raise ValueError("ERROR")
    return np.packbits(bits).tobytes()


def sokr(image_path: str, payload: bytes, rate: float, out_path: str) -> None:

    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)

    if rate !=0.27:
        raise ValueError(f"Недопустимое значение")

    total_blocks = len(vector) // 15
    polezn_blocks = int(total_blocks * rate)
    vmestim_bits = polezn_blocks * 4
    stream = _method + len(payload).to_bytes(4, "little") + payload
    bits = _bits_from_bytes(stream)
    neobx_bits = len(bits)

    if neobx_bits > vmestim_bits:
        raise ValueError(f"Размер скрываемого сообщения больше возможной вместимости {neobx_bits} > {vmestim_bits}")

    if neobx_bits % 4:
        pad = 4 - (neobx_bits % 4)
        bits = np.concatenate([bits, np.zeros(pad, dtype=np.uint8)])
    nibbles = bits.reshape(-1, 4)

    stego_vector = vector.copy()
    for block_idx, m in enumerate(nibbles):
        if block_idx >= polezn_blocks:
            break 
        start = block_idx * 15
        cover_bits = stego_vector[start:start + 15] & 1
        syndrome = (H @ cover_bits) & 1
        diff = syndrome ^ m
        diff_val = diff[0] | (diff[1] << 1) | (diff[2] << 2) | (diff[3] << 3)
        #Если блок неправильный то меняем его значение чтобы изменился синдром
        if diff_val != 0:
            pos = diff_val - 1 
            stego_vector[int(start) + int(pos)] ^= 1

    stego_arr = stego_vector.reshape(arr.shape)
    Image.fromarray(stego_arr, "RGB").save(out_path, format="BMP")


def extract(image_path: str, rate: float = 1.0) -> bytes:
    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)
    total_blocks = len(vector) // 15
    polezn_blocks = int(total_blocks * rate)

    bits_out = []
    for block_idx in range(polezn_blocks):
        start = block_idx * 15
        cover_bits = vector[start:start + 15] & 1 #берем 15 младших бит из блока
        syndrome = (H @ cover_bits) & 1
        bits_out.extend(syndrome.tolist()) #заносим биты в список

    bits = np.array(bits_out, dtype=np.uint8)

    method_len = len(_method_bits)
    if len(bits) < method_len + _HEADER_BITS:
        raise ValueError("Слишком маленький рейт внедрения или малый размер изображения")

    method_bits = bits[:method_len]
    if not np.array_equal(method_bits, _method_bits):
        raise ValueError("Это не хэмминг")

    length_bits = bits[method_len:method_len + _HEADER_BITS]
    secret_msg_len = int.from_bytes(_bytes_from_bits(length_bits), "little")

    total_bits_needed = method_len + _HEADER_BITS + secret_msg_len * 8
    if total_bits_needed > len(bits):
        raise ValueError("ERROR")

    secret_msg_bits = bits[method_len + _HEADER_BITS:total_bits_needed]
    return _bytes_from_bits(secret_msg_bits)
