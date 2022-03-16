from email import message
import sys
from time import sleep
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget ,QStackedWidget , QMainWindow
from time import sleep
import socket
from threading import *
import threading
from functools import partial

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def Recieve(c):
    # while 1:
    reply = c.recv(1024).decode()
    print(reply)
    server.serverrec.setText(str(reply))
    return


def Send(c):
    # while 1:
        # message = input("Server: ")
    print("1==================")
    message=server.serversend.text()
    print(message,"2==================")
    c.send(message.encode())
    return



class ServerScreen(QMainWindow):
    def __init__(self):
        super(ServerScreen,self).__init__()
        self.initUI()

    def startListening(self):
        print('start')
        print("startlistening clicked",server.port.text())
        s.bind(('localhost',int(server.port.text())))
        s.listen()
        # sleep(10)
        print("port is listening")
        c, addr = s.accept()
        print("Connected to",addr)
        # while 1: or self.serverrec.text()!=str(c.recv(1024).decode())
        print("1------server2------")
        # Recieve(c)
        print("2------server2------")
        self.send.clicked.connect(lambda:Send(c))
        print(self.send.isChecked())
        # if self.serverrec.text()!= "received message":
        #     print( self.serverrec.text())
        # #     # Send(c)
        # Recieve(c)
        # sleep(3)
        s.close()

    def initUI(self):
        loadUi('server.ui',self)
        self.startlistening.clicked.connect(self.startListening)
            
    




# def main():
app= QApplication(sys.argv)
server=ServerScreen()
Widget=QStackedWidget()
Widget.addWidget(server)
Widget.setFixedHeight(800)
Widget.setFixedWidth(1200)
Widget.show()
sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()




















from asyncio.windows_events import NULL
import sys
from time import sleep
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget ,QStackedWidget , QMainWindow
from time import sleep
import socket
from threading import *

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def outputMethod():
    # while 1:
        reply = c.recv(1024).decode()
        print(reply)
        client.clientrec.setText(str(reply))
        # print('client: ', reply)
        return


def inputMethod():
    # while 1:
        message=client.clientsend.text()
        print(c,"=-=-=-=-=-")
        c.send(message.encode())
        return

   

class ClientScreen(QMainWindow):
    def __init__(self):
        super(ClientScreen,self).__init__()
        self.initUI()

    def startListening(self):
        print("startlistening clicked",self.ipport.text())
        ip,port =self.ipport.text().split(":")
        print(ip,port)
        c.connect(('localhost', int(port)))
        # while 1:
        # if self.clientrec.text()!= "received message":
        #     print(self.clientrec.text())
        outputMethod()
        print("------client2------")
        # if self.send.isChecked():
        # inputMethod()
        print(c)
        self.send.clicked.connect(inputMethod)
        # self.send.clicked.connect(inputMethod)
        # c.close()
      
    def initUI(self):
        loadUi('client.ui',self)
        self.startlistening.clicked.connect(self.startListening)
            
    




# def main():
app= QApplication(sys.argv)
client=ClientScreen()
Widget=QStackedWidget()
Widget.addWidget(client)
Widget.setFixedHeight(800)
Widget.setFixedWidth(1200)
Widget.show()
sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()