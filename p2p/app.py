import socket
import threading
import sys


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\nСоединение закрыто")
                break
            print("\r" + data.decode() + "\n> ", end="")
        except:
            break


def send_messages(sock, name):
    while True:
        try:
            message = input("> ")
            if message.lower() == "/exit":
                sock.close()
                break
            full_message = f"{name}: {message}"
            sock.send(full_message.encode())
        except:
            break


def main():
    name = input("Введите ваше имя: ")
    host = "127.0.0.1" # локальный адрдес, ЗАМЕНИТЬ НА НУЖНЫЙ (адрес собеседника из своей сети)
    port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((host, port))
        sock.listen(1)
        print("Ожидание подключения собеседника...")
        conn, addr = sock.accept()
        sock = conn
        sock.send(name.encode())
        peer_name = sock.recv(1024).decode()
        print(f"К вам подключился собеседник {peer_name}. Чат работает")


    except OSError:
        print("Подключаемся к собеседнику...")
        sock.connect((host, port))
        sock.send(name.encode())
        peer_name = sock.recv(1024).decode()
        print(f"Вы подключились к собеседнику {peer_name}. Чат работает")

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(sock,),
        daemon=True
    )
    receive_thread.start()

    send_messages(sock, name)



if __name__ == "__main__":
    main()
