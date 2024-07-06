import re
from math import gcd

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



def Eiler(divident_A, exponent_A,divider_M,NOD_AM,New_Divider_A):
    new_exponent = 0
    trash = 1
    while exponent_A >= 1:
        if exponent_A == 1:
            if NOD_AM > 1:
                print(f"{divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M} ")
            divident_A = (divident_A * trash * New_Divider_A) % (divider_M)
            break


        elif divident_A < divider_M and exponent_A % 2 == 0 and exponent_A != 0:
            print(f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A}^2 ≡ {divident_A ** 2 % divider_M} mod {divider_M}]")
            exponent_A = exponent_A // 2
            divident_A **= 2
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")

        elif (divident_A ** exponent_A) * trash <= 100:
            if New_Divider_A > 1:
                print(f"До: {divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M}")
            else:
                print(f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M}")

            divident_A **= exponent_A

            divident_A *= trash
            if New_Divider_A != 1:
                divident_A = divident_A * New_Divider_A
            divident_A = divident_A % divider_M
            print(f"После: {divident_A} mod {divider_M}")
            exponent_A -= exponent_A

        elif divident_A < divider_M:
            print(
                f"До: {divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M} = [{divident_A}^2 ≡ {divident_A ** 2 % divider_M} mod {divider_M}]")
            trash *= divident_A
            exponent_A = (exponent_A - 1) // 2
            divident_A **= 2
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M}")

        elif divident_A > divider_M:
            print(f"До: {divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M} = [{divident_A} ≡ {divident_A % divider_M} mod {divider_M}]")
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M}")
    return divident_A




divident_A = int(input("Введите a: "))
print_divident_A = divident_A

New_Divider_A = int(input("Введите b: "))
print_New_Divider_A = New_Divider_A

divider_M = int(input("Введите делитель: "))
print_divident_M = divider_M

exponent_A = 1
print_divident_exp_A = exponent_A

print(f"{divident_A}x ≡ {New_Divider_A} (mod{divider_M})")

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


NOD_AM = 1
if NOD(divident_A, divider_M) != 1 and New_Divider_A % NOD(divident_A, divider_M) == 0:
    print(f"НОД({divident_A};{divider_M}) = {NOD(divident_A, divider_M)}; {New_Divider_A} делится на {NOD(divident_A, divider_M)} => сравнение разрешимо и имеет {NOD(divident_A, divider_M)} решений")
    NOD_AM = NOD(divident_A, divider_M)
    m = divider_M / NOD_AM
    test = divider_M

    divident_A = divident_A / NOD_AM
    print_divident_A = divident_A
    New_Divider_A = New_Divider_A / NOD_AM
    print_New_Divider_A = New_Divider_A
    divider_M = divider_M / NOD_AM
    print_divident_M = divider_M
    print(f"{divident_A}^{exponent_A} * {New_Divider_A} mod {divider_M} ")

elif New_Divider_A % NOD(divident_A, divider_M) != 0:
    print(f"Сравнение не разрешимо. {New_Divider_A} / {NOD(divident_A, divider_M)} != целому числу")

if gcd(int(divident_A), int(divider_M)) == 1:
    f = 1

    print(f"Т.к. НОД({divident_A};{divider_M}) = 1, то используем теорему Эйлера\n")
    if is_prime(int(divider_M)):
        f = divider_M - 1
    else:
        f *= divider_M
        decomposition = canonical_decomposition(int(divider_M))
        for i in decomposition:
            f *= (1 - 1 / int(i))

    f = int(f) - 1
    exponent_A = f

    print(f"x0 ={divident_A}^φ({divider_M})-1 * {New_Divider_A} mod {divider_M} = {divident_A}^{exponent_A} * {New_Divider_A} mod {divider_M}")

    result = Eiler(divident_A, exponent_A, divider_M, NOD_AM, New_Divider_A)
    print(f"x0 = {result}")



    if NOD_AM > 1:
        print(f"m = {test} / {NOD_AM} = {m}")
        for i in range(int(NOD_AM-1)):
            x = result + (i+1)*m
            print(f"x{i+1} = x0 + {i+1}m = {result} + {i+1}*{m} = {x}")








