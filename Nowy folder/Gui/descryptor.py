import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import base64

import bcrypt


def descryptor():
    print('ok')

def openWindow():
    WindowDescription()

class WindowDescription(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ceramikaIkona.png"))
        self.setWindowTitle("Przelicznik")
        self.setContentsMargins(20, 20, 20, 20)
        self.window_width = 300
        self.window_height = 200
        self.setFixedSize(self.window_width, self.window_height)

        #Buttons
        button = QPushButton('Przelicz', self)
        button.setGeometry(100, 100, 100, 20)

        #Labels
        label1 = QLabel('Tekst przed:',self)
        label1.setGeometry(20, 20, 100, 20)
        label2 = QLabel('Tekst po:',self)
        label2.setGeometry(150, 20, 100, 20)

        #TextLine
        self.text1 = QLineEdit(self)
        self.text1.setGeometry(20, 60, 100, 25)
        self.text2 = QLineEdit('test1',self)
        self.text2.setGeometry(150, 60, 100, 25)

        button.clicked.connect(self.__takeData)


    def __takeData(self):
        text1 = self.text1.text()
        encode_message = text1.encode("utf-8")
        print(encode_message)
        base64_b64encode = base64.b64encode(encode_message)

        encrypt = base64_b64encode.decode('utf-8')

        hashedEcrypt = bcrypt.hashpw(encode_message, bcrypt.gensalt(10))
        print(hashedEcrypt)
        print(encrypt)


app = QApplication(sys.argv)
window = WindowDescription()
window.show()
sys.exit(app.exec())




