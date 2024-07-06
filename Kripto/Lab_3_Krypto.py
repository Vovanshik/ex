import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def Otkrit_Key(p, q, n):
    kvadrat_vichet = [(i * i) % n for i in range(1, n)]
    kvadrat_vichet = sorted(set(kvadrat_vichet))
    repeat_V = [i for i, x_x in enumerate(kvadrat_vichet) if x_x % p == 0 or x_x % q == 0]
    for i in sorted(repeat_V, reverse=True):
        kvadrat_vichet.pop(i)
    Otkr_Key = random.choice(repeat_V)
    print(f"Открытый ключ: {Otkr_Key}")
    return Otkr_Key


def inv_count(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = inv_count(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = inv_count(a, m)
    if g != 1:
        return -1
    else:
        return x % m


def find_Secret(N, reversed):
    for S in range(N):
        if (S * S) % N == reversed:
            return S
    return -1

def Secret_Key(Otkr_Key, n):
    rev_el = modinv(Otkr_Key, n)
    Secret = find_Secret(n, rev_el)
    print(f"Закрытый ключ: {Secret}")
    return Secret

def generate_error(x, N, error_rate=0.5):
    if random.random() < error_rate:
        x = random.randint(0, N-1)
    return x

def main():
    primes = generate_primes(100)  # Генерация простых чисел до 100
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    print(f"Случайны простые числа: p = {p}, q = {q}")

    n = p * q
    Otkr_Key = Otkrit_Key(p, q, n)
    Close_Key = Secret_Key(Otkr_Key, n)

    #Видео 5:53

    r = random.randint(0, n - 1)
    x = (r * r) % n
    x = generate_error(x, n)

    b = random.randint(0, 1)

    result = False
    if b == 0: #Работает пользователь А
        x1 = (r * r) % n #А отправляет B число r
        if x1 == x:
            result = True
    else: # Работает пользователь А
        y = (r * Close_Key) % n #А отправляет B число y
        x1 = (y * y * Otkr_Key) % n # Работает пользователь B
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
        print("Мало тестов. Введите больше.")
    else:
        acredit = int(acredit)
        break
for i in range(rounds):
    print(f"\nЦикл {i + 1}:")
    for accreditation in range(acredit):
        print(f"\nАккредитация {accreditation + 1}:")
        if main():
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
#print(f"Аккредитация пройдена" if success_rate >= expected_rate else f"Аккредитация не пройдена")
