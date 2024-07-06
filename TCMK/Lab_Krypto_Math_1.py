#Вариант 12
#a=5251 b=4183

a = int(input("1 число = "))
b = int(input("2 число = "))
t1 = a
t2 = b
c = 1
while a!=b:
    if (a % 2 == 0) and (b % 2 == 0):
        c *= 2
        a = a / 2
        b = b / 2
    elif (a % 2 != 0) and (b % 2 == 0):
        b = b / 2

    elif (a % 2 == 0) and (b % 2 != 0):
        a = a / 2

    elif (a % 2 != 0) and (b % 2 != 0) and a>b:
        a = a - b
    else:
        b -= a
    if a == b:
        print(f"НОД ({t1};{t2}) = {int(a*c)}")



