from fractions import Fraction
from prettytable import PrettyTable,ALL

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


print("Выберите по какому варианту считать: ")
print("1 - С вводом варианта по списку\n2 - С вводом готовых значений")
Choose = int(input("Ваш выбор: "))

if Choose == 1:
    vibory = [17, 19, 23, 29, 31]
    Variant = int(input("Введите ваш вариант: "))
    p = vibory[Variant % 5]
    a = 1 + (Variant % p)
    b = 1 + (Variant % p)

elif Choose == 2:
    p = int(input("Введите p: "))
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
else:
    print("Такого выбора нет....")
    exit()

print(f"E{p}({a},{b})")
print(f"y^2 = x^3 + {a}x + {b} mod {p}")

Mass_p = []
Mass_X = []
Mass_Y = []

for i in range(p):
    Mass_p.append(i)
    Mass_X.append(((i**3+a*i+b) % p))
    Mass_Y.append(i**2 % p)

Mass_print_p_X = Mass_p.copy()
Mass_print_p_Y = Mass_p.copy()
Mass_print_X = Mass_X.copy()
Mass_print_Y = Mass_Y.copy()

Mass_print_p_X.insert(0, 'x')
Mass_print_p_Y.insert(0, 'y')
vstavka = "x^3 + " + str(a) + "x " + str(b) + " mod" + str(p)

Mass_print_X.insert(0, vstavka)
Mass_print_Y.insert(0, 'y^2')

print(Mass_print_X)
mytable = PrettyTable()
mytable.hrules=ALL
mytable.field_names = Mass_print_p_X
mytable.add_rows([Mass_print_X,Mass_print_p_Y,Mass_print_Y])
print(mytable)

Points = []

Print_Points = ''
for i in range(p):
    for j in range(p):
        if Mass_X[i] == Mass_Y[j]:
            Points.append([i, j])
            Print_Points += "(" + str(i) + "," + str(j) + ")  "


print("Точки: ",Print_Points)
print(f"Порядок эллептической кривой = {len(Points)+1} | {len(Points)} + O = {len(Points)+1}")


print("P+Q = Z(x3,y3)      |   P(x1,y1)  Q(x2,y2)")

dict = {}
for index, sublist in enumerate(Points):
    dict[index] = sublist

print("\nТочки для выбора: ")
for key, value in dict.items():
    print(f'{key}: {value}')
#print(dict)

print("Введите номера для выбора.")


while True:
    Nomer1 = int(input("Введите номер первой точки: "))
    Nomer2 = int(input("Введите номер второй точки: "))
    Point1 = dict[Nomer1]
    Point2 = dict[Nomer2]
    if Point1[0] == Point2[0]:
        print(f"Ошибка!")
    else:
        break

print(f"P({Point1[0]},{Point1[1]}) + Q({Point2[0]},{Point2[1]})")

print(f"λ = ({Point2[1]} - {Point1[1]}) / ({Point2[0]} - {Point1[0]}) ")
lyambda = (Point2[1]-Point1[1])/(Point2[0]-Point1[0])



if lyambda % 1 != 0:
    fraction = Fraction(lyambda).limit_denominator()
    test = str(fraction)

    slasher = test.index('/')

    if "-" in test:
        minus = test.index('-')

    first_number = int(test[:slasher])

    second_number = int(test[slasher + 1:])

    f = 1

    if NOD(second_number,p) != 1:
        print(f"Ошибка!\nНОД {second_number} и {p} != 1")
        exit()

    if is_prime(second_number):
        f = p - 1
    else:
        f *= p
        decomposition = canonical_decomposition(int(p))
        for i in decomposition:
            f *= (1 - 1 / int(i))

    second_number **= f-1

    lyambda = (first_number * (second_number % p)) % p


else: lyambda %= p

print(f"λ = {lyambda}")

print('x3 = λ^2-x1-x2')
print('y3 = λ(x1-x3)-y1\n')
x3 = lyambda**2 - Point1[0] - Point2[0]
y3 = lyambda*(Point1[0]-x3)-Point1[1]

x3 %=p
y3 %=p

print(f'x3 ={x3}')
print(f'y3 ={y3}\n')

print(f"P+Q = Z({x3},{y3})")

print(f"P({Point1[0]},{Point1[1]}) = 2P\n")

print(f"λ = (3*{Point1[0]}**2+{a}) / (2*{Point1[1]})")
lyambda = ((3*Point1[0]**2+a)/(2*Point1[1]))


if lyambda % 1 != 0:
    fraction = Fraction(lyambda).limit_denominator()
    test = str(fraction)

    slasher = test.index('/')

    if "-" in test:
        minus = test.index('-')

    first_number = int(test[:slasher])

    second_number = int(test[slasher + 1:])
    f = 1

    if NOD(second_number,p) != 1:
        print(f"Ошибка!\nНОД {second_number} и {p} != 1")
        exit()

    if is_prime(second_number):
        f = p - 1
    else:
        f *= p
        decomposition = canonical_decomposition(int(p))
        for i in decomposition:
            f *= (1 - 1 / int(i))

    second_number **= f-1

    lyambda = (first_number * (second_number % p)) % p


else:
    lyambda %= p

print(f"λ = {lyambda}")
print("2P(x4,y4)")


print('x4 = λ^2-2*x1')
print('y4 = λ(x1-x4)-y1\n')

x4 = (lyambda**2-2*Point1[0]) % p
y4 = (lyambda*(Point1[0]-x4)-Point1[1]) % p

print(f"2P=S({x4},{y4})")






