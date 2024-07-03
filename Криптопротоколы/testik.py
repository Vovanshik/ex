import tkinter as tk
from tkinter import ttk
import psycopg2
import random
import tkinter.messagebox as mb
import hashlib
import sympy


def is_primitive_root(a, n):
    phi = sympy.totient(n)
    phi = int(str(phi))
    factors = sympy.factorint(phi)
    for factor in factors:
        if pow(a, phi // factor, n) == 1:
            return False
    return True


def find_primitive_root(n):
    for a in range(2, n):
        if is_primitive_root(a, n):
            return a
    return None


def generate_primes(N):
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1
    return [i for i in primes if (i != 0) and i > 100]


def general():
    primes = generate_primes(1000)
    while True:
        p = random.choice(primes[3:])
        q = random.choice([x for x in primes if x < p])
        if (p - 1) % q == 0:
            break
    while True:
        a = random.randint(2, p - 2)
        if pow(a, q, p) == 1:
            break

    x = random.randint(1, q - 1)
    y = pow(a, x, p)

    return p, q, a, x, y

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_A():

    def autentif_user_1():
        p, q, a, Close_Key, Open_Key = general()
        while True:
            k = random.randint(1, q - 1)
            r = pow(a, k, p) % q
            if r != 0:
                break
        hesh_message = str(calculate_hash("Alice.docx"))
        Sum_hesha = 0

        for i in hesh_message:
            Sum_hesha += int(i, 16)
        if Sum_hesha % q == 0:
            Sum_hesha = 1


        s = (Close_Key * r + k * Sum_hesha) % q

        autenti = f"{str(s)}+{str(r)}"
        Open = f"{str(a)}+{str(p)}|{str(q)}+{str(Open_Key)}"

        with open('ecp_user_1.txt', 'w') as f:
            f.write(autenti)
        f.close()

        with open('open_key_A.txt', 'w') as f:
            f.write(Open)
        f.close()

    autentif_user_1()



    return


def check_B():
    def autentif_user_2():
        p, q, a, Close_Key, Open_Key = general()
        while True:
            k = random.randint(1, q - 1)
            r = pow(a, k, p) % q
            if r != 0:
                break

        hesh_message = str(calculate_hash("Bob.docx"))
        Sum_hesha = 0

        for i in hesh_message:
            Sum_hesha += int(i, 16)
        if Sum_hesha % q == 0:
            Sum_hesha = 1

        s = (Close_Key * r + k * Sum_hesha) % q

        autenti = f"{str(s)}+{str(r)}"
        Open = f"{str(a)}+{str(p)}|{str(q)}+{str(Open_Key)}"

        with open('ecp_user_2.txt', 'w') as f:
            f.write(autenti)
        f.close()

        with open('open_key_B.txt', 'w') as f:
            f.write(Open)
        f.close()

    autentif_user_2()

    return


def registr():
    def autentifs_user_1():

        with open('ecp_user_1.txt', 'r') as f:
            n = f.read()
        f.close()

        with open('open_key_A.txt', 'r') as f:
            l = f.read()
        f.close()

        cherta = l.index("|")

        polovinka1 = l[:cherta]
        polovinka2 = l[cherta + 1:]

        plus_i_1 = polovinka1.index("+")
        plus_i_2 = polovinka2.index("+")

        a = int(polovinka1[:plus_i_1])
        p = int(polovinka1[plus_i_1 + 1:])

        q = int(polovinka2[:plus_i_2])
        Open_Key = int(polovinka2[plus_i_2 + 1:])

        plus_i = n.index("+")
        s = int(n[:plus_i])
        r = int(n[plus_i + 1:])

        Send_mess = [r, s]
        # print(f"Пользователь Aлиса отправляет Бобу цифровую подпись r и s: \nr = {r} \ns = {s}")

        hesh_Alice = str(calculate_hash("Send_A.docx"))
        # print(f"Хэш переданного документа: {hesh_Alice}")
        Sum_hesha_Alice = 0
        for i in hesh_Alice:
            Sum_hesha_Alice += int(i, 16)
        if Sum_hesha_Alice % q == 0:
            Sum_hesha_Alice = 1

        v = pow(Sum_hesha_Alice, q - 2, q)
        z1 = (Send_mess[1] * v) % q
        z2 = ((q - Send_mess[0]) * v) % q

        u = (((a ** z1) * (Open_Key ** z2)) % p) % q

        # print(f"Пользователь Боб начал проверку подписи:"
        # f"\nv = {v} \nz1={z1}\nz2={z2}\nu={u}")

        if u == Send_mess[0]:
            # print(f"Боб проверил подпись и она подлинна\nu = r` ({u} = {r})")
            return 1
        else:
            # print(f"Документ был изменен и подпись неподтверждена u != r` ({u} != {r})")
            return 0

    def autentifs_user_2():

        with open('ecp_user_2.txt', 'r') as f:
            n = f.read()
        f.close()

        with open('open_key_B.txt', 'r') as f:
            s = f.read()
        f.close()

        cherta = s.index("|")

        polovinka1 = s[:cherta]
        polovinka2 = s[cherta + 1:]

        plus_i_1 = polovinka1.index("+")
        plus_i_2 = polovinka2.index("+")

        a = int(polovinka1[:plus_i_1])
        p = int(polovinka1[plus_i_1 + 1:])

        q = int(polovinka2[:plus_i_2])
        Open_Key = int(polovinka2[plus_i_2 + 1:])

        plus_i = n.index("+")
        r = int(n[:plus_i])
        s = int(n[plus_i + 1:])

        Send_mess = [r, s]
        # print(f"Пользователь Aлиса отправляет Бобу цифровую подпись r и s: \nr = {r} \ns = {s}")

        hesh_Alice = str(calculate_hash("Send_B.docx"))
        # print(f"Хэш переданного документа: {hesh_Alice}")
        Sum_hesha_Alice = 0
        for i in hesh_Alice:
            Sum_hesha_Alice += int(i, 16)
        if Sum_hesha_Alice % q == 0:
            Sum_hesha_Alice = 1

        v = pow(Sum_hesha_Alice, q - 2, q)
        z1 = (Send_mess[1] * v) % q
        z2 = ((q - Send_mess[0]) * v) % q

        u = (((a ** z1) * (Open_Key ** z2)) % p) % q

        # print(f"Пользователь Боб начал проверку подписи:"
        # f"\nv = {v} \nz1={z1}\nz2={z2}\nu={u}")

        if u == Send_mess[0]:
            # print(f"Боб проверил подпись и она подлинна\nu = r` ({u} = {r})")
            return 1
        else:
            # print(f"Документ был изменен и подпись неподтверждена u != r` ({u} != {r})")
            return 0


    A = autentifs_user_1()
    B = autentifs_user_2()

    if A == 1 and B == 1:
        mb.showinfo("Success", "Аутентификация юзеров подтверждена")
        with open('proverka.txt', 'w') as f:
            f.write('1')
        f.close()

    else:
        mb.showerror("Error", "Аутентификация провалена")
        with open('proverka.txt', 'w') as f:
            f.write('0')
        f.close()
    return


check_A()
registr()