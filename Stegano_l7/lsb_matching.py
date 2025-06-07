from __future__ import annotations

from pathlib import Path
from typing import Tuple
import numpy as np
from PIL import Image

__all__ = ["sokr", "extract"]

_LENGTH_HEADER_BITS = 32 
_method = b"LSBM"
_method_bits = np.unpackbits(np.frombuffer(_method, dtype=np.uint8))
_rng = np.random.default_rng()


def _open_rgb_bmp(path: str | Path) -> Tuple[Image.Image, np.ndarray]:
    img = Image.open(path)
    if img.format != "BMP":
        raise ValueError(f"Это не BMP")
    if img.mode != "RGB":
        try:
            img = img.convert("RGB")
        except Exception:
            raise ValueError("Это не 24бит РГБ")
    arr = np.array(img, dtype=np.uint8)
    return img, arr


def _bits_from_bytes(data: bytes) -> np.ndarray:
    return np.unpackbits(np.frombuffer(data, dtype=np.uint8))


def _bytes_from_bits(bits: np.ndarray) -> bytes:
    if len(bits) % 8:
        raise ValueError("Размер массива не 8 бит")
    return np.packbits(bits).tobytes()


def sokr(image_path: str, payload: bytes, rate: float, out_path: str) -> None:

    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)

    size_bits = int(len(vector) * rate)

    secret_msg_len = len(payload)
    if secret_msg_len >= 2 ** 32:
        raise ValueError("Секретное сообщения слишком большое")

    zagolovok = secret_msg_len.to_bytes(4, "little")
    stream = _method + zagolovok + payload
    bits = _bits_from_bytes(stream)

    if len(bits) > size_bits:
        raise ValueError(
            f"Для встраивания нужно {len(bits)} битов, вместимость контейнера с учетом рейта {size_bits} битов"
        )

    stego_vector = vector.copy()
    zona_vstr = stego_vector[: len(bits)]
    current_lsb = zona_vstr & 1
    mismatch_mask = current_lsb != bits

    indices = np.nonzero(mismatch_mask)[0]
    if indices.size:
        plus_mask = _rng.integers(0, 2, size=indices.size, dtype=np.uint8)
        deltas = np.where(plus_mask == 1, 1, -1).astype(np.int16)
        vals = zona_vstr[indices].astype(np.int16)
        #обработка краевых условий
        deltas[(vals == 0) & (deltas == -1)] = 1
        deltas[(vals == 255) & (deltas == 1)] = -1

        zona_vstr[indices] = (vals + deltas) & 0xFF #сохраняем изменения

    #преобразовываем обратно наш контейнер в картинку
    stego_arr = stego_vector.reshape(arr.shape)
    Image.fromarray(stego_arr, "RGB").save(out_path, format="BMP")


def extract(image_path: str, rate: float = 1.0) -> bytes:

    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)
    max_bits = int(len(vector) * rate)

    min_method_bits = len(_method_bits)
    if max_bits < min_method_bits + _LENGTH_HEADER_BITS:
        raise ValueError("Слишком маленький рейт внедрения")

    method_bits = vector[:min_method_bits] & 1
    if not np.array_equal(method_bits, _method_bits):
        raise ValueError("Это не LSBM")


    header_start = min_method_bits
    header_bits = vector[header_start:header_start + _LENGTH_HEADER_BITS] & 1
    secret_msg_len = int.from_bytes(_bytes_from_bits(header_bits), "little")

    total_bits = min_method_bits + _LENGTH_HEADER_BITS + secret_msg_len * 8
    if total_bits > max_bits:
        raise ValueError("Размер необходимых битов превышает максимальный")

    secret_msg_bits = vector[header_start + _LENGTH_HEADER_BITS:total_bits] & 1
    return _bytes_from_bits(secret_msg_bits)
