import socket
import threading
from typing import List
from math import log2, ceil
import random
import sympy
import hashlib
from tkinter import messagebox


HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 2
active_clients = []





def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


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
    primes = generate_primes(999)
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



def autentif_user_1():

    with open('ecp_user_1.txt', 'r') as f:
        n = f.read()
    f.close()

    with open('open_key_A.txt', 'r') as f:
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

def autentif_user_2():

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








def not_correct_hamming(msg: str, mode: int=8) -> str:
    result = ""

    s_num = ceil(log2(log2(mode + 1) + mode + 1))
    res_len = len(msg) // (mode + s_num)
    code_len = mode + s_num

    to_hamming = []

    for i in range(res_len):
        code = list(map(int, msg[i * code_len:i * code_len + code_len]))
        to_hamming.append(code)
    for i in to_hamming:
        for j in range(s_num):
            i.pop(2 ** j - 1 - j)
        result += "".join(map(str, i))

    msg_l = []

    for i in range(len(result) // 8):
        val = "".join(result[i * 8:i * 8 + 8])
        msg_l.append(int(val, 2))

    result = bytes(msg_l).decode("utf-8",errors='replace')

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

def hamming_decode(msg: str, mode: int=8) -> str:
    result = ""

    s_num = ceil(log2(log2(mode + 1) + mode + 1))
    res_len = len(msg) // (mode + s_num)
    code_len = mode + s_num

    to_hamming = []

    for i in range(res_len):
        code = list(map(int, msg[i * code_len:i * code_len + code_len]))
        to_hamming.append(code)

    hamming_common(to_hamming, s_num, False)

    for i in to_hamming:
        for j in range(s_num):
            i.pop(2 ** j - 1 - j)
        result += "".join(map(str, i))

    msg_l = []

    for i in range(len(result) // 8):
        val = "".join(result[i * 8:i * 8 + 8])
        msg_l.append(int(val, 2))

    result = bytes(msg_l).decode("utf-8")

    return result





def listen_for_messages(client, username):
    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            BLOCK_MODE = 8
            dec_msg = hamming_decode(message, BLOCK_MODE)
            print(username + '~' + not_correct_hamming(message,BLOCK_MODE))
            print(username + '~' + message)

            final_msg = username + '~' + dec_msg
            send_messages_to_all(final_msg)


        else:
            print(f"Сообщение от {username} пустое")



def send_message_to_client(client, message):
    client.sendall(message.encode())



def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)



def client_handler(client):
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            if username == 'Alice':
                proverka = autentif_user_1()
                if proverka == 1:
                    active_clients.append((username, client))
                    prompt_message = "Сервер~" + f"{username} прошел аутентификацию"
                    prompt_message_1 = "Сервер~" + f"{username} добавлен в чат"
                    send_messages_to_all(prompt_message)
                    send_messages_to_all(prompt_message_1)
                    break
                else:
                    messagebox.showerror("ERROR","Вы ваши данные были подменены!")
                    exit()
            elif username == 'Bob':
                proverka = autentif_user_2()
                if proverka == 1:
                    active_clients.append((username, client))
                    prompt_message = "Сервер~" + f"{username} прошел аутентификацию"
                    prompt_message_1 = "Сервер~" + f"{username} добавлен в чат"
                    send_messages_to_all(prompt_message)
                    send_messages_to_all(prompt_message_1)
                    break
                else:
                    messagebox.showerror("ERROR", "Вы ваши данные были подменены!")
                    exit()


        else:
            print("Пустое имя пользователя")

    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Запуск сервера на {HOST} {PORT}")
    except:
        print(f"Невозможно подключиться к {HOST}  {PORT}")

    server.listen(LISTENER_LIMIT)
    while 1:
        client, address = server.accept()
        print(f"Подключение к клиенту успешно {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client,)).start()


if __name__ == '__main__':
    main()