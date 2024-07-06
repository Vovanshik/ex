from prettytable import PrettyTable,ALL

def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    return False

def factorize(n):
    factors = []

    p = 2
    while True:
        while n % p == 0 and n > 0:
            factors.append(p)
            n = n / p
        p += 1
        if p > n / p:
            break
    if n > 1:
        factors.append(int(n))
    return factors


def calculateLegendre(a, p):
    if a >= p or a < 0:
        print("Используем 1 правило.")
        if a >= p:
            print(f"{a} > {p}. Используем 1 правило. Обновляем...{a} mod {p} = ({a%p} / {p}) | ({p}*{a // p} + {a%p})/{p}")
        if a < 0:
            print(f"{a} < 0. Используем 1 правило. Обновляем...{a} mod {p} = ({a%p} / {p}) | ({p}*{a // p} + {a%p})/{p}")
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:
        print(f"Использовали 4 правило, так как {a}/{p} , где a = {a}")
        return a
    elif a == 2:
        print(f"Использовали 6 правило, так как {a}/{p} , где a = {a}")
        if p % 8 == 1 or p % 8 == 7:
            print(f"{p} ≡ +-1 mod 8 => возвращаем 1")
            return 1
        else:
            print(f"{p} ≡ +-3 mod 8 => возвращаем -1")
            return -1
    elif a == p - 1:
        print(f"{a}/{p} | Использовали 8 правило")
        if p % 4 == 1:
            print(f"{a}/{p} = 1")
            return 1
        else:
            print(f"{a}/{p} = -1")
            return -1
    elif not is_prime(a):
        print(f"{a}/{p} | Использовали 3 правило, тк {a} - составное")
        factors = factorize(a)
        text = "Множители " + str(a) + " "
        for i in factors:
            text += f"({i}/{p}) *"
        text = text[:-1]
        print(text)
        result = 1
        for element in factors:
            result *= calculateLegendre(element, p)
        return result
    else:

        if ((p - 1) / 2) % 2 == 0 or ((a - 1) / 2) % 2 == 0:
            print(f"{a}/{p} | Использовали 7 правило, тк {a} и {p} - простые и {p} != 2 , {a} != 2")
            print(f"(-1)^(({p}-1)/2) * (({a}-1)/2) * ({p}/{a}) = (-1)^({(p-1)/2}) * ({(a-1)/2}) * ({p}/{a}) =  1 * ({p}/{a})")
            return calculateLegendre(p, a)
        else:
            print(f"{a}/{p} | Использовали 7 правило, тк {a} и {p} - простые и {p} != 2 , {a} != 2")
            print(f"(-1)^(({p}-1)/2) * (({a}-1)/2) * ({p}/{a}) = (-1)^({(p-1)/2}) * ({(a-1)/2}) * ({p}/{a}) =  -1 * ({p}/{a})")
            return  calculateLegendre(-p, a)




print("Введите переменные выражения: ")
a = int(input("a = "))
b = int(input("b = "))

print(f"x^2 ≡ {a} mod{b}")


if is_prime(b):
    print(f"{a}/{b} = [{b} - простое => Символ Лежандра]")
    Lehandr = calculateLegendre(a, b)
    if Lehandr == 1:
        print(f"x^2 = {a} (mod{b}) = 1 Сравнение разрешимо")
    elif Lehandr == 0:
        print(f"x^2 = {a} (mod{b}) = 0 Сложно что либо сказать...")
    else:
        print(f"x^2 = {a} (mod{b}) = -1 Сравнение неразрешимо")

else:
    sostav = factorize(b)
    text = ""
    for i in sostav:
        text += str(i)+"x"
    text = text[:-1]
    print(f"{a}/{b} = [{b} = {text} - составное => Символ Якоби]")
    Mass_Yakobi = 1
    Mass_Yakobi2 = []
    for i in sostav:
        Mass_Yakobi *= calculateLegendre(a, i)
        Mass_Yakobi2.append(Mass_Yakobi)

    Lehandr = Mass_Yakobi

    if Mass_Yakobi == 1:
        text2 = ''
        for i in Mass_Yakobi2:
            text2 += str(i) + "*"
        text2 = text2[:-1]
        text2 += ' = 1 - сравнение разрешимо'
        print(text2)

    elif Mass_Yakobi == 0:
        text2 = ''
        for i in Mass_Yakobi2:
            text2 += str(i) + "*"
        text2 = text2[:-1]
        text2 += ' = 0 - тут нечего сказать...'
        print(text2)

    else:
        text2 = ''
        for i in Mass_Yakobi2:
            text2 += str(i) + "*"
        text2 = text2[:-1]
        text2 += ' = -1 - сравнение неразрешимо'
        print(text2)

print("\n\n")
if Lehandr == 1:
    if b % 4 == 3:
        print(f"1 Частный случай, тк {b} ≡ 3 mod 4")
        ost = b % 4
        m = 1
        while True:
            if 4 * m == b - ost:
                break
            m += 1
        print(f"{b} = 4*{m} + {ost} | m = {m}")
        print(f"x = +-a^(m+1) mod p = +-{a}^({m}+1) mod {b} = +-{(a**(m+1)) % b} mod {b}")
        x = (a^(m+1)) % b

    elif b % 8 == 5:
        print(f"2 Частный случай, тк {b} ≡ 5 mod 8")
        ost = b % 8
        m = 1
        while True:
            if 8 * m == b - ost:
                break
            m += 1
        print(f"{b} = 8*{m} + {ost} | m = {m}")

        if (a ** (2*m + 1)) % b == 1:
            print(f"a^(2*m + 1)) mod p = {a}^(2*{m}+1) mod {b} = {(a ** (2 * m + 1)) % b} mod {b} ≡ 1 mod {b}")
            print(f"x = +-a^(m+1) mod p = +-{a}^({m}+1) mod {b} = +-{a}^({m+1}) mod {b} = +-{(a ** (m + 1)) % b} "
                  f"mod {b}")
        elif (a ** (2*m + 1)) % b == b-1:
            print(f"a^(2*m + 1)) mod p = {a}^(2*{m}+1) mod {b} = {(a ** (2*m + 1)) % b} mod {b} ≡ -1 mod {b}")
            print(f"x = +-a^(m+1) * 2^(2m+1) mod p = +-{a}^({m}+1) * 2^(2*{m}+1) mod {b} =+-{a}^({m+1}) * 2^({2*m+1}) "
                  f"mod {b}= +-{((a ** (m + 1)) * (2**(2*m+1))) % b} mod {b}")

    else:
        print("Табличка")
        print(f"{b} ≠ 3 mod 4")
        print(f"{b} ≠ 5 mod 8")
        print("N = ? : N/p = -1")
        N = 1
        while True:
            print(f"N = {N}")
            if calculateLegendre(N, b) == -1:
                break
            N+=1
        print("\n")

        print(f"N = {N}")

        k = 1
        h = 1
        for i in range(b):
            for j in range(b):
                if (2**i)*j + 1 == b and j % 2 != 0:
                    k = i
                    h = j
                    break
            if (2**k)*h + 1 == b and h % 2 != 0:
                break


        print(f"k = {k}    h = {h}")

        a1 = int((a**((h+1)/2)) % b)
        print(f"a1 = a^((h+1)/2) mod p = {a}^(({h}+1)/2) mod {b} = {a}^{int((h+1)/2)}  mod {b} = {int((a ** ((h + 1) / 2)) % b)}")

        a2 = (a**(b-2)) % b
        print(f"a2 = a^(-1) mod p = {a}^({b}-2) mod {b} = {(a**(b-2)) % b}")

        N1 = (N**h) % b

        print(f"N1 = N^h mod p = {N}^{h} mod {b} = {(N**h) % b}")

        Mass_printa = []

        N2 = 1


        for i in range(k-1):
            new_b = (a1*N2) % b
            c = (a2*(new_b**2)) % b
            d = (c**(2**(k-2-i))) % b
            if d+1 == b:
                j = 1
                d = -1
            elif d == 1:
                j = 0
            else:
                j = -1

            N2 = (N2 * (N1 ** ((2**i) * j))) % b
            Mass_printa.append([i, new_b, c, d, j, N2])


        x = (a1 * N2) % b
        print(f"x = +-a1*N2(mod p) = +-{a1}*{N2} = +-{x}")

        Mass_Name = ['i', 'B ≡ a1*N2', 'c ≡ a2*B^2', 'd ≡ c^(2^(k-2-i))', 'j', 'N2 ≡ N2*N1^((2^i)*j)']

        mytable = PrettyTable()
        mytable.hrules = ALL
        mytable.field_names = Mass_Name
        for i in range(len(Mass_printa)):
            mytable.add_rows([Mass_printa[i]])
        print(mytable)



















