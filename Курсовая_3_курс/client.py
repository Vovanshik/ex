# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from typing import List
from math import log2, ceil
from random import randrange

HOST = '127.0.0.1'
PORT = 12345

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def noizer(msg: str, mode: int) -> str:

    seq = list(map(int, msg))
    s_num = ceil(log2(log2(mode + 1) + mode + 1))
    code_len = mode + s_num
    cnt = len(msg) // code_len
    result = ""

    for i in range(cnt):
        to_noize = seq[i * code_len:i * code_len + code_len]
        noize = randrange(code_len)
        to_noize[noize] = int(not to_noize[noize])
        result += "".join(map(str, to_noize))

    return result

def hamming_common(src: List[List[int]], s_num: int, encode=True) -> None:
    s_range = range(s_num)

    for i in src:
        sindrome = 0
        for s in s_range:
            sind = 0
            for p in range(2 ** s, len(i) + 1, 2 ** (s + 1)):
                for j in range(2 ** s):
                    if (p + j) > len(i):
                        break
                    sind ^= i[p + j - 1]

            if encode:
                i[2 ** s - 1] = sind
            else:
                sindrome += (2 ** s * sind)

        if (not encode) and sindrome:
            i[sindrome - 1] = int(not i[sindrome - 1])


def hamming_encode(msg: str, mode: int=8) -> str:
    result = ""
    msg_b = msg.encode("utf-8")
    s_num = ceil(log2(log2(mode + 1) + mode + 1))
    bit_count = []
    for byte in msg_b:
        bit_count += list(map(int, f"{byte:08b}"))
    res_len = ceil((len(msg_b) * 8) / mode)
    bit_count += [0] * (res_len * mode - len(bit_count))

    to_hamming = []

    for i in range(res_len):
        code = bit_count[i * mode:i * mode + mode]
        for j in range(s_num):
            code.insert(2 ** j - 1, 0)
        to_hamming.append(code)

    print(to_hamming)

    hamming_common(to_hamming, s_num, True)

    for i in to_hamming:
        result += "".join(map(str, i))

    return result


def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)



def connect():

    try:
        # Connect to the server
        client.connect((HOST, PORT))
        add_message("[SERVER] Успешное подключение к серверу")
    except:
        messagebox.showerror("Невозможно подключиться", f"Невозможно подключиться {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Пустое имя", "Имя не должно быть пустым")

    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)


def send_message():
    message = message_textbox.get()
    BLOCK_MODE = 8
    if message != '':
        enc_msg = hamming_encode(message, BLOCK_MODE)
        noize_msg = noizer(enc_msg, BLOCK_MODE)
        client.sendall(noize_msg.encode())
        message_textbox.delete(0, len(noize_msg))
    else:
        messagebox.showerror("Пустое сообщения", "Сообщение должно что то содержать")


root = tk.Tk()
root.geometry("600x600")
root.title("Локальная сеть")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=600, bg=MEDIUM_GREY)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Имя:", font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(top_frame, text="Подключиться", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=32)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Отправить", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


def listen_for_messages_from_server(client):
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split('~')[1]


            add_message(f"[{username}] {content}")

        else:
            messagebox.showerror("Ошибка", "Пустое сообщения")


# main function
def main():
    root.mainloop()


if __name__ == '__main__':
    main()