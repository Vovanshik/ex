import random
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
                return num, iter
            continue


def is_primitive_root(a, n):
    phi = sympy.totient(n)
    phi = int(str(phi))
    factors = sympy.factorint(phi)
    for factor in factors:
        if pow(a, phi // factor, n) == 1:
            return False
    return True
# def find_primitive_roots(n, num_roots):
#     # Поиск первых num_roots первообразных корней по модулю n
#     primitive_roots = []
#     a = 2  # начинаем проверку с числа 2
#     while len(primitive_roots) < num_roots:
#         if is_primitive_root(a, n):
#             primitive_roots.append(a)
#         a += 1
#     return primitive_roots


def find_primitive_root(n):
    # Поиск первообразного корня по модулю n
    for a in range(2, n):
        if is_primitive_root(a, n):
            return a
    return None
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

def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def find_primitive_roots(n):
    roots = list()
    i = 2
    phi = sympy.totient(n)
    decom = canonical_decomposition(phi)
    exponents = list(set(decom))
    while len(roots) !=100:
        flag = True

        for exp in exponents:
            if (i ** (phi//exp)) % n == 1:
                flag = False

        if flag:
            roots.append(i)
        i+=1

    return roots


def diff_hell():
    n = random.getrandbits(100-1) | (1 << (100-1)) | 1
    g = find_primitive_root(n)

    first_secret = random.randint(2, n-2)
    second_secret = random.randint(2, n-2)

    first_public = mod_pow(g, first_secret, n)
    second_public = mod_pow(g, second_secret, n)

    first_shared_key = mod_pow(second_public, first_secret, n)
    second_shared_key = mod_pow(first_public, second_secret, n)

    assert first_shared_key == second_shared_key

    print("Секретный ключ, полученный Первого:", first_shared_key)
    print("Секретный ключ, полученный Второго:", second_shared_key)



print(len(bin(generate_random_number(512)[0])))
print(prime_by_range(2**512, 2**1024))
print(find_primitive_roots(7))

diff_hell()