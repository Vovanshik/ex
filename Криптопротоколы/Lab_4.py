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
    return [i for i in primes if (i != 0) and i > 5]

def generate_primesRSA(N):
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
    return [i for i in primes if (i != 0) and i > 10]


def rsa():
    primes = generate_primesRSA(200)
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
        return -1,-1,-1

    print(f"d = {d} ")
    e_obr = st_phi(d, M)

    print(f"e = {e_obr}")

    return [d, e_obr, N]


Kol_vo = int(input("введите кол-во избирателей: "))

Main_center = rsa()

print(f"Главный центр говорит: Это открытый ключ и я его сообщаю: {Main_center[0]} , {Main_center[2]}")

Mass_bi = []
Eto_toshe_dlya_zateneniya = generate_primes(30)
Fam = ['Васькин','Геральт','Лазанья','Дилко','Вилко','Шпилко']
for i in range(Kol_vo):
    while True:
        Eto_kluchi_izbirateley = rsa()
        if -1 not in Eto_kluchi_izbirateley:
            break
    Eto_dlya_zateneniya = random.randint(1, 3)
    Da_skolko_moshno_zateneniy = random.choice(Eto_toshe_dlya_zateneniya)

    Eto_zateneniye = Eto_dlya_zateneniya * Da_skolko_moshno_zateneniy
    A_eto_dlya_shifr_zateneniya = pow(Eto_zateneniye, Eto_kluchi_izbirateley[0], Eto_kluchi_izbirateley[2])
    Eto_FIO = random.choice(Fam)
    Mass_bi.append([i+1, Eto_FIO, Eto_dlya_zateneniya, Eto_zateneniye, Da_skolko_moshno_zateneniy, Eto_kluchi_izbirateley[0], Eto_kluchi_izbirateley[1],
                    Eto_kluchi_izbirateley[2], A_eto_dlya_shifr_zateneniya])


print(Mass_bi)

Qushka = 1

for i in Mass_bi:
    Qushka *= i[3]

Qushka2 = Qushka
Qushka3 = Qushka
sch2 = 0
while Qushka2 % 2 == 0:
    sch2 += 1
    Qushka2 = Qushka2 / 2

sch3 = 0
while Qushka3 % 3 == 0:
    sch3 += 1
    Qushka3 = Qushka3 / 3

R = 1
for i in Mass_bi:
    R *= i[4]

Novaya_Q = (2**sch2) * (3**sch3) * R

u = N - (sch2 + sch3)

sch_1 = 0
for i in Mass_bi:
    if i[2] == 1:sch_1+=1

print(f"Воздержались = {sch_1}")

print(Novaya_Q)
print(u)


