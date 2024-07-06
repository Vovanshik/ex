from prettytable import PrettyTable,ALL
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

while True:
    a = int(input("a = "))
    b = int(input("b = "))
    m = int(input("m = "))
    if b % NOD(a,m) == 0:
        break
    else:
        print(f"{b} не делится на НОД({a}, {m}) = {NOD(a,m)}")

a_old = a
b_old = b
m_old = m

print(f'{a}x ≡ {b} mod {m}')

print(f"ax - my = b")
print(f"{a}x - {m}y={b}")


print(f'НОД({a}, {m}) = {NOD(a,m)}')
d = int(NOD(a, m))
if NOD(a, m) > 1:
    a = int(a / d)
    b = int(b / d)
    m = int(m / d)
    print(f"{a}x - {m}y={b}")

Mass_delit = []
delitel = m
delimoe = a
while True:
    Mass_delit.append(delimoe // delitel)
    delimoe = delimoe % delitel
    if delimoe == 1:
        Mass_delit.append(delitel)
        break
    n = delimoe
    delimoe = delitel
    delitel = n

print(f"{a}/{m} = {Mass_delit}")

k = [i for i in range(-1, len(Mass_delit))]
ak = [x for x in Mass_delit]
ak.insert(0, "")
Pk = [1, ak[1]]
Qk = [0, 1]

for i in range(len(k) - 2):
    Pk.append(ak[i + 2]*Pk[-1] + Pk[-2])
    Qk.append(ak[i + 2]*Qk[-1] + Qk[-2])

k.insert(0, "k")
ak.insert(0, "ak")
Pk.insert(0, "Pk")
Qk.insert(0, "Qk")
mytable = PrettyTable()
mytable.hrules=ALL
mytable.field_names = k
mytable.add_rows([ak, Pk, Qk])
print(mytable)

ex1 = (-1) **(k[-1]-1)
ex2 = b_old / NOD(a_old, m_old)
ex3 = Qk[-2]
x0 =(ex1*ex2*ex3) % (m_old)
Mass_x = [x0]

if NOD(a_old,m_old) > 1:
    print(f"x0 = {int(x0)}")
    for i in range(int(NOD(a_old, m_old))-1):
        x_i = (int(Mass_x[0] + (i+1)*(m_old / NOD(a_old, m_old))))
        print(f"x{i+1} = {x_i}")

        Mass_x.append(int(x_i))
else:
    print(f"x = {int(x0)}")






