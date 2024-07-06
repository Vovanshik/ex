from fractions import Fraction
from prettytable import PrettyTable, ALL



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


def p_q(Point1, Point2, p, a):
    #print(f"λ = ({Point2[1]} - {Point1[1]}) / ({Point2[0]} - {Point1[0]}) ")
    if (Point2[0] - Point1[0]) == 0:
        print("Деление на ноль")
        return -1
    lyambda = (Point2[1] - Point1[1]) / (Point2[0] - Point1[0])

    if lyambda % 1 != 0:
        fraction = Fraction(lyambda).limit_denominator()
        test = str(fraction)

        slasher = test.index('/')

        if "-" in test:
            minus = test.index('-')

        first_number = int(test[:slasher])

        second_number = int(test[slasher + 1:])

        f = 1

        if NOD(second_number, p) != 1:
            print(f"Ошибка!\nНОД {second_number} и {p} != 1")
            return -1

        if is_prime(p):
            f = p - 1
        else:
            f *= p
            decomposition = canonical_decomposition(int(p))
            for i in decomposition:
                f *= (1 - 1 / int(i))

        second_number **= f - 1

        lyambda = (first_number * (second_number % p)) % p


    else:
        lyambda %= p

    #print(f"λ = {lyambda}")

    #print('x3 = λ^2-x1-x2')
    #print('y3 = λ(x1-x3)-y1\n')
    x3 = lyambda ** 2 - Point1[0] - Point2[0]
    y3 = lyambda * (Point1[0] - x3) - Point1[1]

    x3 %= p
    y3 %= p

    #print(f'x3 ={x3}')
    #print(f'y3 ={y3}\n')

    #print(f"P+Q = Z({x3},{y3})")



    Point3 = [x3, y3]

    return Point3


def P_peremn(Point1, p, a):
    #print(f"P({Point1[0]},{Point1[1]}) = 2P\n")

    #print(f"λ = (3*{Point1[0]}**2+{a}) / (2*{Point1[1]})")
    if (2 * Point1[1]) == 0:
        print("Деление на ноль")
        return -1
    lyambda = ((3 * Point1[0] ** 2 + a) / (2 * Point1[1]))

    if lyambda % 1 != 0:
        fraction = Fraction(lyambda).limit_denominator()
        test = str(fraction)

        slasher = test.index('/')

        if "-" in test:
            minus = test.index('-')

        first_number = int(test[:slasher])

        second_number = int(test[slasher + 1:])
        f = 1

        if NOD(second_number, p) != 1:
            print(f"Ошибка!\nНОД {second_number} и {p} != 1")
            return -1

        if is_prime(p):
            f = p - 1
        else:
            f *= p
            decomposition = canonical_decomposition(int(p))
            for i in decomposition:
                f *= (1 - 1 / int(i))

        second_number **= (f - 1)

        lyambda = (first_number * (second_number % p)) % p


    else:
        lyambda %= p

    #print(f"λ = {lyambda}")
    #print("2P(x4,y4)")

    #print('x4 = λ^2-2*x1')
    #print('y4 = λ(x1-x4)-y1\n')

    x4 = (lyambda ** 2 - 2 * Point1[0]) % p
    y4 = (lyambda * (Point1[0] - x4) - Point1[1]) % p

    #print(f"2P=S({x4},{y4})")

    Point4 = [x4, y4]

    return Point4

def umnosh_P(Point1,C):
    #print(f"P({Point1[0]},{Point1[1]})")
    Mass_points = []
    sch = 1
    sch_summ = 0
    for m in range(C):
        if sch % 2 != 0:
            if len(Mass_points) == 0:
                Mass_points.append(Point1)
                sch += 1
            elif sch != 1:
                #print(f"Вычисляем {sch}P.... ")
                Point2 = p_q(Mass_points[sch_summ], Mass_points[sch_summ + 1], p, a)
                if Point2 == -1:
                    Mass_points.append(0)
                    break

                Mass_points.append(Point2)
                sch_summ += 1
                sch += 1

        else:
            #print(f"Вычисляем {sch}P.... ")
            c = ((len(Mass_points) + 1) / 2) - 1
            Point2 = P_peremn(Mass_points[int(c)], p, a)
            if Point2 == -1:
                Mass_points.append(0)
                break
            Mass_points.append(Point2)
            sch += 1

    #print("\nРезультат:")

    # for i in range(len(Mass_points)):
    #     print(f"{i + 1}P = ({Mass_points[i][0]};{Mass_points[i][1]})")

    # for i in range(C):
    #     print(f"{i + 1}P = ({Mass_points[i % len(Mass_points)][0]};{Mass_points[i % len(Mass_points)][1]})")
    for i in range(C-len(Mass_points)):
        Mass_points.append(Mass_points[i % len(Mass_points)])
    return Mass_points[-1]

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
    Mass_X.append(((i ** 3 + a * i + b) % p))
    Mass_Y.append(i ** 2 % p)

Mass_print_p_X = Mass_p.copy()
Mass_print_p_Y = Mass_p.copy()
Mass_print_X = Mass_X.copy()
Mass_print_Y = Mass_Y.copy()

Mass_print_p_X.insert(0, 'x')
Mass_print_p_Y.insert(0, 'y')
vstavka = "x^3 + " + str(a) + "x " + str(b) + " mod" + str(p)

Mass_print_X.insert(0, vstavka)
Mass_print_Y.insert(0, 'y^2')

mytable = PrettyTable()
mytable.hrules = ALL
mytable.field_names = Mass_print_p_X
mytable.add_rows([Mass_print_X, Mass_print_p_Y, Mass_print_Y])
print(mytable)

Points = []

Print_Points = ''
for i in range(p):
    for j in range(p):
        if Mass_X[i] == Mass_Y[j]:
            Points.append([i, j])
            Print_Points += "(" + str(i) + "," + str(j) + ")  "

print("Точки: ", Print_Points)
print(f"Порядок эллептической кривой = {len(Points) + 1} | {len(Points)} + O = {len(Points) + 1}")

print("P+Q = Z(x3,y3)      |   P(x1,y1)  Q(x2,y2)")

dict = {}
for index, sublist in enumerate(Points):
    dict[index] = sublist

print("\nТочки для выбора: ")
for key, value in dict.items():
    print(f'{key}: {value}')
# print(dict)

print("Введите номера для выбора:")

while True:
    Nomer1 = int(input("Введите номер первой точки: "))
    Point1 = dict[Nomer1]
    break


umnosh_P(Point1,1)
gen = int(input("Выберите генератор: 1. Конгруэнтный, 2. Инверсивный "))
C = int(input("Введите фиксированное значение C: "))

kol_vo = int(input("Введите количество подсчетов: "))
kol_vo+=1
print('Выберите начальную точку x0(x,y):')
while True:
    nach_x = int(input('x:'))
    nach_y = int(input('y:'))
    if nach_x >=p or nach_y >= p:
        print("Точки вне поля\n Попробуйте снова")
    else:
        break



x0 = [nach_x, nach_y]

X = [x0]
if gen == 1:
    if C == 0:
        x_i = [Point1 for i in range(kol_vo)]
        for i in x_i:
            X.append(i)

    elif C == 1:
        for i in range(kol_vo):
            if i != 0:
                if X[i - 1] == Point1:
                    x_i = P_peremn(X[i - 1], p, a)
                elif X[i-1] == 0:
                    X.append(Point1)
                    continue
                else:
                    x_i = p_q(X[i - 1], Point1, p, a)
                if x_i == -1:
                    X.append(0)
                else:
                    X.append(x_i)


    else:
        for i in range(kol_vo):
            if i != 0:
                if X[i - 1] == 0:
                    X.append(Point1)
                else:
                    x_i = umnosh_P(X[i - 1], C)
                    if x_i == Point1:
                        x_i = P_peremn(x_i, p, a)
                    else:
                        x_i = p_q(x_i, Point1, p, a)
                    if x_i == -1:
                        X.append(0)
                    else:
                        X.append(x_i)
    sch = 1
    for i in range(len(X)):
        if i != 0:
            if X[i] == X[0]:
                sch = i + 1
                break

    for i in range(len(X)):
        print(f"x{i} = {X[i]}")

    print(f"Период последовательности равен {sch}")

if gen == 2:
    if C == 0:
        x_i = [Point1 for i in range(kol_vo)]
        for i in x_i:
            X.append(i)

    elif C == 1:
        for i in range(kol_vo):
            if i != 0:
                Obratnoe = X[i - 1].copy()
                Obratnoe[1] = (-Obratnoe[1]) % p
                if Obratnoe == Point1:
                    x_i = P_peremn(X[i - 1], p, a)
                else:
                    x_i = p_q(Obratnoe, Point1, p, a)
                if x_i == -1:
                    X.append(0)
                else:
                    X.append(x_i)


    else:
        for i in range(kol_vo):
            if i != 0:
                if X[i - 1] == 0:
                    X.append(Point1)
                else:
                    Obratnoe = X[i - 1].copy()
                    Obratnoe[1] = (-Obratnoe[1]) % p
                    x_i = umnosh_P(Obratnoe, C)
                    if x_i == Point1:
                        x_i = P_peremn(x_i, p, a)
                    elif x_i == 0:
                        x_i = Point1
                    else:
                        x_i = p_q(x_i, Point1, p, a)
                    if x_i == -1:
                        X.append(0)
                    else:
                        X.append(x_i)

    sch = 1
    for i in range(len(X)):
        if i != 0:
            if X[i] == X[0]:
                sch = i + 1
                break

    for i in range(len(X)):
        print(f"x{i} = {X[i]}")

    print(f"Период последовательности равен {sch}")









