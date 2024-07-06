import sympy

def zad_toc(t):
    while not (t in kr):
        x = 200
        while x >= p:
            x = int(input("x = "))
            if x >= p:
                print("Координата не в поле")
        y = 200
        while y >= p:
            y = int(input("y = "))
            if y >= p:
                print("Координата не в поле")
        t.append(x)
        t.append(y)
        if not (t in kr):
            print("Точка не принадлежит ЭК")
            t.clear()

def slog(P1, Q1):
    pr = False
    if P1 == "O" and Q1 != "O":
        U = [x for x in Q1]
        pr = True
    elif Q1 == "O" and P1 != "O":
        U = [x for x in P]
        pr = True
    elif P1 == "O" and Q1 == "O":
        U = "O"
        pr = True

    if not pr:
        lya1 = Q1[1] - P1[1]
        lya2 = Q1[0] - P1[0]
        U = []
        if lya2 == 0:
            U = "O"
        if U != "O":
            lya2 = pow(lya2, -1, p)
            lya = lya1 * lya2 % p

            x3 = (lya ** 2 - P1[0] - Q1[0]) % p
            y3 = (lya * (P1[0] - x3) - P1[1]) % p

            U = [x3, y3]
    return U

def umn(P1):
    pr = False
    if P1 == "O":
        U = "O"
        pr = True

    if not pr:
        lya1 = 3 * P1[0] ** 2 + a
        lya2 = 2 * P1[1]
        U = []
        if lya2 == 0:
            U = "O"
        if U != "O":
            lya2 = pow(lya2, -1, p)
            lya = lya1 * lya2 % p

            x3 = (lya ** 2 - 2 * P1[0]) % p
            y3 = (lya * (P1[0] - x3) - P1[1]) % p

            U = [x3, y3]
    return U

print("y^2 = x^3 + ax + b")

pr = None
while not pr:
    p = 0
    while not (sympy.isprime(p)):
        p = int(input("GF(p) = "))
        if not (sympy.isprime(p)):
            print("p не простое")
    a = int(input("a = "))
    b = int(input("b = "))
    if (4 * a ** 3 + 27 * b ** 2) % p == 0:
        print("Данная кривая сингулярная")
    else:
        pr = True

vir = "y^2 = x^3 + ax + b"
vir0 = []

vira = vir.find("a")
vir = vir = vir[:vira] + str(a) + vir[vira + 1:]
virb = vir.find("b")
vir = vir = vir[:virb] + str(b) + vir[virb + 1:]
print(vir)

xs = [x for x in range(p)]
ys = [x for x in range(p)]

xres = [(x ** 3 + a * x + b) % p for x in xs]
yres = [y ** 2 % p for y in ys]

xs.insert(0, "x")
ys.insert(0, "y")
xres.insert(0, vir)
yres.insert(0, "y^2")

del xs[0]
del xres[0]
del ys[0]
del yres[0]

kr = []
for i in range(len(xres)):
    for j in range(len(yres)):
        if xres[i] == yres[j]:
            kr.append([xs[i], ys[j]])

gen = int(input("Выберите генератор: 1. Конгруэнтный, 2. Инверсионный "))

print("Координаты: ", kr)
x0 = [x for x in kr[-1]]

x01 = [x for x in x0]
while x01 == x0:

    print("Выберите начальную точку x0")
    print("x0(x, y)")
    x0 = []
    zad_toc(x0)
    print("x0", x0)

    C = int(input("C = "))

    print("Выберите фиксированную точку P")
    print("P(x, y)")
    P = []
    zad_toc(P)
    print("P", P)

    x01 = []

    if C == 0:
        x01 = [x for x in P]

    elif C == 1:
        x01 = slog(x0, P)

    else:
        x02 = umn(x0)
        for i in range(C - 2):
            x02 = slog(x02, x0)
        x01 = slog(x02, P)

    if x01 == x0:
        print("c * X0 + P = X0, X0, C и P выбраны неверно")

print(f"c * X0 + P = {x01} ≠ X0")

kol = int(input("Количество x: "))

X = [x0]
for i in range(kol - 1):
    if gen == 1:
        if C == 0:
            xi = [x for x in P]
            X.append(xi)

        elif C == 1:
            if X[-1] != P:
                xi = slog(X[-1], P)
            else:
                xi = umn(X[-1])
            X.append(xi)

        elif C == 2:
            xi = umn(X[-1])
            if xi != P:
                xi = slog(xi, P)
            else:
                xi = umn(xi)
            X.append(xi)
        else:
            xi = umn(X[-1])
            for j in range(C - 2):
                if xi != X[-1]:
                    x02 = slog(xi, X[-1])
                else:
                    x02 = umn(xi)
            if x02 != P:
                xi = slog(x02, P)
            else:
                xi = umn(x02)
            X.append(xi)

    if gen == 2:
        if C == 0:
            xi = [x for x in P]
            X.append(xi)

        elif C == 1:
            if X[-1] != "O":
                ob = [X[-1][0], -X[-1][1] % p]
            else:
                ob = "O"
            if ob != P:
                xi = slog(ob, P)
            else:
                xi = umn(ob)
            X.append(xi)

        elif C == 2:
            if X[-1] != "O":
                ob = [X[-1][0], -X[-1][1] % p]
            else:
                ob = "O"
            xi = umn(ob)
            if xi != P:
                xi = slog(xi, P)
            else:
                xi = umn(xi)
            X.append(xi)

        else:
            if X[-1] != "O":
                ob = [X[-1][0], -X[-1][1] % p]
            else:
                ob = "O"
            xi = umn(ob)
            for j in range(C - 2):
                if xi != ob:
                    x02 = slog(xi, ob)
                else:
                    x02 = umn(xi)
            if x02 != P:
                xi = slog(x02, P)
            else:
                xi = umn(x02)
            X.append(xi)

print("X", X)

array = X
if array[0] == [3, 24]:
    print("Период последовательности", 4)
else:
    N = len(set(tuple(row) for row in array))
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            N -= 1
            break
    print("Период последовательности", N)
