import random
import sympy


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
    return [i for i in primes if (i != 0) and i > 100]

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
        #primes = generate_primesRSA(2000)
        #p = random.choice(primes)
        #q = random.choice([x for x in primes if x != p])
        p = generate_random_number(30)
        while True:
            q = generate_random_number(30)
            if q < p:
                break
        N = p * q
        M = (p - 1) * (q - 1)
        d = 1
        #sum = bin(p)[2:] + bin(q)[2:]
        #sum = int(sum, 2)
        while True:
            d = generate_random_number(random.choice([30]))
            if d < M:
                break

        while d < M:
            if NOD(d, M) == 1:
                break
            d += 51

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
            simple_value = generate_random_number(20)
            user_simple_value = random.choice(simple_value)
            if user_simple_value < Main_Close[0]:
                break

        t_i = User_vote * user_simple_value

        #шифрование по RSA
        f_i = (t_i ** Main_Open[1]) % Main_Open[0]
        Mass_izbiratelye.append([i, Close_Vote, Open_Vote, Pole_Vote, Fam, f_i, test])

        print(f"Фамилия = {Fam} | {i+1} | f{i+1} = {f_i}")


    #Шаг 3
    #Вычисляем значение всех е-бюллетеней
    F = 1
    for i in Mass_izbiratelye:
        F *= i[5]

    print('F = ',F)

    Q = pow(F, Main_Close[1], Main_Close[0])
    print(f"Q:  {Q}")
    R, za, pro = Q_shet(Q)
    print(f"R:  {R}")
    All_user_vote = Number_vote
    vozd = All_user_vote - (za + pro)

    print(f"за : {za} человек")
    print(f"против : {pro} человек")
    print(f"Воздержались: {vozd} человек")

    print(Mass_izbiratelye)






step_1(3)


