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
            print(f"{a} > {p}. Не пойдет. Обновляем...{a} mod {p} = ({a%p} / {p}) | ({p}*{a // p} + {a%p})/{p}")
        if a < 0:
            print(f"{a} < 0. Не пойдет. Обновляем...{a} mod {p} = ({a%p} / {p}) | ({p}*{a // p} + {a%p})/{p}")
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




DroBb = input("Введите переменные выражения: ")
a = int(DroBb[:DroBb.find('/')])
b = int(DroBb[DroBb.find('/')+1:])

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
        Mass_Yakobi *= calculateLegendre(a,i)
        Mass_Yakobi2.append(Mass_Yakobi)

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


