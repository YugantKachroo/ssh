import sys
from PyQt4 import QtGui, QtCore
import sys
from sender import transfer
from scanner import scan_ports
class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,464,417)
        self.home()

    def home(self):
        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(20,60,401,231))
        self.listWidget.addItem(str(1))
        self.listWidget.addItem(str(2))
        self.listWidget.itemClicked.connect(self.Connect)
        self.path = QtGui.QLineEdit(self)
        self.path.setGeometry(QtCore.QRect(20,310,281,29))
        self.File = str(self.path.text())
        self.IP = '127.0.0.1'

        btn1 = QtGui.QPushButton("send", self)
        btn1.clicked.connect(self.Send)
        btn1.resize(btn1.minimumSizeHint())
        btn1.move(220,20)

        btn2 = QtGui.QPushButton("Select File", self)
        btn2.clicked.connect(self.selectFile)
        btn2.resize(btn2.minimumSizeHint())
        btn2.move(310,310)

        btn3 = QtGui.QPushButton("refresh", self)
        btn3.clicked.connect(self.scanPorts)
        btn3.resize(btn2.minimumSizeHint())
        btn3.move(30,20)
        self.show()
    def Send(self):
        print(self.IP)
        print(self.File)
        transfer(self.IP,self.File)
    def selectFile(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        print(name)
        self.path.setText(name)
        self.File = name
        print (self.File)
    def scanPorts(self):
        self.listWidget.clear()
        Hs=scan_ports()
        print('ft')
        for i, host in enumerate(Hs, start=1):
            self.listWidget.addItem(str(host[1]))
    def Connect(self,ip):
        self.IP = ip.text()
        print(self.IP)
'''
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
'''