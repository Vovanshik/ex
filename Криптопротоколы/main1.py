import tkinter as tk
from tkinter import messagebox
import sys
import os

with open('proverka.txt', 'w') as f:
    f.write('0')
f.close()




def autent():
    os.system('python Authentication.py')

def create_window():
    with open('proverka.txt', 'r') as f:
        n = int(f.read())
    f.close()
    if n == 1:
        os.system('python main2.py')
    else:
        messagebox.showerror("Ошибка!", "Аутентификация не была пройдена!")


def chat():
    with open('proverka.txt', 'r') as f:
        n = int(f.read())
    f.close()
    if n == 1:
        os.system('python Chat.py')
    else:
        messagebox.showerror("Ошибка!", "Аутентификация не была пройдена!")

root = tk.Tk()
a = tk.Button(root, text="Аутентификация", command=autent)
a.pack()
b = tk.Button(root, text='Обмен ключами', command=create_window)
b.pack()
c = tk.Button(root, text='Чат', command=chat)
c.pack()

root.mainloop()