from __future__ import annotations

from pathlib import Path
from typing import Tuple
import numpy as np
from PIL import Image
__all__ = [
    "sokr",
    "extract",
]

Bits_for_method = 32
_method = b"LSBR"
_method_bits = np.unpackbits(np.frombuffer(_method, dtype=np.uint8))



def _open_rgb_bmp(path: str | Path) -> Tuple[Image.Image, np.ndarray]:
    img = Image.open(path)
    if img.format != "BMP":
        raise ValueError("Это не BMP".format(img.format))
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
    if len(bits) % 8 != 0:
        raise ValueError("Error")
    return np.packbits(bits).tobytes()


def sokr(image_path: str, secretmsg: bytes, rate: float, out_path: str) -> None:
    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)
    stegocons = len(vector)
    max_size_vstavki = int(stegocons * rate)

    secretmsg_len = len(secretmsg)
    if secretmsg_len >= 2 ** 32:
        raise ValueError("Ошибка")

    header = secretmsg_len.to_bytes(4, byteorder="little") #сохраняем длину сообщения для последующего извлечения
    full = _method + header + secretmsg
    full_bits = _bits_from_bytes(full)

    if len(full_bits) > max_size_vstavki:
        raise ValueError(
            f"Не хватает места для встраивания"
            f"({max_size_vstavki} bits)"
        )

    stego_vector = vector.copy()
    stego_vector[: len(full_bits)] &= 0xFE
    stego_vector[: len(full_bits)] |= full_bits

    stego_arr = stego_vector.reshape(arr.shape)
    stego_img = Image.fromarray(stego_arr, mode="RGB")
    stego_img.save(out_path, format="BMP")


def extract(image_path: str, rate: float = 1.0) -> bytes:

    img, arr = _open_rgb_bmp(image_path)
    vector = arr.reshape(-1)
    max_bits = int(len(vector) * rate)

    raspozn_method = len(_method_bits)
    if max_bits < raspozn_method + Bits_for_method:
        raise ValueError("Слишком маленький рейт внедрения.")

    magic_bits = vector[:raspozn_method] & 1
    if not np.array_equal(magic_bits, _method_bits):
        raise ValueError("Это не LSBR")

    header_start = raspozn_method
    header_bits = vector[header_start:header_start + Bits_for_method] & 1
    secret_msg_len = int.from_bytes(_bytes_from_bits(header_bits), byteorder="little")

    total_bits_needed = raspozn_method + Bits_for_method + secret_msg_len * 8
    if total_bits_needed > max_bits:
        raise ValueError("Ошибка. Общее кол-во необходимых битов превосходит максимальное значение")

    secretmsg_bits = vector[header_start + Bits_for_method:total_bits_needed] & 1
    return _bytes_from_bits(secretmsg_bits)