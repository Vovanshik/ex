Alphabet = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т","У",
            "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т","у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3','4', '5',
            '6', '7', '8', '9', '10', '!', '@', '"', '№', '#', '0', '$', ';', '%', '^', ':', '?', '&', '*', '(',
            ')', '-', '_', '+', '=', '~','`', '|', '/', '{', '}', '[', ']', '.', ',', '<', '>', ' ']

import sys
import random
import time



def loading_animation_Bob():
    #animation = "|/-\\"
    animation = ['.','..','...','....']
    for _ in range(5):
        for char in animation:
            sys.stdout.write('\r' + 'Отправка ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + 'Успешно! ')

def loading_animation():
    #animation = "|/-\\"
    animation = ['.','..','...','....']
    for _ in range(5):
        for char in animation:
            sys.stdout.write('\r' + 'Расшифровка ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + 'Успешно! ')

def NOD(a, b):
    c = 1
    while a != b:
        if (a % 2 == 0) and (b % 2 == 0):
            c *= 2
            a = a / 2
            b = b / 2
        elif (a % 2 != 0) and (b % 2 == 0):
            b = b / 2

        elif (a % 2 == 0) and (b % 2 != 0):
            a = a / 2

        elif (a % 2 != 0) and (b % 2 != 0) and a > b:
            a = a - b
        else:
            b -= a
        if a == b:
            return a * c


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    return False

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def canonical_decomposition(n):
    if n < 2:
        return [n]

    factors = prime_factors(n)
    unique_factors = set(factors)
    decomposition = []

    for factor in unique_factors:
        count = factors.count(factor)
        if count > 1:
            decomposition.append(factor)
        else:
            decomposition.append(factor)

    return decomposition

def st_phi(second_number,p):
    f = 1
    if NOD(second_number, p) != 1:
        return -1

    if is_prime(p):
        f = p - 1
    else:
        f *= p
        decomposition = canonical_decomposition(int(p))
        for i in decomposition:
            f *= (1 - 1 / int(i))

    second_number **= int(f - 1)
    return second_number % p

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
    return [i for i in primes if (i != 0) and i > 100]

def general():
    primes = generate_primes(1000)
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    print(f"Случайны простые числа: p = {p}, q = {q}")
    N = p * q
    print(f"Модуль равен = {N}")
    M = (p - 1) * (q - 1)
    print(f"M = {M}")
    d = 1

    sum = bin(p)[2:] + bin(q)[2:]
    sum = int(sum, 2)

    while d < M:
        if NOD(d, M) == 1 and len(str(d)) == len(str(sum)):
            break
        d += 1

    if d == M:
        print("Неудачно сгенерировано число. Генерируем снова...")
        return -1, -1, -1

    print(f"d = {d} ")
    e_obr = st_phi(d, M)

    print(f"e = {e_obr}")

    return d, e_obr, N



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
    while True:
        Close_Key, Open_Key, Module = general()
        if Close_Key != -1 or Open_Key != Module:
            break



    Mass_Numbers = []
    print(f"Bob имеет закрытый ключ для подписи: ({Close_Key},{Module})")
    Text_Bob = input("Введите текст: ")
    print(f"Bob шифрует сообщение с помощью открытого ключа Алисы...")
    indexi = ''
    time.sleep(1)
    idnex_text = ''
    for i in Text_Bob:
        Mass_Numbers.append([Alphabet.index(i), (Alphabet.index(i)**Close_Key) % Module])
        indexi += str((Alphabet.index(i)**Close_Key) % Module)
        idnex_text += str((Alphabet.index(i)))

    print(idnex_text)

    print(f"Bob отправляет пару символ и подпись сообщения Алисе: {indexi}")
    print(Mass_Numbers)
    print("\n")
    print(f"Алиса имеет открытый ключ: ({Open_Key},{Module})")
    print("Alice начала проверку подписи ")
    print("\n")
    Mass_Alice = []
    indexi1 = ''
    perevod = ''
    for i in Mass_Numbers:
        Mass_Alice.append((i[1]**Open_Key) % Module)
        indexi1 += str((i[1]**Open_Key) % Module)
        perevod += str(Alphabet[(i[1]**Open_Key) % Module])
    print("Алиса расшифровала подпись Боба....")
    print(f"Числовой вид: {indexi1}")
    print(f"Текстовый вид: {perevod}")



else:
    with open('Bob_text.txt', 'r', encoding='utf-8') as f:
        Text_Bob = f.read()
    f.close()
    while True:
        Close_Key, Open_Key, Module = general()
        if Close_Key != -1 or Open_Key != Module:
            break
    Mass_Numbers = []
    print(f"Bob имеет открытый ключ Алисы: ({Open_Key},{Module})")
    print(f"Bob шифрует сообщение с помощью открытого ключа Алисы...")
    indexi = ''
    time.sleep(3)
    for i in Text_Bob:
        Mass_Numbers.append((Alphabet.index(i) ** Open_Key) % Module)
        indexi += str((Alphabet.index(i) ** Open_Key) % Module)
    print(f"Bob отправляет зашифрованное сообщение Алисе: {indexi}")
    loading_animation_Bob()
    print("\n")
    Mass_Numbers = podmena(Mass_Numbers, Open_Key, Module)
    print(f"Алиса имеет закрытый ключ: ({Close_Key},{Module})")
    print("Alice начала расшифровку ")
    loading_animation()
    Mass_Alice = []
    indexi1 = ''
    perevod = ''
    for i in Mass_Numbers:
        indexi1 += str((i ** Close_Key) % Module)
        perevod += str(Alphabet[(i ** Close_Key) % Module])
    print("Алиса расшифровала сообщение Боба....")
    with open('Alice_text.txt', 'w', encoding='cp1251') as f:
        f.write(perevod)
    f.close()















