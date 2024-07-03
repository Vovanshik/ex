import tkinter as tk
from tkinter import ttk
import psycopg2
import random
import tkinter.messagebox as mb
import hashlib



conn = psycopg2.connect(user="postgres",
                        password="1234567890",
                        database="Vote",
                        host="localhost",
                        port=5432)
cur = conn.cursor()

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

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


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    return False

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def canonical_decomposition(n):
    if n < 2:
        return [n]

    factors = prime_factors(n)
    unique_factors = set(factors)
    decomposition = []

    for factor in unique_factors:
        count = factors.count(factor)
        if count > 1:
            decomposition.append(factor)
        else:
            decomposition.append(factor)

    return decomposition

def st_phi(second_number,p):
    f = 1
    if NOD(second_number, p) != 1:
        return -1

    if is_prime(p):
        f = p - 1
    else:
        f *= p
        decomposition = canonical_decomposition(int(p))
        for i in decomposition:
            f *= (1 - 1 / int(i))

    second_number **= int(f - 1)
    return second_number % p


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

def generate_primesRSA(N):
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
    return [i for i in primes if (i != 0) and i > 200]

def rsa():
    while True:
        primes = generate_primesRSA(600)
        p = random.choice(primes)
        q = random.choice([x for x in primes if x < p])
        N = p * q
        M = (p - 1) * (q - 1)
        d = 1
        sum = bin(p)[2:] + bin(q)[2:]
        sum = int(sum, 2)
        while d < M:
            if NOD(d, M) == 1 and len(str(d)) == len(str(sum)):
                break
            d += 1

        if d != M:
            break

    e_obr = st_phi(d, M)
    return [d, e_obr, N]

def Q_shet(Q):
    r = 0

    while Q % 2 == 0:
        Q //= 2
        r += 1

    p = 0
    while Q % 3 == 0:
        Q //= 3
        p += 1
    return Q, r, p

def Count_results():

    cur.execute("SELECT * FROM users")
    result = cur.fetchall()

    Q = 1

    with open('n_center.txt', 'r', encoding='utf-8') as file:
        Pole_Center = int(file.read())

    with open('secret_center_key.txt', 'r', encoding='utf-8') as file:
        Cloce_Key = int(file.read())

    for i in result:
        Q *= pow(i[4], Cloce_Key, Pole_Center)
    print(f"Q:  {Q}")
    R, za, pro = Q_shet(Q)
    print(f"R:  {R}")
    All_user_vote = len(result)
    vozd = All_user_vote - (za + pro)

    root4 = tk.Tk()
    root4.title("Подсчет")
    root4.geometry("625x200")
    s = ttk.Style()
    s.theme_use('clam')

    Vivod_text_YES = tk.Label(root4, text="Vote for YES: ", font=("device", 12))
    Vivod_text_YES.place(x=10, y=125)

    Vivod_text_YES_Value = tk.Label(root4, text=str(za), fg="green",font=("device", 12))
    Vivod_text_YES_Value.place(x=110, y=125)

    Vivod_text_NO = tk.Label(root4, text="Vote for NO: ", font=("device", 12))
    Vivod_text_NO.place(x=10, y=145)

    Vivod_text_NO_Value = tk.Label(root4, text=str(pro), fg="red",font=("device", 12))
    Vivod_text_NO_Value.place(x=100, y=145)

    Vivod_text_VOZ = tk.Label(root4, text="Vote for NEUTRAL: ", font=("device", 12))
    Vivod_text_VOZ.place(x=10, y=165)

    Vivod_text_VOZ_Value = tk.Label(root4, text=str(vozd), fg="#7B68EE",font=("device", 12))
    Vivod_text_VOZ_Value.place(x=150, y=165)

    tree = ttk.Treeview(root4, column=("c1", "c2", "c3"), show='headings', height=5)
    tree.column("# 1", anchor='center')
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor='center')
    tree.heading("# 2", text="FIO")
    tree.column("# 3", anchor='center')
    tree.heading("# 3", text="F_i")

    with open('ZA.txt', 'w', encoding='utf-8') as file:
            file.write(str(za))
    with open('PRO.txt', 'w', encoding='utf-8') as file:
            file.write(str(pro))


    for i in result:
        tree.insert('', 'end', text=f"{i[0]}", values=(i[0], i[1], i[4]))

    tree.pack()
    scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")
    root4.mainloop()

def Authentication(FIO, close_key,public_key,n):
    text_poverk = str(calculate_hash("Bob.docx"))

    Sum_hesha = 0

    for i in text_poverk:
        Sum_hesha += int(i, 16)



    n_users = int(n)
    e_users = int(public_key)

    user_ECP = (Sum_hesha ** close_key) % n_users

    server_ECP = str(calculate_hash("Alice.docx"))

    Sum_hesha_Alice = 0

    for i in server_ECP:
        Sum_hesha_Alice += int(i, 16)

    Alice_admit_Bob = (user_ECP ** e_users) % n_users

    if Sum_hesha_Alice == Alice_admit_Bob:
        print(f"подпись подтверждена \n {Sum_hesha_Alice} = {Alice_admit_Bob}")
        return True
    else:
        return False

def Step_1_2():
    Main_Center = rsa()
    with open('open_center_key.txt', 'w', encoding='utf-8') as file:
            file.write(str(Main_Center[0]))
    with open('secret_center_key.txt', 'w', encoding='utf-8') as file:
            file.write(str(Main_Center[1]))
    with open('n_center.txt', 'w', encoding='utf-8') as file:
            file.write(str(Main_Center[2]))

    delete_query = '''TRUNCATE users;'''
    cur.execute(delete_query)
    alter_query = '''ALTER SEQUENCE users_id_seq RESTART WITH 1;'''
    cur.execute(alter_query)

    Mass_Fam = []
    Mass_Vote = []





    def Vvod():
        Fam = FIO.get()
        if Fam in Mass_Fam:
            mb.showerror("Error", "Такой человек уже проголосовал!")
            FIO.delete(0, 'end')
        else:
            Mass_Fam.append(Fam)
            User_vote = random.choice([2, 3, 1])
            Mass_Vote.append(User_vote)
            # Каждый избиратель создает ключи RSA
            Vote_Rsa = rsa()
            Close_Vote = Vote_Rsa[0]
            Open_Vote = Vote_Rsa[1]
            Pole_Vote = Vote_Rsa[2]
            with open('n_center.txt', 'r', encoding='utf-8') as file:
                Pole_Center = int(file.read())

            with open('open_center_key.txt', 'r', encoding='utf-8') as file:
                Open_Key = int(file.read())

            with open('secret_center_key.txt', 'r', encoding='utf-8') as file:
                Cloce_Key = int(file.read())

            # Затемнение
            while True:
                simple_value = generate_primes(200)
                user_simple_value = random.choice(simple_value)
                if user_simple_value < Pole_Center:
                    break

            t_i = User_vote * user_simple_value
            f_i = (t_i ** Open_Key) % Pole_Center
            if Authentication(Fam,Close_Vote,Open_Vote,Pole_Vote):
                insert_query = '''INSERT INTO users (fami, open_key_e, open_key_n, f_i,R) VALUES (%s,%s,%s,%s,%s);'''
                data = (Fam, Open_Vote, Pole_Vote, f_i, user_simple_value)
                cur.execute(insert_query, data)
                conn.commit()
                FIO.delete(0, 'end')
                print(Mass_Vote)
            else:
                mb.showerror("Error", "Такой человек не прошел проверку!")
                FIO.delete(0, 'end')





    root3 = tk.Tk()
    root3.title("Выборы")
    root3.geometry("300x100")

    FIO = tk.Entry(root3)
    FIO.place(x=10, y=30, width=100)

    enter_text = tk.Label(root3, text="Enter Initials ", font=("Matura MT Script Capitals", 12))
    enter_text.place(x=10, y=1)

    print_message = tk.Label(root3, text="*Голосовать не нужно\nМы это сделаем за вас! ", font=("system", 6))
    print_message.place(x=120, y=30)

    Control_btn = tk.Button(root3, text="(O_O)", command=Vvod, font=("Helvetica", 12), bg="#CD950C", fg="black")
    Control_btn.place(x=10, y=60)

    root3.mainloop()
    return

def proverka_vote():

    with open('ZA.txt', 'r', encoding='utf-8') as file:
        Vote_ZA = int(file.read())

    with open('PRO.txt', 'r', encoding='utf-8') as file:
        Vote_PRO = int(file.read())



    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    with open('n_center.txt', 'r', encoding='utf-8') as file:
        Pole_Center = int(file.read())

    with open('open_center_key.txt', 'r', encoding='utf-8') as file:
        Open_Key = int(file.read())

    #Восстанавливаем Q
    R = 1
    for i in result:
        R *= i[5]

    F = 1
    for i in result:
        F *= i[4]

    New_Q = (2**Vote_ZA)*(3**Vote_PRO) * R
    Shifr_New_Q = pow(New_Q, Open_Key, Pole_Center)
    if Shifr_New_Q == (F % Pole_Center):
        mb.showinfo("Success", f"R = {R} \nF = {F}\nQ = {Shifr_New_Q}\n {Shifr_New_Q} = {F % Pole_Center}")
        mb.showinfo("Success", f"Упешно проверено голосование")
        print("Урааа")
    else:
        mb.showinfo("LOSE", f"R = {R} \nF = {F}\nQ = {Shifr_New_Q}\n {Shifr_New_Q} != {F % Pole_Center}")
        mb.showinfo("LOSE", f"Голосование провалено")


root2 = tk.Tk()
root2.title("Абонент А")
root2.geometry("500x200")

code = tk.Button(root2, text="Голосование", command=Step_1_2, font=("Helvetica", 12), bg="#CD950C", fg="black")
code.place(x=200, y=10)

Decode = tk.Button(root2, text="Подсчет результата", command=Count_results, font=("Helvetica", 12), bg="#CD950C", fg="black")
Decode.place(x=173, y=50)

Control_btn = tk.Button(root2, text="Контроль", command=proverka_vote, font=("Helvetica", 12), bg="#CD950C", fg="black")
Control_btn.place(x=214, y=90)


root2.mainloop()
