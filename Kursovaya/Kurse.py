import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import psycopg2
import hashlib
import tkinter.messagebox as mb

conn = psycopg2.connect(user="postgres",
                        password="1234567890",
                        database="Kurs_4",
                        host="localhost",
                        port=5432)
cur = conn.cursor()



class GraphicalPasswordApp:
    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.current_image_index = 0
        self.selected_parts = set()
        self.passwords = {}  # Словарь для хранения паролей для каждой картинки

        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_left_click)


        self.submit_button = tk.Button(master, text="Подтвердить", command=self.change_image)
        self.submit_button.pack()


        self.password_button = tk.Button(master, text="Создать пароль", command=self.create_password)
        self.password_button.pack()

        self.password = ""

    def load_image(self):
        if self.current_image_index < len(self.images):
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((400, 300))
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            # Рисование сетки
            for i in range(1, 4):
                self.canvas.create_line(0, i * 100, 400, i * 100, fill="gray")
            for i in range(1, 5):
                self.canvas.create_line(i * 100, 0, i * 100, 300, fill="gray")
        else:
            self.save_passwords()
            self.master.destroy()

    def change_image(self):
        self.current_image_index += 1
        self.canvas.delete("all")
        self.load_image()

    def on_left_click(self, event):
        row = event.y // 100
        column = event.x // 100
        part = (int(row), int(column))

        if part in self.selected_parts:
            self.selected_parts.remove(part)
            self.canvas.itemconfig("part{}".format(part), outline="")
        else:
            self.selected_parts.add(part)
            self.canvas.itemconfig("part{}".format(part), outline="red")

    def create_password(self):
        self.password = ""
        for part in self.selected_parts:
            self.password += str(part[0]) + str(part[1])

        self.passwords[self.current_image_index] = self.password

    def save_passwords(self):
        Stroka = ''
        for image_index, password in self.passwords.items():
            Stroka += image_index + password
        insert_query = '''INSERT INTO log_user (log,password,secret_key) VALUES (%s,%s,%s);'''
        with open("login.txt", "r") as f:
            login = f.read()

        with open("secret.txt", "r") as f:
            secret = f.read()

        Stroka, secret = hashlib.sha256(Stroka.encode('UTF-8')).hexdigest(), hashlib.sha256(secret.encode('UTF-8')).hexdigest()

        data = (login, Stroka, secret)
        cur.execute(insert_query, data)
        conn.commit()

class GraphicalPasswordAppLogin:
    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.current_image_index = 0
        self.selected_parts = set()
        self.passwords = {}  # Словарь для хранения паролей для каждой картинки

        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_left_click)

        # Кнопка для смены изображения
        self.submit_button = tk.Button(master, text="Подтвердить", command=self.change_image)
        self.submit_button.pack()

        # Кнопка для создания пароля
        self.password_button = tk.Button(master, text="Создать пароль", command=self.create_password)
        self.password_button.pack()

        self.password = ""

    def load_image(self):
        if self.current_image_index < len(self.images):
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((400, 300))
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            # Рисование сетки
            for i in range(1, 4):
                self.canvas.create_line(0, i * 100, 400, i * 100, fill="gray")
            for i in range(1, 5):
                self.canvas.create_line(i * 100, 0, i * 100, 300, fill="gray")
        else:
            self.save_passwords()
            self.master.destroy()

    def change_image(self):
        self.current_image_index += 1
        self.canvas.delete("all")
        self.load_image()

    def on_left_click(self, event):
        row = event.y // 100
        column = event.x // 100
        part = (int(row), int(column))

        if part in self.selected_parts:
            self.selected_parts.remove(part)
            self.canvas.itemconfig("part{}".format(part), outline="")
        else:
            self.selected_parts.add(part)
            self.canvas.itemconfig("part{}".format(part), outline="red")

    def create_password(self):
        self.password = ""
        for part in self.selected_parts:
            self.password += str(part[0]) + str(part[1])

        self.passwords[self.current_image_index] = self.password

    def save_passwords(self):
        Stroka = ''
        for image_index, password in self.passwords.items():
            Stroka += image_index + password

        Stroka = hashlib.sha256(Stroka.encode('UTF-8')).hexdigest()

        with open("login.txt", "r") as f:
            login = f.read()

        cur.execute(f"SELECT password FROM log_user WHERE log = '{login}'")
        result = cur.fetchone()
        if Stroka == result[0]:
            mb.showinfo("Успех", "Вход выполнен")




import hashlib

def image_for_password():
    root = tk.Toplevel()
    root.title("Graphical Password")

    images = ["1.jpg", "2.jpg", "3.jpg"]

    app = GraphicalPasswordApp(root, images)

    root.mainloop()


def image_for_password2():
    root = tk.Toplevel()
    root.title("Graphical Password")

    images = ["1.jpg", "2.jpg", "3.jpg"]

    app = GraphicalPasswordAppLogin(root, images)

    root.mainloop()

def registration():

    def complete():
        login = root_powers_text.get()
        with open("login.txt", "w") as f:
            f.write(f"{login}")

        secret = root_powers_text_2.get()
        with open("secret.txt", "w") as f:
            f.write(f"{secret}")

        root3.destroy()
        image_for_password()

    root3 = tk.Tk()
    root3.geometry("500x350")

    root_powers_text = tk.Entry(root3)
    root_powers_text.place(x=10, y=30, width=488)

    root_powers_text_2 = tk.Entry(root3)
    root_powers_text_2.place(x=10, y=150, width=488)

    Key_text = tk.Entry(root3)
    Key_text.place(x=70, y=75, width=80)

    enter_text = tk.Label(root3, text="Придумайте логин:", font=("Matura MT Script Capitals", 12))
    enter_text.place(x=10, y=1)

    label_key = tk.Label(root3, text="Введите секретное слово:", font=("Matura MT Script Capitals", 12))
    label_key.place(x=10, y=70)

    code = tk.Button(root3, text="Подтвердить", command=complete, font=("Helvetica", 12), bg="#CD950C",
                     fg="black")
    code.place(x=200, y=200)

    root3.mainloop()


def registration2(login):

    def complete():
        with open("login.txt", "w") as f:
            f.write(f"{login}")

        secret = root_powers_text_2.get()
        with open("secret.txt", "w") as f:
            f.write(f"{secret}")

        root3.destroy()
        image_for_password()

    root3 = tk.Tk()
    root3.geometry("500x350")


    root_powers_text_2 = tk.Entry(root3)
    root_powers_text_2.place(x=10, y=150, width=488)

    Key_text = tk.Entry(root3)
    Key_text.place(x=70, y=75, width=80)


    label_key = tk.Label(root3, text="ЫЫЫВведите секретное слово:", font=("Matura MT Script Capitals", 12))
    label_key.place(x=10, y=70)

    code = tk.Button(root3, text="Подтвердить", command=complete, font=("Helvetica", 12), bg="#CD950C",
                     fg="black")
    code.place(x=200, y=200)

    root3.mainloop()


def login():

    def complete():
        log = root_powers_text.get()
        with open("login.txt", "w") as f:
            f.write(f"{log}")

        root4.destroy()
        image_for_password2()

    root4 = tk.Tk()
    root4.geometry("300x100")

    root_powers_text = tk.Entry(root4)
    root_powers_text.place(x=10, y=30, width=100)

    enter_text = tk.Label(root4, text="Введите логин:", font=("Matura MT Script Capitals", 12))
    enter_text.place(x=10, y=1)

    log_btn = tk.Button(root4, text="Войти", command=complete, font=("Helvetica", 12), bg="#CD950C", fg="black")
    log_btn.place(x=200, y=10)

def forget_pswd():


    def vosstanovleniye():
        Name = root_powers_text.get()
        Secret = hashlib.sha256(root_powers_text_2.get().encode('UTF-8')).hexdigest()
        if Name == "" or Secret == "":
            messagebox.showerror("Ошибка!", "Поле логин/секретное слово не должны быть пустыми.")
            return
        cur.execute(f"SELECT secret_key FROM log_user WHERE log = '{Name}'")
        result = cur.fetchone()
        if result != None and Secret == result[0]:
            cur.execute(f"DELETE FROM log_user WHERE log = '{Name}'")
            registration2(Name)
        else:
            messagebox.showerror("Ошибка!", "Неправильный логин/секретное слово.")



    root5 = tk.Tk()
    root5.title("Восстановление")
    root5.geometry("300x300")

    root_powers_text = tk.Entry(root5)
    root_powers_text.place(x=10, y=30, width=250)

    root_powers_text_2 = tk.Entry(root5)
    root_powers_text_2.place(x=10, y=150, width=250)

    Key_text = tk.Entry(root5)
    Key_text.place(x=70, y=75, width=80)

    enter_text = tk.Label(root5, text="Введите логин:", font=("Matura MT Script Capitals", 12))
    enter_text.place(x=10, y=1)

    label_key = tk.Label(root5, text="Введите секретное слово:", font=("Matura MT Script Capitals", 12))
    label_key.place(x=10, y=70)

    code = tk.Button(root5, text="Подтвердить",command=vosstanovleniye, font=("Helvetica", 12), bg="#CD950C",
                     fg="black")
    code.place(x=85, y=200)

    root5.mainloop()



root2 = tk.Tk()
root2.title("Курсовая")
root2.geometry("500x200")

code = tk.Button(root2, text="Регистрация", command=registration, font=("Helvetica", 12), bg="#CD950C", fg="black")
code.place(x=200, y=10)

Decode = tk.Button(root2, text="Вход", command=login, font=("Helvetica", 12), bg="#CD950C", fg="black")
Decode.place(x=225, y=50)

Control_btn = tk.Button(root2, text="Забыли пароль?", command=forget_pswd, font=("Helvetica", 12), bg="#CD950C", fg="black")
Control_btn.place(x=188, y=90)

root2.mainloop()