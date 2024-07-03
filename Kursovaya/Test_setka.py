import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class GraphicalPasswordApp:
    def __init__(self, master, images, rows, columns):
        self.master = master
        self.images = images
        self.current_image_index = 0
        self.rows = rows
        self.columns = columns
        self.selected_parts = set()
        self.passwords = {}  # Словарь для хранения паролей для каждой картинки

        self.canvas = tk.Canvas(master, width=700, height=500)
        self.canvas.pack()

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_left_click)

        # Кнопка для смены изображения
        self.submit_button = tk.Button(master, text="Submit", command=self.change_image)
        self.submit_button.pack()

        # Кнопка для создания пароля
        self.password_button = tk.Button(master, text="Create Password", command=self.create_password)
        self.password_button.pack()

        self.password = ""

    def load_image(self):
        if self.current_image_index < len(self.images):
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((700, 500))
            self.photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

            # Рисование сетки
            cell_width = 700 // self.columns
            cell_height = 500 // self.rows
            for i in range(1, self.rows):
                self.canvas.create_line(0, i * cell_height, 700, i * cell_height, fill="gray")
            for i in range(1, self.columns):
                self.canvas.create_line(i * cell_width, 0, i * cell_width, 500, fill="gray")
        else:
            self.save_passwords()
            self.master.destroy()

    def change_image(self):
        self.create_password()  # Сохранить пароль перед сменой изображения
        self.current_image_index += 1
        self.canvas.delete("all")  # Очистить холст перед загрузкой нового изображения
        self.selected_parts.clear()  # Очистить выбранные части
        self.load_image()

    def on_left_click(self, event):
        row = event.y // (500 // self.rows)
        column = event.x // (700 // self.columns)
        part = (int(row), int(column))

        if part in self.selected_parts:
            self.selected_parts.remove(part)
            self.canvas.delete("dot-{}-{}".format(part[0], part[1]))
        else:
            self.selected_parts.add(part)
            x0 = column * (700 // self.columns)
            y0 = row * (500 // self.rows)
            x1 = x0 + (700 // self.columns)
            y1 = y0 + (500 // self.rows)
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="red", tags="dot-{}-{}".format(part[0], part[1]))

    def create_password(self):
        self.password = ""
        for part in sorted(self.selected_parts):
            self.password += str(part[0]) + str(part[1]) + " "
        print(self.passwords)

        self.passwords[self.current_image_index] = self.password.strip()

    def save_passwords(self):
        with open("passwords.txt", "w") as f:
            for image_index, password in self.passwords.items():
                f.write(f"Image {image_index}: {password}\n")

def main():
    root = tk.Tk()
    root.title("Graphical Password")

    # Пути к изображениям
    images = ["1.jpg", "2.jpg", "3.jpg","4.jpg","5.jpg"]

    # Количество строк и столбцов для сетки
    rows = 20
    columns = 20

    app = GraphicalPasswordApp(root, images, rows, columns)

    root.mainloop()

if __name__ == "__main__":
    main()