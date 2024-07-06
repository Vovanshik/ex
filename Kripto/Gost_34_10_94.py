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
import hashlib


def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


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


def isMillerRabinPassed(mrc, number_test):
    maxDivisionByTwo = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionByTwo += 1
    assert (2 ** maxDivisionByTwo * ec == mrc - 1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionByTwo):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True

    numberOfRabinTrials = number_test
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


def generate_prime(n):
    while True:
        num = random.getrandbits(n - 1) | (1 << (n - 1)) | 1
        if all(num % prime != 0 for prime in sympy.primerange(3, 2000)):
            if isMillerRabinPassed(num, 5):
                return num
            continue


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
    while True:
        p = random.choice(primes[3:])
        q = random.choice([x for x in primes if x < p])
        if (p - 1) % q == 0:
            break
    while True:
        a = random.randint(2, p - 2)
        if pow(a, q, p) == 1:
            break

    x = random.randint(1, q - 1)
    y = pow(a, x, p)


    return p, q, a, x, y


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
    p, q, a, Close_Key, Open_Key = general()
    while True:
        k = random.randint(1, q - 1)
        r = pow(a, k, p) % q
        print(f"Алиса генерирует случайно число k: {k}")
        print(f"Алиса высчитывает число r`: {r}")
        if r != 0:
            break

    print(f'p={p}\nq ={q}\na={a}')

    hesh_message = str(calculate_hash("Alice.docx"))
    print(f"Хэш документа Алисы: {hesh_message}")
    Sum_hesha = 0

    for i in hesh_message:
        Sum_hesha += int(i, 16)
    if Sum_hesha % q == 0:
        Sum_hesha = 1

    print(Sum_hesha)

    s = (Close_Key * r + k * Sum_hesha) % q

    Send_mess = [r, s]
    print(f"Пользователь Aлиса отправляет Бобу цифровую подпись r и s: \nr = {r} \ns = {s}")


    hesh_Alice = str(calculate_hash("Bob.docx"))
    print(f"Хэш переданного документа: {hesh_Alice}")
    Sum_hesha_Alice = 0
    for i in hesh_Alice:
        Sum_hesha_Alice += int(i, 16)
    if Sum_hesha_Alice % q == 0:
        Sum_hesha_Alice = 1

    v = pow(Sum_hesha_Alice, q - 2, q)
    z1 = (Send_mess[1] * v) % q
    z2 = ((q - Send_mess[0]) * v) % q

    u = (((a ** z1) * (Open_Key ** z2)) % p) % q

    print(f"Пользователь Боб начал проверку подписи:"
          f"\nv = {v} \nz1={z1}\nz2={z2}\nu={u}")

    if u == Send_mess[0]:
        print(f"Боб проверил подпись и она подлинна\nu = r` ({u} = {r})")
    else:
        print(f"Документ был изменен и подпись неподтверждена u != r` ({u} != {r})")
