
import random

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
    return [i for i in primes if i != 0]


def Otkr_K(N,p,q):
    V1 = [(i*i) % N for i in range(1, N)]
    V2 = list(set(V1))
    V3 = []
    for i in range(len(V2)):
        if V2[i] % p != 0 or V2[i] % q != 0:
            V3.append(V2[i])
    Otkr_Key = random.choice(V3)
    return Otkr_Key


def close_key_S(Otkr_Key, n):
    V_minus_one = st_phi(Otkr_Key,n)

    for i in range(n):
        if (i*i) % n == V_minus_one:
            return i
    return -1

def shum(x, N, error_rate=0.5):
    if random.random() < error_rate:
        x = random.randint(0, N-1)
    return x

def global_opeation():
    primes = generate_primes(100)
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    print(f"Случайны простые числа: p = {p}, q = {q}")
    N = p * q
    Otkr_Kluch = Otkr_K(N, p, q)
    print(f"Случайный открытый ключ = {Otkr_Kluch}")
    Zakr_Kluck = close_key_S(Otkr_Kluch, N)
    print(f"Случайный закрытый ключ = {Zakr_Kluck}")

    #Работает пользователь А ( который доказывает свою подлинность и владеет секретным ключом)
    r = random.randint(1, N - 1)
    x = (r**2) % N
    x = shum(x,N)


    # Работает B пользователь
    b = random.randint(0, 1)


    result = False
    if b == 0:  # Работает пользователь А
        x1 = (r**2) % N  # А отправляет B число r
        if x1 == x:
            result = True
    else:  # Работает пользователь А
        y = (r * Zakr_Kluck) % N  # А отправляет B число y
        x1 = (y * y * Otkr_Kluch) % N  # Работает пользователь B
        if x1 == x:
            result = True

    print(f"b={b}: Аккредитация пройдена." if result else f"b={b}: Аккредитация не пройдена.")
    return result


total_passed = 0
total_failed = 0
while True:
    rounds = input("Введите количество тестов: ")
    if rounds.isdigit() == False:
        print("Это не число. Попробуйте снова ")
    elif int(rounds) < 2:
        print("Мало тестов. Введите больше.")
    else:
        rounds = int(rounds)
        break

while True:
    acredit = input("Введите количество аккредитаций: ")
    if acredit.isdigit() == False:
        print("Это не число. Попробуйте снова")
    elif int(acredit) < 2:
        print("Мало аккредитаций. Введите больше.")
    else:
        acredit = int(acredit)
        break
for i in range(rounds):
    print(f"\nЦикл {i + 1}:")
    for accreditation in range(acredit):
        print(f"\nАккредитация {accreditation + 1}:")
        if global_opeation():
            total_passed += 1
        else:
            total_failed += 1

total_accreditations = total_passed + total_failed
success_rate = (total_passed / total_accreditations) * 100
expected_rate = (1/2) ** rounds * 100

print(f"\nВсего аккредитаций: {int(total_passed)+int(total_failed)}")
print(f"Количество пройденных аккредитаций: {total_passed}")
print(f"Количество проваленных аккредитаций: {total_failed}")
print(f"Процент успешных аккредитаций: {success_rate:.5f}%")
print(f"Вероятность, что А обманет В по формуле (1/2)^{rounds}: {expected_rate:.2f}%")

