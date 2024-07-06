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





def Ferma(divident_A,exponent_A,divider_M,NOD_AM,New_Divider_A):
    new_exponent = 0
    trash = 1
    while exponent_A >= 1:
        if exponent_A >= divider_M:
            print(f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M}")
            new_exponent = exponent_A // (divider_M - 1)
            exponent_A -= new_exponent * (divider_M - 1)
            if exponent_A >= divider_M - 1:
                exponent_A -= divider_M - 1
            if exponent_A == 0:
                divident_A = 1
                print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")



        elif exponent_A == 1:
            if NOD_AM >1 :
                print(f"{divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M} | * {NOD_AM}")
            divident_A = (divident_A * trash * New_Divider_A) % (divider_M)
            divident_A *= NOD_AM

            break


        elif divident_A < divider_M and exponent_A % 2 == 0 and exponent_A != 0:
            print(
                f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A}^2 ≡ {divident_A ** 2 % divider_M} mod {divider_M}]")
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
            divider_M *= NOD_AM
            divident_A *= NOD_AM
            print(f"После: {divident_A} mod {divider_M}")
            exponent_A -= exponent_A

        elif divident_A < divider_M:
            print(
                f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A}^2 ≡ {divident_A ** 2 % divider_M} mod {divider_M}]")
            trash *= divident_A
            exponent_A = (exponent_A - 1) // 2
            divident_A **= 2
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")

        elif divident_A > divider_M:
            print(
                f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A} ≡ {divident_A % divider_M} mod {divider_M}]")
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")

    return divident_A


def Eiler(divident_A,exponent_A,divider_M,NOD_AM,New_Divider_A,f):
    print(f"Теорема Эйлера: {divident_A}^{int(f)} ≡ 1(mod {divider_M})")
    new_exponent = 0
    trash = 1
    while exponent_A >= 1:
        if exponent_A >= divider_M:
            print(f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M}")
            new_exponent = exponent_A // (f)
            exponent_A -= new_exponent * (f)
            if exponent_A >= divider_M - 1:
                exponent_A -= divider_M - 1

            if exponent_A == 0:
                divident_A = 1
                print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")



        elif exponent_A == 1:
            if NOD_AM >1 :
                print(f"{divident_A}^{exponent_A}*{trash}*{New_Divider_A} mod {divider_M} | * {NOD_AM}")
            divident_A = (divident_A * trash * New_Divider_A) % (divider_M)
            divident_A *= NOD_AM
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
            divider_M *= NOD_AM
            divident_A *= NOD_AM
            print(f"После: {divident_A} mod {divider_M}")
            exponent_A -= exponent_A

        elif divident_A < divider_M:
            print(
                f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A}^2 ≡ {divident_A ** 2 % divider_M} mod {divider_M}]")
            trash *= divident_A
            exponent_A = (exponent_A - 1) // 2
            divident_A **= 2
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")

        elif divident_A > divider_M:
            print(
                f"До: {divident_A}^{exponent_A}*{trash} mod {divider_M} = [{divident_A} ≡ {divident_A % divider_M} mod {divider_M}]")
            divident_A = divident_A % divider_M
            print(f"После: {divident_A}^{exponent_A}*{trash} mod {divider_M}")
    return divident_A

kol_vo = int(input("Введите кол-во чисел перед модом: "))


if kol_vo > 1:
    sch = 0
    stroka = ""
    for i in range(kol_vo):

        divident_A = int(input("Введите делимое: "))
        print_divident_A = divident_A
        exponent_A = int(input("Введите степень: "))
        print_divident_exp_A = exponent_A
        divider_M = int(input("Введите делитель: "))
        print_divident_M = divider_M
        if i != (kol_vo-1):
            stroka += str(divident_A) + "^" + str(exponent_A) + "+"
        else: stroka += str(divident_A) + "^" + str(exponent_A)

        if exponent_A % 2 == 0 and divident_A < 0:
            divident_A *= -1

        print(divident_A, divider_M, exponent_A)


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


        New_Divider_A = 1

        NOD_AM = 1
        if NOD(divident_A, divider_M) != 1:
            NOD_AM = NOD(divident_A, divider_M)
            exponent_A -= 1
            New_Divider_A = divident_A / NOD(divident_A, divider_M)
            divider_M = divider_M / NOD(divident_A, divider_M)
            print(f"{divident_A}^{exponent_A} * {New_Divider_A} mod {divider_M})")



        if is_prime(int(divider_M)) and gcd(int(divident_A), int(divider_M)) == 1 and isinstance(divident_A, int):
            print(f"Теорема фермы: {divident_A}^{divider_M - 1} ≡ 1(mod {divider_M})")
            result = Ferma(divident_A, exponent_A, divider_M, NOD_AM, New_Divider_A)
            print(f"{print_divident_A}^{print_divident_exp_A} mod {print_divident_M} = {result}")
            sch += result



        elif gcd(int(divident_A), int(divider_M)) == 1 and isinstance(divident_A, int):
            f = 1
            print("Теорема Эйлера\n")
            if is_prime(int(divider_M)):
                f = divider_M - 1
            else:
                f *= divider_M
                decomposition = canonical_decomposition(int(divider_M))
                for i in decomposition:
                    f *= (1 - 1 / int(i))

            f = int(f)
            result = Eiler(divident_A, exponent_A, divider_M, NOD_AM, New_Divider_A, f)
            print(f"{print_divident_A}^{print_divident_exp_A} mod {print_divident_M} = {result}")
            sch += result


    print(f"{stroka} mod {divider_M} = {sch}")

else:
    divident_A = int(input("Введите делимое: "))
    print_divident_A = divident_A
    exponent_A = int(input("Введите степень: "))
    print_divident_exp_A = exponent_A
    divider_M = int(input("Введите делитель: "))
    print_divident_M = divider_M

    if exponent_A % 2 == 0 and divident_A < 0:
        divident_A *= -1

    print(divident_A, divider_M, exponent_A)


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


    New_Divider_A = 1

    NOD_AM = 1
    if NOD(divident_A, divider_M) != 1:
        NOD_AM = NOD(divident_A, divider_M)
        exponent_A -= 1
        New_Divider_A = divident_A / NOD(divident_A, divider_M)
        divider_M = divider_M / NOD(divident_A, divider_M)
        print(f"{divident_A}^{exponent_A} * {New_Divider_A} mod {divider_M} ")

    if is_prime(int(divider_M)) and gcd(int(divident_A), int(divider_M)) == 1 and isinstance(divident_A, int):
        print(f"Теорема фермы: {divident_A}^{divider_M - 1} ≡ 1(mod {divider_M})")
        result = Ferma(divident_A, exponent_A, divider_M, NOD_AM, New_Divider_A)
        print(f"{print_divident_A}^{print_divident_exp_A} mod {print_divident_M} = {result}")



    elif gcd(int(divident_A), int(divider_M)) == 1 and isinstance(divident_A, int):
        f = 1
        print("Теорема Эйлера\n")
        if is_prime(int(divider_M)):
            f = divider_M - 1
        else:
            f *= divider_M
            decomposition = canonical_decomposition(int(divider_M))
            for i in decomposition:
                f *= (1 - 1 / int(i))

        f = int(f)
        result = Eiler(divident_A, exponent_A, divider_M, NOD_AM, New_Divider_A, f)
        print(f"{print_divident_A}^{print_divident_exp_A} mod {print_divident_M} = {result}")







