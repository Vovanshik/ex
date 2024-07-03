import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class GraphicalPasswordApp:
    def __init__(self, master, image_path, rows, columns):
        self.master = master
        self.image_path = image_path
        self.rows = rows
        self.columns = columns
        self.selected_parts = set()

        self.canvas = tk.Canvas(master, width=columns*100, height=rows*100)
        self.canvas.pack()

        self.load_image()
        self.canvas.bind("<Button-1>", self.on_click)

    def load_image(self):
        image = Image.open(self.image_path)
        image = image.resize((self.columns * 100, self.rows * 100))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        for i in range(1, self.rows):
            self.canvas.create_line(0, i * 100, self.columns * 100, i * 100, fill="gray")
        for i in range(1, self.columns):
            self.canvas.create_line(i * 100, 0, i * 100, self.rows * 100, fill="gray")

    def on_click(self, event):
        row = event.y // 100
        column = event.x // 100
        part = (int(row), int(column))

        if part in self.selected_parts:
            self.selected_parts.remove(part)
            self.canvas.itemconfig("part{}".format(part), outline="")
        else:
            self.selected_parts.add(part)
            self.canvas.itemconfig("part{}".format(part), outline="red")

    def get_password(self):
        password = ""
        for part in self.selected_parts:
            password += str(part[0]) + str(part[1])
        return password

    def on_left_click(self, event):
        row = event.y // 100
        column = event.x // 100
        part = (int(row), int(column))

        if part in self.selected_parts:
            self.selected_parts.remove(part)
            self.canvas.delete("highlight-{}-{}".format(part[0], part[1]))
        else:
            self.selected_parts.add(part)
            x0 = column * 100
            y0 = row * 100
            x1 = x0 + 100
            y1 = y0 + 100
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="red", tags="highlight-{}-{}".format(part[0], part[1]))

def image_for_password():
    Mass_password = []

    for i in range(3):
        root = tk.Toplevel()
        root.title("Graphical Password")

        image_path = f"{i + 1}.jpg"
        rows = 5
        columns = 10

        app = GraphicalPasswordApp(root, image_path, rows, columns)

        def submit_password():
            password = app.get_password()
            Mass_password.append(password)
            messagebox.showinfo("Пароль", "Ваш графический пароль: {}".format(password))
        submit_button = tk.Button(root, text="Подтвердить", command=submit_password)
        submit_button.pack()

        root.mainloop()
        root.destroy()

    print(Mass_password)


def registration():
    root3 = tk.Toplevel()
    root3.title("Абонент А")
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

    code = tk.Button(root3, text="Подтвердить", command=image_for_password, font=("Helvetica", 12), bg="#CD950C",
                     fg="black")
    code.place(x=200, y=200)

    root3.mainloop()



root2 = tk.Tk()
root2.title("Абонент А")
root2.geometry("500x200")

code = tk.Button(root2, text="Регистрация", command=registration, font=("Helvetica", 12), bg="#CD950C", fg="black")
code.place(x=200, y=10)

Decode = tk.Button(root2, text="Вход", command=image_for_password, font=("Helvetica", 12), bg="#CD950C", fg="black")
Decode.place(x=173, y=50)

Control_btn = tk.Button(root2, text="Забыли пароль?", command=image_for_password, font=("Helvetica", 12), bg="#CD950C", fg="black")
Control_btn.place(x=214, y=90)


root2.mainloop()