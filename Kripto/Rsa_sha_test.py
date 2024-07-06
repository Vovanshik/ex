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

import sys
import random
import time
import hashlib
import sympy

def prime_by_range(start,stop):
    primes = list(sympy.primerange(start, stop))
    return primes

def isMillerRabinPassed(mrc,number_test):
    maxDivisionByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionByTwo += 1
    assert(2**maxDivisionByTwo * ec == mrc -1)

    def trialComposite(round_tester):
        if pow(round_tester,ec,mrc) == 1:
            return False
        for i in range(maxDivisionByTwo):
            if pow(round_tester,2**i * ec,mrc) == mrc-1:
                return False
        return True

    numberOfRabinTrials = number_test
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def generate_random_number(n):
    iter = 0
    while True:
        num = random.getrandbits(n-1) | (1 << (n-1)) | 1
        iter+=1
        if all(num % prime != 0 for prime in sympy.primerange(3, 2000)):
            if isMillerRabinPassed(num,5):
                return num
            continue




def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Чтение файла блоками для эффективности
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def podmena(Mass_Numbers, Open_Key, Module, error_rate=0.6):
    if random.random() < error_rate:
        Text_Bob_Fake = "Я забыл логин и пароль от аккаунта. Можешь снова их выслать?"
        Mass_Numbers = []
        for i in Text_Bob_Fake:
            Mass_Numbers.append((Alphabet.index(i) ** Open_Key) % Module)
    return Mass_Numbers


def loading_animation_Bob():
    # animation = "|/-\\"
    animation = ['.', '..', '...', '....']
    for _ in range(5):
        for char in animation:
            sys.stdout.write('\r' + 'Отправка ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + 'Успешно! ')


def loading_animation():
    # animation = "|/-\\"
    animation = ['.', '..', '...', '....']
    for _ in range(5):
        for char in animation:
            sys.stdout.write('\r' + 'Расшифровка ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + 'Успешно! ')


# def NOD(a, b):
#     c = 1
#     while a != b:
#         if (a % 2 == 0) and (b % 2 == 0):
#             c *= 2
#             a = a / 2
#             b = b / 2
#         elif (a % 2 != 0) and (b % 2 == 0):
#             b = b / 2
#
#         elif (a % 2 == 0) and (b % 2 != 0):
#             a = a / 2
#
#         elif (a % 2 != 0) and (b % 2 != 0) and a > b:
#             a = a - b
#         else:
#             b -= a
#         if a == b:
#             return a * c

def NOD(a, b):
    while b:
        a, b = b, a % b
    return a

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

def find_d(M, sum, d=19433666567834128636663913775172897338308410786575036168633866408713705661097):
    length_sum = len(str(sum))
    while d < M:
        if NOD(d, M) == 1 and len(str(d)) == length_sum:
            return d
        d += 10000
    return None

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


def st_phi(second_number, p):
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
    #primes = generate_primes(1000)
    #p = random.choice(primes)
    #q = random.choice([x for x in primes if x != p])

    p = generate_random_number(128)
    q = generate_random_number(128)
    print(f"Случайны простые числа: p = {p}, q = {q}")
    N = p * q
    print(f"Модуль равен = {N}")
    M = (p - 1) * (q - 1)
    print(f"M = {M}")
    d = 1

    sum = bin(p)[2:] + bin(q)[2:]
    sum = int(sum, 2)

    d1 = find_d(M,sum)

    if d1 == M:
        print("Неудачно сгенерировано число. Генерируем снова...")
        return -1, -1, -1

    print(f"d = {d1} ")
    #e_obr = st_phi(d1, M)
    e_obr = pow(d1, -1, M)

    print(f"e = {e_obr}")

    return d1, e_obr, N


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

    Bob_hash = str(calculate_hash("Bob.docx"))

    print(f"Хэш функция Боба: {Bob_hash}")

    # Sum_hesha = 0
    #
    # for i in Bob_hash:
    #     Sum_hesha += int(i, 16)
    Sum_hesha = int(Bob_hash, 16)

    print(f"Значение Хэша Боба: {Sum_hesha}")

    Bob_ECP = pow(Sum_hesha, Close_Key, Module)
    print(f"Bob передает файл и подпись Алисе... {Bob_ECP}")
    print(f"Алиса получает подпись и файл... {Bob_ECP}")

    Alice_count_Bob_hash = str(calculate_hash("Alice.docx"))

    print(f"Хэш переданного документа: {Alice_count_Bob_hash}")

    # Sum_hesha_Alice = 0
    #
    # for i in Alice_count_Bob_hash:
    #     Sum_hesha_Alice += int(i, 16)

    Sum_hesha_Alice = int(Alice_count_Bob_hash, 16)

    Alice_admit_Bob = (Bob_ECP ** Open_Key) % Module
    print(f"Значение Хэша документа Боба, посланного Алисе: {Alice_admit_Bob}")

    print("Проверка Хэша...")

    if Sum_hesha_Alice == Alice_admit_Bob:
        print(f"Документ не был изменен и подпись подтверждена \n {Sum_hesha_Alice} = {Alice_admit_Bob}")



    print("\n Ситуация с подменой содержимого...Документ Eva.docx")

    print(f"Bob передает файл и подпись Алисе... {Bob_ECP}")
    print(f"Алиса получает подпись и файл Евы... {Bob_ECP}")

    Alice_count_Eva_hash = str(calculate_hash("Eva.docx"))
    print(f"Хэш переданного документа: {Alice_count_Eva_hash}\n")

    Sum_hesha_Alice_Eva = 0

    for i in Alice_count_Eva_hash:
        Sum_hesha_Alice_Eva += int(i, 16)

    Alice_admit_Bob_Eva = (Bob_ECP ** Open_Key) % Module
    print(f"Значение Хэша документа Боба, посланного Алисе: {Alice_admit_Bob_Eva }")

    print("Проверка Хэша...")

    if Sum_hesha_Alice_Eva != Alice_admit_Bob_Eva:
        print(f"Документ был изменен и подпись неподтверждена \n {Sum_hesha_Alice_Eva} = {Alice_admit_Bob_Eva }")



