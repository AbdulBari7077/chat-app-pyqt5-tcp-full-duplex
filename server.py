from email import message
import sys
from time import sleep
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget ,QStackedWidget , QMainWindow
from time import sleep
import socket as s
from threading import *
import threading
from functools import partial



def Recieve():
    while 1:
        reply = client.recv(1024).decode()
        print(reply)
        server.serverrec.setText(str(reply))
    return


def startListening(port):
    global client, addr
    socket = s.socket()
    print('started socket')
    socket.bind(('localhost',int(port)))
    socket.listen(5)
    # sleep(10)
    # print("port is listening")
    while True:
        client, addr = socket.accept()
        print("connected")
        threading.Thread(target=Recieve).start()
    # print("Connected to",addr)
    # # while 1: or self.serverrec.text()!=str(c.recv(1024).decode())
    # print("1------server2------")
    # # Recieve(c)
    # print("2------server2------")
    # server.send.clicked.connect(lambda:Send(c))
    # print(server.send.isChecked())
    # if self.serverrec.text()!= "received message":
    #     print( self.serverrec.text())
    # #     # Send(c)
    # Recieve(c)
    # sleep(3)
    s.close()

def Send():
    message=server.serversend.text()
    print(message,"2==================")
    client.send(message.encode())
    return

def verifyPort():
    port =server.port.text()
    print("startlistening clicked",server.port.text())
    if int(port)>0 and int(port)<65535: 
        t1 = threading.Thread(target=startListening, args=(port,))
        t1.start()
    else:
        print("Wrong Port")


class ServerScreen(QMainWindow):
    def __init__(self):
        super(ServerScreen,self).__init__()
        self.initUI()
   
    def initUI(self):
        loadUi('server.ui',self)
        # self.startlistening.clicked.connect(startListening)
            
    


# def main():
app= QApplication(sys.argv)
server=ServerScreen()
Widget=QStackedWidget()
Widget.addWidget(server)
Widget.setFixedHeight(800)
Widget.setFixedWidth(1200)
Widget.show()
server.startlistening.clicked.connect(verifyPort)
server.send.clicked.connect(Send)
sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()