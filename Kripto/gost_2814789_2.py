import binascii
from math import log2, ceil
import random
from random import randrange
import numpy


def text_to_bits(text, encoding='cp1251', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(binstring, encoding='cp1251', errors='surrogatepass'):
    n = int(binstring, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def split_text(text: str):
    text_bin = text_to_bits(text)
    text_bin_block = []
    if len(text_bin) % 64 == 0:
        for i in range(len(text_bin) // 64):
            text_bin_block.append(text_bin[i * 64:(i * 64) + 64])
    else:
        temp = len(text_bin) % 64
        for i in range(len(text_bin) // 64):
            text_bin_block.append(text_bin[i * 64:(i * 64) + 64])
        text_bin_block.append('0' * (64 - temp) + text_bin[-temp:])
    # print(text_bin_block)
    # print(len(text_bin_block[1]))
    return text_bin_block

def split_text2(text: str):
    text_bin = text
    text_bin_block = []
    if len(text_bin) % 64 == 0:
        for i in range(len(text_bin) // 64):
            text_bin_block.append(text_bin[i * 64:(i * 64) + 64])
    else:
        temp = len(text_bin) % 64
        for i in range(len(text_bin) // 64):
            text_bin_block.append(text_bin[i * 64:(i * 64) + 64])
        text_bin_block.append('0' * (64 - temp) + text_bin[-temp:])
    # print(text_bin_block)
    # print(len(text_bin_block[1]))
    return text_bin_block


def razbivka_32(text, k):
    lol = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
    New_key = lol(text, k)
    return New_key


def round(block, k_i, P):
    matrix = (
        (1, 13, 4, 6, 7, 5, 14, 4),
        (15, 11, 11, 12, 13, 8, 11, 10),
        (13, 4, 10, 7, 10, 1, 4, 9),
        (0, 1, 0, 1, 1, 13, 12, 2),
        (5, 3, 7, 5, 0, 10, 6, 13),
        (7, 15, 2, 15, 8, 3, 13, 8),
        (10, 5, 1, 13, 9, 4, 15, 0),
        (4, 9, 13, 8, 15, 2, 10, 14),
        (9, 0, 3, 4, 14, 14, 2, 6),
        (2, 10, 6, 10, 4, 15, 3, 11),
        (3, 14, 8, 9, 6, 12, 8, 1),
        (14, 7, 5, 14, 12, 7, 1, 12),
        (6, 6, 9, 0, 11, 6, 0, 7),
        (11, 8, 12, 3, 2, 0, 7, 15),
        (8, 2, 15, 11, 5, 9, 5, 5),
        (12, 12, 14, 2, 3, 11, 9, 3)

    )

    left_block = block[:32]
    right_block = block[32:]
    # k_i = '11001010110011101100110111010001'
    # left_block = '11001100110001011100101111000101'

    # right_block = '11011000110010101100111000100000'

    # new_right = right_block

    right_block = int(right_block, 2)
    k_i = int(k_i, 2)
    new_right_part = (right_block + k_i) % 2 ** 32
    new_right_part = bin(new_right_part)[2:]
    # print(new_right_part)
    if len(new_right_part) < 32:
        new_right_part = '0' * (32 - len(new_right_part)) + new_right_part
    # print(new_right_part)
    new_right_part = razbivka_32(new_right_part, 4)
    # print(new_right_part)

    for k in range(8):
        new_right_part[k] = str(bin(matrix[int(new_right_part[k], 2)][k])[2:])
        if len(new_right_part[k]) < 4:
            new_right_part[k] = '0' * (4 - len(new_right_part[k])) + new_right_part[k]
    # print(new_right_part)
    new_right_part = "".join(new_right_part)
    new_right_part = new_right_part[11:] + new_right_part[:11]
    # print(new_right_part)
    # print(left_block)
    new_right_block = int(new_right_part, 2) ^ int(left_block, 2)
    new_right_block = bin(new_right_block)[2:].zfill(len(new_right_part))

    # print(new_right_block)

    new_left_block = block[32:]

    # new_left_block = new_right
    if P != 31:
        new_block = new_left_block + new_right_block
    else:
        new_block = new_right_block + new_left_block
    # print(new_block)
    return new_block


def shifr(text):
    to_gost = split_text(text)
    Key_Spisok = []
    for i in range(256):
        Key_Spisok.append(random.randint(0, 1))

    New_Key = []
    New_text = ""
    Vivod_key = ""
    for i in (Key_Spisok):
        New_text += str(i)
        Vivod_key += str(i)
        if len(New_text) == 32:
            New_Key.append(New_text)
            New_text = ""

    print("Ключ:\n")
    print(Vivod_key)
    print("Шифрование:")

    for j in range(len(to_gost)):
        for i in range(32):
            k_i = New_Key[i % 8] if i < 24 else New_Key[7 - (i % 8)]
            to_gost[j] = round(to_gost[j], k_i, i)

    print(to_gost)
    stringToWrite = ""
    for i in range(len(to_gost)):
        stringToWrite += to_gost[i] + "\n"
    f = open('text.txt', 'w')
    f.writelines(stringToWrite)
    f.close()

    s = open('key.txt', 'w')
    s.writelines(Vivod_key)
    s.close()

    return to_gost, New_Key


def deshifr(Key_Spisok):

    testik = []
    with open('text.txt', 'r') as f:
        testik.append(f.read().replace("\n", ""))


    to_gost = split_text2(testik[0])

    New_Key = []
    New_text = ""
    for i in (Key_Spisok):
        New_text += str(i)
        if len(New_text) == 32:
            New_Key.append(New_text)
            New_text = ""

    print("Дешифрование")

    for j in range(len(to_gost)):
        for i in range(32):
            k_i = New_Key[i] if i < 8 else New_Key[7 - (i % 8)]
            to_gost[j] = round(to_gost[j], k_i, i)
    #print(to_gost)

    text = ''

    for i in to_gost:
        text+=text_from_bits(i)

    print(text)






vibor = input("Выберите действие:\n1 - Зашифровать | 2 - Дешифровать\n")

if vibor == "1" :
    text = input("Введите текст: ")
    print(shifr(text))
    text, key = shifr(text)
    deshifr(key)

else:
    #text = input("Введите текст: ")
    key = input('Введите ключ: ')
    #text = 1010001101111110100011010000010111011100010000010100110101100101
    #key = '0100100000000010101111011001110111101110001010111000111110101111000000010000101111110101011100011010000010011110011011100111101000011001111001100101111011011111001001110100010101000001010011011011101111011000100111010100101010001000000010100010000100000110'
    deshifr(key)









