Alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У",
            "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
            '5',
            '6', '7', '8', '9', '10', '!', '@', '"', '№', '#', '0', '$', ';', '%', '^', ':', '?', '&', '*', '(',
            ')', '-', '_', '+', '=', '~', '`', '|', '/', '{', '}', '[', ']', '.', ',', '<', '>', ' ']

import random
import sympy


def is_primitive_root(a, n):
    phi = sympy.totient(n)
    phi = int(str(phi))
    factors = sympy.factorint(phi)
    for factor in factors:
        if pow(a, phi // factor, n) == 1:
            return False
    return True


def find_primitive_root(n):
    for a in range(2, n):
        if is_primitive_root(a, n):
            return a
    return None


def generate_primes(N):
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1
    return [i for i in primes if (i != 0) and i > 1000]




def general(check):
    if check == 0:
        primes = generate_primes(100000)
        p = random.choice(primes)
        g = find_primitive_root(p)
        x = random.choice(range(1, p - 1))
    else:
        while True:
            primes = generate_primes(100)
            p = random.choice(primes)
            g = find_primitive_root(p)
            if g < 10:
                break
        while True:
            x = random.choice(range(1, p - 1))
            if x < 10:
                break
    y = (g ** x) % p
    print(f"Открытый ключ: ({y},{g},{p})")

    return [y, g, p, x]



print("Выберите действие: \n 1 - Ручной ввод \n 2 - Считать с файла")

while True:
    Vibor = input()
    if Vibor.isdigit() == False:
        print("Это не число. Попробуйте снова ")
    elif int(Vibor) > 2 or int(Vibor) < 1:
        print("Ошибка с выбором. Попробуйте снова.")
    else:
        Vibor = int(Vibor)
        break

if Vibor == 1:
    y, g, p, x = general(0)
    print(f"Длина p в битах = {len(bin(p)[2:])}")
    print("Шифрование: ")
    Text = input("Введите текст: ")
    Mass_Numbers = []
    indexi = ''
    Points = []
    for i in Text:
        Points.append(Alphabet.index(i))
    dict = {}
    for index, sublist in enumerate(Points):
        dict[index] = sublist

    print("\nПозиции символов: ")
    for key, value in dict.items():
        print(f'{Alphabet[value]}:{value}')

    for i in Text:
        k = random.choice(range(1, p))
        a = (g ** k) % p
        print(f"Сессионый ключ = ", k)
        Mass_Numbers.append([a, k, ((Alphabet.index(i))*(y**k)) % p])
        indexi += "("+str(a) + "," + str(((Alphabet.index(i))*(y**k)) % p) + ")"
    print(f"Шифртекст = {indexi}")
    perevod = ''
    indexi1 = ''


    print("Расшифрование: ")
    for i in Mass_Numbers:
        indexi1 += str((i[2]*(i[0]**(p-1-x))) % p) + " "
        perevod += str(Alphabet[(i[2]*(i[0]**(p-1-x))) % p])
    print(f"расшифрованное сообщение в числовом виде = {indexi1}")
    print(f"расшифрованное сообщение в текстовом виде = {perevod}")

else:
    with open('Bob_text.txt', 'r', encoding='utf-8') as f:
        Text_Bob = f.read()
    f.close()
    y, g, p, x = general(0)
    print(f"Длина p в битах = {len(bin(p)[2:])}")
    print("Шифрование: ")
    Text = Text_Bob
    Mass_Numbers = []
    indexi = ''
    Points = []
    for i in Text:
        Points.append(Alphabet.index(i))
    dict = {}
    for index, sublist in enumerate(Points):
        dict[index] = sublist
    print("\nПозиции символов: ")
    for key, value in dict.items():
        print(f'{Alphabet[value]}:{value}')

    for i in Text:
        k = random.choice(range(1, p))
        a = (g ** k) % p
        print(f"Сессионый ключ = ", k)
        Mass_Numbers.append([a, k, ((Alphabet.index(i)) * (y ** k)) % p])
        indexi += "(" + str(a) + "," + str(((Alphabet.index(i)) * (y ** k)) % p) + ")"
    print(f"Шифртекст: {indexi}")
    perevod = ''
    indexi1 = ''
    for i in Mass_Numbers:
        indexi1 += str((i[2] * (i[0] ** (p - 1 - x))) % p) + " "
        perevod += str(Alphabet[(i[2] * (i[0] ** (p - 1 - x))) % p])

    with open('Alice_text.txt', 'w', encoding='cp1251') as f:
        f.write(perevod)
    f.close()

