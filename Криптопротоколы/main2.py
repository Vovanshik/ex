import tkinter as tk
import sys
import os


def create_window():
    os.system('python Diff.py')

def kill_newwin():
    os.system('python Diff_2.py')

root = tk.Tk()
root.title("Диффи-Хэлл")
a = tk.Button(root, text="Абонент А", command=create_window)
a.pack()
b = tk.Button(root, text='Абонент B', command=kill_newwin)
b.pack()


root.mainloop()