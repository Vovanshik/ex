import random

print("Выберите по какому варианту считать: ")
print("1 - С вводом варианта по списку\n2 - С вводом готовых значений")
Choose = int(input("Ваш выбор: "))

if Choose == 1:
    vibory = [17, 19, 23, 29, 31]
    Variant = int(input("Введите ваш вариант: "))
    p = vibory[Variant % 5]
    a = 1 + (Variant % p)
    XY = input("Введите точку:")
    Pozition = XY.index(',')
    Point = [int(XY[1:Pozition]), int(XY[Pozition + 1:-1])]


elif Choose == 2:
    p = int(input("Введите p: "))
    while True:
        a = int(input("Введите a: "))
        if a >= p:
            print(f"Ошибка a > p | {a} > {p}")
        else:
            break
    XY = input("Введите точку:")
    Pozition = XY.index(',')
    Point = [int(XY[1:Pozition]), int(XY[Pozition+1:-1])]


else:
    print("Такого выбора нет....")
    exit()


b = (Point[1]**2 - (Point[0]**3 + a*Point[0]))

if (4*(a**3) + 27*(b**2)) % p != 0 and b >0:
    print("Кривая найдена")
    print(f"Задается уравнением : y^2 = x^3 + {a}x + {b} mod {p}")
else:
    print("Кривая не найдена")