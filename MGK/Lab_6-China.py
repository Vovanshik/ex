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

def print_uravn(Mass_a,Mass_m,Mass_x):
    for i in range(len(Mass_a)):
        if i == 0:
            if Mass_x[i] == 1:
                print(f"⎛ x ≡ {Mass_a[i]} mod {Mass_m[i]}")
            else:
                print(f"⎛ {Mass_x[i]}x ≡ {Mass_a[i]} mod {Mass_m[i]}")
        elif i != len(Mass_a) - 1:
            if Mass_x[i] == 1:
                print(f"| x ≡ {Mass_a[i]} mod {Mass_m[i]}")
            else:
                print(f"| {Mass_x[i]}x ≡ {Mass_a[i]} mod {Mass_m[i]}")
        else:
            if Mass_x[i] == 1:
                print(f"⎝ x ≡ {Mass_a[i]} mod {Mass_m[i]}")
            else:
                print(f"⎝ {Mass_x[i]}x ≡ {Mass_a[i]} mod {Mass_m[i]}")


sch_ur = int(input("Введите кол-во уравнений в системе: "))
print("Введите систему:")
sch = 1


Mass_a = []
Mass_m = []
Mass_x = []
for i in range(sch_ur):
    print(f"Введите коэффициенты {i+1} уравнения:")
    a = int(input())
    b = int(input())
    c = int(input())
    if b > c:
        print(f"{b} > {c} | Ошибка")
        exit()
    Mass_a.append(b)
    Mass_m.append(c)
    Mass_x.append(a)

sch = 0
for i in Mass_m:
    for j in Mass_m:
        if i != j and NOD(i, j) != 1:
            sch += 1
print_uravn(Mass_a,Mass_m,Mass_x)

if sch > 0:
    print("Числа не взаимнопростые")
    exit()

for i in range(len(Mass_a)):

    if Mass_a[i] % Mass_x[i] == 0 and Mass_m[i] % Mass_x[i] == 0:
        bilo = Mass_a[i]
        bilo1 = Mass_m[i]
        bilo2 = Mass_x[i]
        Mass_a[i] = int(Mass_a[i] / Mass_x[i])
        Mass_m[i] = int(Mass_m[i] / Mass_x[i])
        if Mass_x[i] > 1:
            print("-----------------")
            print(f"{bilo2}x ≡ {bilo} mod {bilo1} |:{bilo2}")
            print(f"x ≡ {Mass_a[i]} mod {Mass_m[i]}")
        Mass_x[i] = 1

    else:
        if NOD(Mass_x[i], Mass_m[i]) == 1:
            print("-----------------")
            print(f"{Mass_x[i]}x ≡ {Mass_a[i]} mod {Mass_m[i]}")
            print(f"НОД({Mass_x[i]},{Mass_m[i]}) = 1 -> x0 = [a^(φ(m)-1) * b mod m] =")
            print(f"{Mass_x[i]}^(φ({Mass_m[i]})-1) * {Mass_a[i]} mod {Mass_m[i]} = {((Mass_x[i] ** (Mass_m[i]-2)) * Mass_a[i]) % Mass_m[i]} mod {Mass_m[i]} ")
            Mass_a[i] = ((Mass_x[i] ** (Mass_m[i]-2)) * Mass_a[i]) % Mass_m[i]
            Mass_x[i] = 1
        else:
            print("Ошибка")
            exit()

print_uravn(Mass_a, Mass_m, Mass_x)




for i in range(len(Mass_a)):
    print(f"a{i+1} = {Mass_a[i]}")

for i in range(len(Mass_m)):
    print(f"m{i+1} = {Mass_m[i]}")

Mass_M = []
pere = 1
text = ""
sch = 1
for i in Mass_m:
    for j in Mass_m:
        if i != j:
            text += f"{str(j)}*"
            pere *= j
    text = text.rstrip('*')
    print(f"M{sch} = {text} = {pere}")
    sch+=1
    text = ""
    Mass_M.append(pere)
    pere = 1




Mass_N = []
print("Ni = Mi ^(-1) mod mi")
for i in range(len(Mass_a)):
    print(f"N{i+1} = {Mass_M[i]}^(-1) mod {Mass_m[i]} = {Mass_M[i]}^(φ({Mass_m[i]})-1) mod {Mass_m[i]} = {(Mass_M[i]**(Mass_m[i]-2)) % Mass_m[i]} mod {Mass_m[i]}")
    Mass_N.append((Mass_M[i]**(Mass_m[i]-2)) % Mass_m[i])

proizv_m = 1
text_m = ""
for i in Mass_m:
    text_m += f"{i}*"
    proizv_m *= i

text_m = text_m.rstrip("*")

summa = 0
text_umnosh = ""
for i in range(len(Mass_a)):
    text_umnosh += f"{Mass_a[i]}*{Mass_M[i]}*{Mass_N[i]}+"
    summa += Mass_a[i]*Mass_M[i]*Mass_N[i]
text_umnosh = text_umnosh.rstrip("+")

x0 = summa % proizv_m
text_umnosh = f"ъъx0 = ({text_umnosh}) mod ({text_m}) = {summa} (mod {proizv_m}) = {x0}"
print(text_umnosh)







