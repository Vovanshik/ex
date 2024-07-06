from prettytable import PrettyTable
import math

def g_x(x):
    return (x**2 + 5)

n = 1359331
#n = 8051
x = 2
y = x
d = 1

mytable = PrettyTable()
mytable.field_names = ["i", "x", "y", "gcd(|x-y|,n)"]
i = 1
while d == 1:
    print(f"i = {i}")
    print(f"x = ({x}^2 + 5 mod {n} = {g_x(x)} mod {n} = {g_x(x) % n}")
    x = g_x(x) % n

    print(f"y = f({y}^2 + 5 mod {n}) = f({g_x(y)} mod n) = {g_x(g_x(y) % n)} mod n = {g_x(g_x(y) % n) % n}")
    y = g_x(g_x(y) % n) % n
    print(f"d = NOD(|{x-y}|,{n}) = {math.gcd(abs(x-y), n)}")
    d = math.gcd(abs(x-y), n)
    mytable.add_row([i, x, y, d])
    i+=1
    print("\n\n")


print(mytable)


