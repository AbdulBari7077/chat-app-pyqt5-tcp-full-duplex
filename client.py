from asyncio.windows_events import NULL
import sys
from time import sleep
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget ,QStackedWidget , QMainWindow
from time import sleep
import socket
import threading 

def SendMsg():
    message=client.clientsend.text()
    c.send(message.encode())
    return


def outputMethod():
    while 1:
        reply = c.recv(1024).decode()
        print(reply)
        client.clientrec.setText(str(reply))
        print('client: ', reply)
        return



def connectclient(ip, port): #connects a socket
    global c
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('localhost', int(port)))
    threading.Thread(target=outputMethod).start()

def verifyPort():
    print("startlistening clicked",client.ipport.text())
    ip,port =client.ipport.text().split(":")
    # print(ip,port)
    if int(port)>0 and int(port)<65535: 
        t1 = threading.Thread(target=connectclient, args=(ip, port)) # run connect function -> argumrnts( port + ip)
        t1.start()
    else:
        print("Wrong Port")


class ClientScreen(QMainWindow):
    def __init__(self):
        super(ClientScreen,self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('client.ui',self)
            
    




# def main():
app= QApplication(sys.argv)
client=ClientScreen()
client.startlistening.clicked.connect(verifyPort)
client.send.clicked.connect(SendMsg)
Widget=QStackedWidget()
Widget.addWidget(client)
Widget.setFixedHeight(800)
Widget.setFixedWidth(1200)
Widget.show()
sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()