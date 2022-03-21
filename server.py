
import sys
from tkinter import Widget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QWidget ,QStackedWidget , QMainWindow
from time import sleep
import socket 
import threading

clients = set()
clients_lock = threading.Lock()


def Recieve():
    while 1:
        # print(client)
        reply = client.recv(1024).decode()
        print("recived server:",reply)
        server.serverrec.setText(str(reply))
    return


def startListening(port):
    global client, addr
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('started socket')
    s.bind(('localhost',int(port)))
    s.listen(5)
    # sleep(10)
    print("port is listening")
    while True:
        client, addr = s.accept()
        with clients_lock:
            clients.add(client)
        print("--------------------connected----------------------")
        # sleep(10)
        threading.Thread(target=Recieve).start()

def Send():
    message=server.serversend.text()
    with clients_lock:
        for c in clients:
            c.sendall(message.encode())
    # client.sendall()
    return

def verifyPort():
    port =server.port.text()
    print("startlistening clicked",server.port.text())
    try :
        if int(port)>0 and int(port)<65535: 
            t1 = threading.Thread(target=startListening, args=(port,))
            t1.start()
        else:
            print("Wrong Port : Port should be between 0-65535")
    except:
        print("Wrong Port : Port should be between 0-65535")
    # if (server.port.text()) == "" :
    #     print("-------------Port Field should be Not Empty------")
    #     # server.port.setText(str("0-65535"))
    #     # verifyPort()
    #     return
    # elif int(port)>0 and int(port)<65535: 
    #     t1 = threading.Thread(target=startListening, args=(port,))
    #     t1.start()
    # else:
        



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