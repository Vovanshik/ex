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
    return [i for i in primes if (i != 0) and i > 100]

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
    return [i for i in primes if (i != 0) and i > 200]

def Q_shet(Q):
    r = 0

    while Q % 2 == 0:
        print("Делим на 2")
        Q //= 2
        r += 1

    p = 0
    while Q % 3 == 0:
        print("Делим на 3")
        Q //= 3
        p += 1
    return Q, r, p

def rsa():
    while True:
        primes = generate_primesRSA(600)
        p = random.choice(primes)
        q = random.choice([x for x in primes if x < p])
        N = p * q
        M = (p - 1) * (q - 1)
        d = 1
        sum = bin(p)[2:] + bin(q)[2:]
        sum = int(sum, 2)
        while d < M:
            if NOD(d, M) == 1 and len(str(d)) == len(str(sum)):
                break
            d += 1

        if d != M:
            break

    e_obr = st_phi(d, M)
    return [d, e_obr, N]




def step_1(Number_vote):

    #Шаг 1

    Familiya = ["Иванов", "Петров", "Сидоров", "Козлов", "Михайлов", "Федоров", "Новиков", "Морозов", "Волков", "Алексеев"]
    Main_Center = rsa()
    Main_Open = [Main_Center[2], Main_Center[1]]
    Main_Close = [Main_Center[2], Main_Center[0]]
    Mass_izbiratelye = []

    #Шаг 2
    for i in range(Number_vote):
        Fam = random.choice(Familiya)

        #Голосование 2 - за, 3 - против, 1 - воздержался
        User_vote = random.choice([2, 3, 1])
        if User_vote ==2:
            test = 'За'
        elif User_vote == 3:
            test = 'Против'
        else:
            test = 'Воздержался'

        #Каждый избиратель создает ключи RSA
        Vote_Rsa = rsa()
        Close_Vote = Vote_Rsa[0]
        Open_Vote = Vote_Rsa[1]
        Pole_Vote = Vote_Rsa[2]

        #Затемнение
        while True:
            simple_value = generate_primes(200)
            user_simple_value = random.choice(simple_value)
            if user_simple_value < Main_Close[0]:
                break

        t_i = User_vote * user_simple_value

        #шифрование по RSA
        f_i = (t_i ** Main_Open[1]) % Main_Open[0]
        Mass_izbiratelye.append([i, Close_Vote, Open_Vote, Pole_Vote, Fam, f_i, test,user_simple_value])

        print(f"Фамилия = {Fam} | {i+1} | f{i+1} = {f_i}")


    #Шаг 3
    #Вычисляем значение всех е-бюллетеней
    F = 1
    for i in Mass_izbiratelye:
        F *= i[5]

    print('F = ',F)
    Q = 1


    for i in Mass_izbiratelye:
        Q *= pow(i[5], Main_Close[1], Main_Close[0])
    print(f"Q:  {Q}")
    R, za, pro = Q_shet(Q)
    print(f"R:  {R}")
    All_user_vote = Number_vote
    vozd = All_user_vote - (za + pro)

    print(f"за : {za} человек")
    print(f"против : {pro} человек")
    print(f"Воздержались: {vozd} человек")

    Vote_result = [za,pro,vozd]

    for i in Mass_izbiratelye:
        print(i)
    print("HAHA")
    return Main_Open, Mass_izbiratelye,Vote_result,F


def proverka_vote(Main_Open, Mass_izbiratelye,Vote_result,F):
    #Восстанавливаем Q
    R = 1
    for i in Mass_izbiratelye:
        R *= i[7]
    New_Q = (2**Vote_result[0])*(3**Vote_result[1]) * R
    Shifr_New_Q = pow(New_Q,Main_Open[1],Main_Open[0])
    if Shifr_New_Q == (F % Main_Open[0]):
        print("Урааа")
    else:print("***")








Open_Center_Key, Izbir, result,F = step_1(10)
proverka_vote(Open_Center_Key, Izbir, result,F)




