import random
import numpy as np

def gauss_elimination(A, B):
    n = len(A)
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            B[k] -= A[k][i] * x[i]
    return x

def MNK_metod(coefficients, y_values):
    solution = np.linalg.lstsq(coefficients, y_values,None)[0]
    return solution

def podshet(X, K):
    New_X = [list(map(int, x)) for x in X]
    V4 = []
    for i in range(K):
        V4.append(New_X[i])
        #R = random.choice(New_X)
        #New_X.remove(R)
        #V4.append(R)

    b = []
    for i in range(len(V4)):
        b.append(V4[i][-1])
        V4[i].remove(V4[i][-1])

    #print(V4)
    if K == 3:
        print(V4)
        print(b)
        resutl = gauss_elimination(V4, b)
        print(resutl)
        return resutl[0]
    elif K == 5:
        resutl = MNK_metod(V4, b)
        return resutl[0]




# X = []

# for i in range(6):
#     Koef = input(f"Введите коэффициенты для X{i+1}: ")
#     X.append(Koef.split(','))
#
# print(X)

#Вариант 12
X1 = [[['14', '12', '26', '2938'], ['16', '20', '25', '3342'], ['3', '16', '4', '647'], ['11', '24', '16', '2311'], ['21', '28', '29', '4367']],
      [['14', '12', '26', '2924'], ['16', '20', '25', '3326'], ['3', '16', '4', '644'], ['11', '24', '16', '2300'], ['21', '28', '29', '4346']],
      [['14', '12', '26', '2980'], ['16', '20', '25', '3390'], ['3', '16', '4', '656'], ['11', '24', '16', '2344'], ['21', '28', '29', '4430']],
      [['14', '12', '26', '3050'], ['16', '20', '25', '3470'], ['3', '16', '4', '671'], ['11', '24', '16', '2399'], ['21', '28', '29', '4535']],
      [['14', '12', '26', '3246'], ['16', '20', '25', '3694'], ['3', '16', '4', '713'], ['11', '24', '16', '2553'], ['21', '28', '29', '4829']],
      [['14', '12', '26', '2994'], ['16', '20', '25', '3406'], ['3', '16', '4', '659'], ['11', '24', '16', '2355'], ['21', '28', '29', '4451']]]


K = 3
Mass_otv = []
for i in range(6):
    Mass_otv.append(podshet(X1[i], K))

Mass_text = ''
for i in range(len(Mass_otv)):
    Mass_otv[i] = round(Mass_otv[i])

print(Mass_otv)

sicret_bukv = [bytes([num]).decode('cp1251', errors='replace') for num in Mass_otv]

print("".join(sicret_bukv))
