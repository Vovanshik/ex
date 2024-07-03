import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import cv2
import numpy as np
from threading import Thread

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class ImageProcessor:

    def __init__(self, quant_step=10):
        self.quant_step = quant_step


    def convert_to_grayscale(self, image):
        return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    def haar_wavelet_transform(self, image):
        transformed = np.copy(image)
        (rows, cols) = image.shape
        for i in range(0, rows, 2):
            for j in range(0, cols, 2):
                transformed[i // 2, j // 2] = (image[i, j] + image[i, j + 1] + image[i + 1, j] + image[i + 1, j + 1]) / 4
        return transformed[:rows // 2, :cols // 2]

    def inverse_haar_wavelet_transform(self, image, original_shape):
        restored = np.zeros(original_shape)
        (rows, cols) = original_shape
        for i in range(0, rows, 2):
            for j in range(0, cols, 2):
                restored[i:i + 2, j:j + 2] = image[i // 2, j // 2]
        return restored

    def quantize(self, image):
        return np.round(image / self.quant_step) * self.quant_step

    def process_image(self, img_path, progress_callback):
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = self.convert_to_grayscale(img)

        progress_callback(20)

        transformed = self.haar_wavelet_transform(gray)
        progress_callback(40)
        quantized = self.quantize(transformed)
        progress_callback(60)
        restored = self.inverse_haar_wavelet_transform(quantized, gray.shape)
        progress_callback(80)

        return restored


    def set_quant_step(self, quant_step):
        self.quant_step = quant_step

class GUIApp:
    def __init__(self, master):
        self.master = master
        master.title("Сжатие изображений")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        self.processor = ImageProcessor()
        self.create_widgets()


    def create_widgets(self):
        style = ttk.Style()
        style.configure('new.TFrame', background="red")
        style.configure('TButton', font=BUTTON_FONT, foregroung=WHITE, background=OCEAN_BLUE,  padding=10)  # Кнопки
        style.configure('TLabel', font=BUTTON_FONT, foregroung=WHITE, background=OCEAN_BLUE, padding=5)  # Метки
        style.configure('Horizontal.TScale',foregroung=WHITE, background=OCEAN_BLUE, sliderlength=30)  # Ползунок
        style.configure("red.Horizontal.TProgressbar", background=OCEAN_BLUE)

        middle_frame = tk.Frame(root, width=700, height=600, bg=MEDIUM_GREY)
        middle_frame.grid(row=1, column=0, sticky=tk.NSEW)


        self.load_btn = tk.Button(self.master, text="Загрузить", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE,command=self.load_image)
        self.load_btn.place(x=50, y=50, width=200, height=50)


        self.save_btn = tk.Button(self.master, text="Сохранить",font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=self.save_image)
        self.save_btn.place(x=350, y=50, width=200, height=50)


        self.process_btn = tk.Button(self.master, text="Обработать", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE,command=self.process_image)
        self.process_btn.place(x=50, y=150, width=200, height=50)


        self.status_lbl = ttk.Label(self.master, text="Пусто:(")
        self.status_lbl.place(x=50, y=350)


        self.quant_lbl = ttk.Label(self.master, text="Шаг квантования:")
        self.quant_lbl.place(x=350, y=150)


        self.quant_slider = ttk.Scale(self.master, from_=10, to=300, orient='horizontal', command=self.update_quant_value)
        self.quant_slider.place(x=350, y=180, width=200)


        self.progress = ttk.Progressbar(self.master, style="red.Horizontal.TProgressbar", orient="horizontal", length=300, mode="determinate")
        self.progress.place(x=150, y=250)


    def load_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.status_lbl.config(text="Картинка загружена")
            self.loaded_image = cv2.imread(self.file_path)

    def process_image(self):
        if hasattr(self, 'loaded_image'):
            self.processor.set_quant_step(int(self.quant_slider.get()))
            Thread(target=self.start_processing, daemon=True).start()
        else:
            messagebox.showwarning("Ошибка", "Изображения нет")

    def start_processing(self):
        self.processed_image = self.processor.process_image(self.file_path, self.update_progress)
        self.status_lbl.config(text="Картинка обработана")
        self.update_progress(100)


    def update_progress(self, value):
        self.progress['value'] = value
        self.master.update_idletasks()

    def save_image(self):
        if hasattr(self, 'processed_image'):
            save_path = filedialog.asksaveasfilename(defaultextension='.jpg')
            cv2.imwrite(save_path, self.processed_image)
            messagebox.showinfo("✓", "Картинка сохранена")
        else:
            messagebox.showwarning("!", "Изображение не обработано")

    def update_quant_value(self, value):
        self.status_lbl.config(text=f"Шаг квантования: {int(float(value))}")

# Точка входа в программу
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
