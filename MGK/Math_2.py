def normal(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)

def peremnosh(s1,s2):
    res = [0] * (len(s1) + len(s2) - 1)
    for o1, i1 in enumerate(s1):
        for o2, i2 in enumerate(s2):
            res[o1 + o2] += i1 * i2

    return res

def print_result(polynom):
    polynom_q = ""
    for i in range(len(polynom)):
        if polynom[i] != 0.0 or polynom[i] != 0:
            if i == 0:
                polynom_q += str(int(round(polynom[i], 1))) + " "
            else:
                polynom_q += str(int(round(polynom[i], 1))) + "x" + str(i) + " "


    return polynom_q




def calculate(f_x, g_x):
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
    chastn, r = calculate(f_x, g_x)
    Mass_Chastn=[]
    Mass_Ost = []
    Mass_Ost.append(r)
    Mass_Chastn.append(chastn)
    while r:
        chastise, r_1 = calculate(g_x, r)
        if len(r_1) != 1 and r_1[0] != 0:
            Mass_Ost.append(r_1)

        elif len(r_1) == 1 and r_1[0] != 0:
            Mass_Ost.append(r_1)

        Mass_Chastn.append(chastise)
        g_x = r
        r = r_1
        if len(r_1) == 1 and r_1[0] == 0:
            break

    print("\nОстатки:")
    #print(Mass_Ost)
    for i in range(len(Mass_Ost)):
        print(f"ч{i+1} = {print_result(Mass_Ost[i])}")

    print("\nЧастные:")
    #print(Mass_Chastn)

    for i in range(len(Mass_Chastn)):
        print(f"q{i + 1} = {print_result(Mass_Chastn[i])}")

    print("\n")

    if len(Mass_Ost) == 1:
        print("Это первая формула")
        print("f+(-q1)g")
        new_list = [i*(-1) for i in Mass_Chastn[0]]
        print(f"{print_result(Mass_Ost[0])}=1F+{print_result(new_list)}g")

    if len(Mass_Ost) == 2:
        print("Это вторая формула")
        print("(-q2)f+(1+q1q2)g")
        new_list = [i * (-1) for i in Mass_Chastn[1]]
        Sp = peremnosh(Mass_Chastn[0], Mass_Chastn[1])
        Sp[0] += 1
        print(f"{print_result(Mass_Ost[1])}=({print_result(new_list)})F+({print_result(Sp)})g")


    if len(Mass_Ost) == 3:
        print("Это третья формула")
        print("(1+q2q3)+(-q1-q3-q3q1-q2q3q4)g")
        new_list = [i * (-1) for i in Mass_Chastn[0]]

        if len(new_list)>len(Mass_Chastn[2]):
            Mass_Chastn = Mass_Chastn + [0]*(len(new_list)-len(Mass_Chastn))
        else:
            new_list = new_list + [0]*(len(Mass_Chastn)-len(new_list))


        minus_q1_q3 = [i - vich for i, vich in zip(new_list, Mass_Chastn[2])]
        q1q2 = peremnosh(Mass_Chastn[0],Mass_Chastn[1])
        q1q2q3 = peremnosh(q1q2, Mass_Chastn[2])

        if len(q1q2q3)>len(minus_q1_q3):
            minus_q1_q3 = minus_q1_q3 + [0]*(len(q1q2q3)-len(minus_q1_q3))
        else:
            q1q2q3 = q1q2q3 + [0]*(len(minus_q1_q3)-len(q1q2q3))

        itog_minus_q1_q3 = [i - vich for i, vich in zip(minus_q1_q3,q1q2q3)]

        q2q3 = peremnosh(Mass_Chastn[1],Mass_Chastn[2])
        q2q3[0]+=1
        print(f"{print_result(Mass_Ost[2])}=({print_result(q2q3)})F+({print_result(itog_minus_q1_q3)})g")


    if len(Mass_Ost) == 4:
        print("Это четвертая формула")
        print("(-q2-q4-q2q3q4)f+(1+q1q2+q1q4+q3q4+q1q2q3q4)g")
        q2q3 = peremnosh(Mass_Chastn[1], Mass_Chastn[2])
        q2q3q4 = peremnosh(q2q3, Mass_Chastn[3])

        q1q2 = peremnosh(Mass_Chastn[0], Mass_Chastn[1])

        q1q4 = peremnosh(Mass_Chastn[0], Mass_Chastn[1])

        q3q4 = peremnosh(Mass_Chastn[2], Mass_Chastn[3])

        q1q2q3q4 = peremnosh(q1q2, q3q4)

        minus_q2 = [i * (-1) for i in Mass_Chastn[1]]

        if len(minus_q2) > len(Mass_Chastn[3]):
            Mass_Chastn[3] = Mass_Chastn[3] + [0]*(len(minus_q2)-len(Mass_Chastn[3]))
        else:
            minus_q2 = minus_q2 + [0]*(len(Mass_Chastn[3])-len(minus_q2))

        minus_q2_q4 = [i - vich for i, vich in zip(minus_q2, Mass_Chastn[3])]

        if len(q2q3q4)>len(minus_q2_q4):
            minus_q2_q4 = minus_q2_q4 + [0]*(len(q2q3q4)-len(minus_q2_q4))
        else:
            q2q3q4 = q2q3q4 + [0]*(len(minus_q2_q4)-len(q2q3q4))

        minus_q2q3q4 = [i - vich for i, vich in zip(minus_q2_q4, q2q3q4)]

        if len(q1q2)>len(q1q4):
            q1q4 = q1q4 + [0]*(len(q1q2)-len(q1q4))
        else:
            q1q2 = q1q2 + [0]*(len(q1q4)-len(q1q2))


        plus_q1q2_q1q4 = [i + vich for i, vich in zip(q1q2, q1q4)]


        if len(plus_q1q2_q1q4)>len(q3q4):
            q3q4 = q3q4 + [0]*(len(plus_q1q2_q1q4)-len(q3q4))
        else:
            plus_q1q2_q1q4 = plus_q1q2_q1q4 + [0]*(len(q3q4)-len(plus_q1q2_q1q4))

        plus_q3q4 = [i + vich for i, vich in zip(plus_q1q2_q1q4, q3q4)]

        if len(q1q2q3q4)>len(plus_q3q4):
            plus_q3q4 = plus_q3q4 + [0]*(len(q1q2q3q4)-len(plus_q3q4))
        else:
            q1q2q3q4 = q1q2q3q4 + [0]*(len(plus_q3q4)-len(q1q2q3q4))

        plus_all = [i + vich for i, vich in zip(q1q2q3q4, plus_q3q4)]
        plus_all[0] +=1

        print(f"{print_result(Mass_Ost[3])}=({print_result(minus_q2q3q4)})F+({print_result(plus_all)})g")

    return r

def main():
    #Вариант 12
    f_x = [0, 6, 12, 14, 11, 5, 1]
    g_x = [3, 9, 13, 11, 5, 1]
    proverka(f_x, g_x)

    f_x = [1, 2, -1, -4, -2]
    g_x = [1, 1, -1, -2, -2]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)


    f_x = [1, -2, -4, 6, 1]
    g_x = [1, 0, -5, -3]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)

    f_x = [1, 0, -3, -1, 2, 2, -3, 1]
    g_x = [1, 0, -3, 0, 1]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)

    #Вариант 12

    print("Вариант 12")

    f_x = [1, -2, 0, 4, -4]
    g_x = [1, -1, -1, 2, -2]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)

    #Вариант 18

    print('Вариант 18')

    f_x = [3, 6, -3, 4, 14, -6, -4, 4]
    g_x = [3, 0, -3, 7, 0, -6, 2]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)


    print("Вариант 20")

    f_x = [1, -4, 11, -27, 37, -35, 35]
    g_x = [1, -3, 7, -20, 10, -25]
    f_x.reverse()
    g_x.reverse()
    proverka(f_x, g_x)




if __name__ == '__main__':
    main()