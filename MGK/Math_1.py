def normal(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def print_result(polynom):
    polynom_q = ""
    for i in range(len(polynom)):
        if polynom[i] != 0.0 or polynom[i] != 0:
            if i == 0:
                polynom_q += str(round(polynom[i], 1)) + " "
            else:
                polynom_q += str(round(polynom[i], 1)) + "x" + str(i) + " "
    return polynom_q




def calculate(f_x, g_x):
    f_x.reverse()
    g_x.reverse()
    if len(f_x) >= len(g_x):
        x_n = len(f_x) - len(g_x)
        g_x = [0] * x_n + g_x
    else:
        return [0], f_x

    chastn = []
    delitel = float(g_x[-1])
    for i in range(x_n + 1):
        koef_x = f_x[-1] / delitel
        chastn = [koef_x] + chastn

        if koef_x != 0:
            d = [koef_x * i for i in g_x]
            f_x = [i - vich for i, vich in zip(f_x, d)]
        f_x.pop()
        g_x.pop(0)

    normal(f_x)
    return chastn, f_x

def proverka(f_x, g_x):
    q, r = calculate(f_x, g_x)
    print(q)
    print(r)
    print(f"f(x) = ({print_result(g_x)}) * ({print_result(q)}) + ({print_result(r)})")
    return q, r

def main():
    #Вариант 12
    print("Вариант 12")
    f_x = [1, -2, -1, 4, -2]
    g_x = [1, -1, -1, 2, -2]
    proverka(f_x, g_x)

    # На паре
    print("\nНа паре")
    f_x = [2, -3, -1, 2, 1]
    g_x = [1, -3, 3]
    proverka(f_x, g_x)

    # На паре
    print("\nНа паре")
    f_x = [1, -2, 1, 3]
    g_x = [3, -2, -1]
    proverka(f_x, g_x)

    # Вариант 16
    print("\nВариант 16")
    f_x = [1, -1, 1, 0, 1, -1, -1]
    g_x = [1, 0, 1, 0, 1, 0]
    proverka(f_x, g_x)

    # На паре
    print("\nНа паре")
    f_x = [1, 0, 0, 0, 0]
    g_x = [1, 1, -1]
    proverka(f_x, g_x)

    # Вариант 4
    print("\nВариант 4")
    f_x = [1, 0, -3, 1, 2, -2, -3, -1]
    g_x = [1, 0, -3, 0, 1]
    proverka(f_x, g_x)


if __name__ == '__main__':
    main()