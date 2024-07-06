import sympy
from tabulate import tabulate

print("ax ≡ b(mod m)")

pr = True
while pr:
    a = int(input("a = "))
    b = int(input("b = "))
    m = int(input("m = "))
    d = sympy.gcd(a, m)
    if d > 0 and b % d == 0:
        pr = False
    else:
        print("НОД(a, m) ≯ 0 или b не делится на НОД(a, m)")
a_old = a
b_old = b
m_old = m

print(f"НОД({a}, {m}) =", d)
if d != 1:
    a = int(a / d)
    b = int(b / d)
    m = int(m / d)
    print(f"a = {a}, b = {b}, m = {m}")

nep_dr = []
delimoe = a
delitel = m
pr = True
while pr:
    nep_dr.append(delimoe // delitel)
    delimoe = delimoe % delitel
    if delimoe == 1:
        nep_dr.append(delitel)
        pr = False
    n = delimoe
    delimoe = delitel
    delitel = n
print(f"{a}/{m} = {nep_dr}")

k = [x for x in range(-1, len(nep_dr))]
ak = [x for x in nep_dr]
ak.insert(0, "")
Pk = [1, ak[1]]
Qk = [0, 1]
for i in range(len(k) - 2):
    Pk.append(ak[i + 2] * Pk[-1] + Pk[-2])
    Qk.append(ak[i + 2] * Qk[-1] + Qk[-2])

k.insert(0, "k")
ak.insert(0, "ak")
Pk.insert(0, "Pk")
Qk.insert(0, "Qk")
print(tabulate([k, ak, Pk, Qk]))

x = (pow(-1, (len(k) - 3 - 1)) * (b_old / d) * Qk[-2]) % m_old
print("x =", x)
