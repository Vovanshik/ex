import random
import sympy
import tkinter as tk
from tkinter.messagebox import showwarning



def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def miller_rabin_test(p, t):
    b = 0
    m = p - 1
    while m % 2 == 0:
        m //= 2
        b += 1

    for i in range(t):
        a = random.randint(2, p - 1)

        z = pow(a, m, p)
        if z == 1 or z == p - 1:
            continue
        j = 0

        while j < b - 1:
            z = pow(z, 2, p)
            if z == 1:
                return False
            if z == p - 1:
                break
            j += 1
        else:
            if z != p - 1:
                return False
    return True


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


def send_secret():

    with open('n.txt', 'r') as f:
        n = int(f.read())
    f.close()


    with open('second_secret.txt', 'r') as f:
        second_secret = int(f.read())
    f.close()



    chteniye = ""
    with open('Ya.txt','r') as f:
        chteniye = f.read()
    second_shared_key = mod_pow(int(chteniye), second_secret, n)

    with open('secret_all.txt', 'r') as f:
        n = f.read()
    f.close()
    if n == '':
        with open('secret_all.txt', 'w') as f:
            f.write(str(second_shared_key))
        f.close()


    root_powers_text_2.insert(0, second_shared_key)

def clear():
    root_powers_text.delete(0, 'end')
    root_powers_text_2.delete(0, 'end')

def diff_hell():


    with open('n.txt', 'r') as f:
        n = f.read()
    f.close()

    with open('g.txt', 'r') as f:
        g = f.read()
    f.close()

    if n == '' and g == '' and root_powers_text.get() == '':
        n = random.getrandbits(100 - 1) | (1 << (100 - 1)) | 1
        g = find_primitive_root(n)
        second_secret = random.randint(2, n - 2)
        with open('n.txt', 'w') as f:
            f.write(str(n))
        f.close()

        with open('g.txt', 'w') as f:
            f.write(str(g))
        f.close()


    elif root_powers_text.get() != "" and n == '' and g == '':
        n = int(root_powers_text.get())
        if not miller_rabin_test(n, 5):
            showwarning(title="Предупреждение", message="Число не простое...Повторите еще раз")
            return
        g = find_primitive_root(n)
        second_secret = int(Key_text.get())
        with open('n.txt', 'w') as f:
            f.write(str(n))
        f.close()

    elif n != '' and g != '':
        n = int(n)
        g = int(g)
        second_secret = random.randint(2, n - 2)


    with open('second_secret.txt', 'w') as f:
        f.write(str(second_secret))
    f.close()

    n = int(n)
    g = int(g)

    second_public = mod_pow(g, second_secret, n)
    with open('Yb.txt','w') as f:
        f.write(str(second_public))
    f.close()



root2 = tk.Tk()
root2.title("Абонент B")
root2.geometry("500x350")


root_powers_text = tk.Entry()
root_powers_text.place(x=10,y=30, width=488)

root_powers_text_2 = tk.Entry()
root_powers_text_2.place(x=10,y=150, width=488)

Key_text = tk.Entry()
Key_text.place(x=70,y=75, width=80)

enter_text = tk.Label(root2, text="Enter n:", font=("Matura MT Script Capitals", 12))
enter_text.place(x=10,y=1)

enter_text_2 = tk.Label(root2, text="Output:", font=("Matura MT Script Capitals", 12))
enter_text_2.place(x=10,y=120)


label_key = tk.Label(root2, text="Xb:", font=("Matura MT Script Capitals", 12))
label_key.place(x=10,y=70)


code = tk.Button(root2, text="Генерация/Передача данных", command=diff_hell, font=("Helvetica", 12), bg="#CD950C", fg="black")
code.place(x=200,y=200)

Decode = tk.Button(root2, text="Получение ключа",command=send_secret, font=("Helvetica", 12), bg="#CD950C", fg="black")
Decode.place(x=200,y=240)

Clear_btn = tk.Button(root2, text="Очистить",command=clear, font=("Helvetica", 12), bg="#CD950C", fg="black")
Clear_btn.place(x=215,y=280)



root2.mainloop()