from fractions import Fraction
from prettytable import PrettyTable,ALL
import math

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

def p_q(Point1,Point2):
    #print(f"λ = ({Point2[1]} - {Point1[1]}) / ({Point2[0]} - {Point1[0]}) ")
    if (Point2[0] - Point1[0]) == 0:
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

    # print(f"λ = {lyambda}")
    #
    # print('x3 = λ^2-x1-x2')
    # print('y3 = λ(x1-x3)-y1\n')
    x3 = lyambda ** 2 - Point1[0] - Point2[0]
    y3 = lyambda * (Point1[0] - x3) - Point1[1]

    x3 %= p
    y3 %= p

    # print(f'x3 ={x3}')
    # print(f'y3 ={y3}\n')
    #
    # print(f"P+Q = Z({x3},{y3})")



    Point3 = [x3,y3]

    return Point3

def P_peremn(Point1):
    #print(f"P({Point1[0]},{Point1[1]}) = 2P\n")

    #print(f"λ = (3*{Point1[0]}**2+{a}) / (2*{Point1[1]})")
    if (2*Point1[1]) == 0:
        #print("Деление на ноль")
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
            #print(f"Ошибка!\nНОД {second_number} и {p} != 1")
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

    # print(f"λ = {lyambda}")
    # print("2P(x4,y4)")
    #
    # print('x4 = λ^2-2*x1')
    # print('y4 = λ(x1-x4)-y1\n')

    x4 = (lyambda ** 2 - 2 * Point1[0]) % p
    y4 = (lyambda * (Point1[0] - x4) - Point1[1]) % p

    #print(f"2P=S({x4},{y4})")

    Point4 = [x4,y4]

    return Point4






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
    Point1 = dict[Nomer1]
    break
print("Вариант 12")
print(f"P({Point1[0]},{Point1[1]})")
Massive_Points = []
sch = 1
sch_summ = 0

N1 = p + 1 + 2*round(math.sqrt(p),1)
print(f"N1 = {p} + 1 +2√{p} = {p+1} + 2*{round(math.sqrt(p),1)}={p + 1 + 2*round(math.sqrt(p),1)}")
N1 = round(math.sqrt(N1), 1)

m = math.ceil(N1)
print(f"m = ⌈√N1⌉ = ⌈{N1}⌉ = {m}")

for i in range(m):
    if sch % 2 == 1:
        if len(Massive_Points) == 0:
            Massive_Points.append(Point1)
            sch += 1
        elif sch > 1:
            Point2 = p_q(Massive_Points[sch_summ], Massive_Points[sch_summ+1])
            if Point2 == -1:
                Massive_Points.append(0)
                break
            Massive_Points.append(Point2)
            sch += 1
            sch_summ += 1

    else:
        c = ((len(Massive_Points) + 1) / 2) - 1
        Point2 = P_peremn(Massive_Points[int(c)])
        if Point2 == -1:
            Massive_Points.append(0)
            break
        Massive_Points.append(Point2)
        sch += 1

New_Massive_points = []
for i in range(m):
    New_Massive_points.append(Massive_Points[i % len(Massive_Points)])
Q = New_Massive_points[m-1].copy()


Massiv_print_t = []
Massiv_print_t.append("t")
for i in range(m):
    Massiv_print_t.append(i+1)


Test_sp = []
for x in New_Massive_points:
    if x != 0:
        Test_sp.append(f'({int(x[0])},{int(x[1])})')
    else:
        Test_sp.append('0')
Test_sp.insert(0, "2P")



mytable_new = PrettyTable()
mytable_new.hrules=ALL
mytable_new.field_names = Massiv_print_t
mytable_new.add_rows([Test_sp])
print(mytable_new)


print(f"Q = -mP = -{m}({Massive_Points[0][0]},{Massive_Points[0][1]}) = - ({Q[0]},{Q[1]}) = ({Q[0]},-{Q[1]})"
      f"= ({Q[0]},{-Q[1] % p}) mod {p}")
Q[1] = -Q[1] % p

per = 0
R = 0
Mass_R = R
while True:
    if Mass_R not in New_Massive_points:
        if Mass_R == 0:
            print(f"i = {per}, R = {R} - не содержится в таблице"
                  f"\nR = R + Q = 0 + ({Q[0]},{Q[1]}) = ({Q[0]},{Q[1]})")
            Mass_R = Q
        else:
            Mass_R_do = Mass_R.copy()
            if Mass_R == Q:
                Mass_R = P_peremn(Q)
            else:
                Mass_R = p_q(Mass_R, Q)
            if Mass_R == -1:
                Mass_R = New_Massive_points[0]
                print(f"i = {per}, R = ({Mass_R_do[0]},{Mass_R_do[1]}) - не содержится в таблице"
                      f"\nR = R + Q = ({Mass_R_do[0]},{Mass_R_do[1]}) + ({Q[0]},{Q[1]}) = ({Mass_R[0]},{Mass_R[1]})")
            else:
                print(f"i = {per}, R = ({Mass_R_do[0]},{Mass_R_do[1]}) - не содержится в таблице"
                      f"\nR = R + Q = ({Mass_R_do[0]},{Mass_R_do[1]}) + ({Q[0]},{Q[1]}) = ({Mass_R[0]},{Mass_R[1]})")
        per += 1
    else:
        if Mass_R != 0:
            pozition = New_Massive_points.index(Mass_R) + 1
            print(f"({Mass_R[0]},{Mass_R[1]}) содержится в таблице при t = {pozition}")
            print(f"h = m*i+t = {m}*{per}+{pozition} = {m * per + pozition} - порядок точки P({Massive_Points[0][0]};{Massive_Points[0][1]})")
            break
        else:
            pozition = New_Massive_points.index(Mass_R) + 1
            print(f"({Mass_R}) содержится в таблице при t = {pozition}")
            print(f"h = m*i+t = {m}*{per}+{pozition} = {m * per + pozition} - порядок точки P({Massive_Points[0][0]};{Massive_Points[0][1]})")
            break




