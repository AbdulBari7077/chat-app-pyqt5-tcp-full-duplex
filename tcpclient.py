from time import sleep
from threading import *
import socket
import threading

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def outputMethod():
    while 1:
        reply = c.recv(1024).decode()
        print('Server: ', reply)


def inputMethod():
    while 1:
        message = input("Client: ")
        c.send(message.encode())
    

def main():

    c.connect(('localhost', 1234))
    t1 = threading.Thread(target=outputMethod, )
    t2 = threading.Thread(target=inputMethod, )
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    c.close()

main()