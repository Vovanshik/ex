import socket
import threading
from typing import List
from math import log2, ceil

HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 5
active_clients = []

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
            active_clients.append((username, client))
            prompt_message = "Сервер~" + f"{username} добавлен в чат"
            send_messages_to_all(prompt_message)
            break
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