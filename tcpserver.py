from time import sleep
import socket
from threading import *
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class recv:
    def __init__(self, c):
        self.c = c

    def run(self):
        while 1:
            reply = self.c.recv(1024).decode()
            print('Client: ', reply)

class send:
    def __init__(self, c):
        self.c = c

    def run(self):
        while 1:
            message = input("Server: ")
            self.c.send(message.encode())

def main():
    s.bind(('localhost',1234))
    s.listen(3)
    sleep(10)
    c, addr = s.accept()
    th1 = recv(c)
    th2 = send(c)
    t1 = threading.Thread(target=th1.run, )
    sleep(3)
    t2 = threading.Thread(target=th2.run, )
    status = t1.start()
    # if status == False:
    #         break
    t2.start()
    t1.join()
    t2.join()
    s.close()

main()
