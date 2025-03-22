import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QFont

class App(QWidget):

    def __init__(self):
        super().__init__()
        # window = QMainWindow()
        self.title= "Account Registration System"
        self.initUI()

        # Icon
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(750,300,500,500)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.setStyleSheet("background-color : #acdcf9")

        # Buttons
        self.button1 = QPushButton('Submit', self)
        self.button1.setToolTip("Click to Submit!")
        self.button1.move(100,400)
        self.button1.setGeometry(100, 400, 100, 40)
        self.button1.setFont(QFont('Arial', 10, QFont.Bold))
        self.button1.setStyleSheet("background-color : #757dd9")
        self.button1.clicked.connect(self.submit)

        self.button2 = QPushButton('Clear', self)
        self.button1.setToolTip("Click to Clear!")
        self.button2.move(300,400)
        self.button2.setGeometry(300, 400, 100, 40)
        self.button2.setFont(QFont('Arial', 10, QFont.Bold))
        self.button2.setStyleSheet("background-color : #757dd9")

        # Textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(210, 80)
        self.textbox1.resize(260, 30)
        self.textbox1.setText("")
        self.textbox1.setFont(QFont('Arial', 12))
        self.textbox1.setStyleSheet("background-color : white")

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(210, 130)
        self.textbox2.resize(260, 30)
        self.textbox2.setText("")
        self.textbox2.setFont(QFont('Arial', 12))
        self.textbox2.setStyleSheet("background-color : white")

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(210, 180)
        self.textbox3.resize(260, 30)
        self.textbox3.setText("")
        self.textbox3.setFont(QFont('Arial', 12))
        self.textbox3.setStyleSheet("background-color : white")

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(210, 230)
        self.textbox4.resize(260, 30)
        self.textbox4.setText("")
        self.textbox4.setFont(QFont('Arial', 12))
        self.textbox4.setStyleSheet("background-color : white")

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(210, 280)
        self.textbox5.resize(260, 30)
        self.textbox5.setText("")
        self.textbox5.setFont(QFont('Arial', 12))
        self.textbox5.setStyleSheet("background-color : white")

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(210, 330)
        self.textbox6.resize(260, 30)
        self.textbox6.setText("")
        self.textbox6.setFont(QFont('Arial', 12))
        self.textbox6.setStyleSheet("background-color : white")

        # Labels
        self.textboxlbl1 = QLabel("First Name: ", self)
        self.textboxlbl1.move(50, 80)
        self.textboxlbl1.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl2 = QLabel("Last Name: ", self)
        self.textboxlbl2.move(50, 130)
        self.textboxlbl2.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl3 = QLabel("Username: ", self)
        self.textboxlbl3.move(50, 180)
        self.textboxlbl3.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl4 = QLabel("Password: ", self)
        self.textboxlbl4.move(50, 230)
        self.textboxlbl4.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl5 = QLabel("Email Address: ", self)
        self.textboxlbl5.move(50, 280)
        self.textboxlbl5.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl6 = QLabel("Contact Number: ", self)
        self.textboxlbl6.move(50, 330)
        self.textboxlbl6.setFont(QFont('Arial', 11, QFont.Bold))

        self.textboxlbl7 = QLabel("REGISTER", self)
        self.textboxlbl7.move(218, 30)
        self.textboxlbl7.setFont(QFont('Arial', 12, QFont.Bold))

        # Clear
        self.button2.clicked.connect(self.textbox1.clear)
        self.button2.clicked.connect(self.textbox2.clear)
        self.button2.clicked.connect(self.textbox3.clear)
        self.button2.clicked.connect(self.textbox4.clear)
        self.button2.clicked.connect(self.textbox5.clear)
        self.button2.clicked.connect(self.textbox6.clear)

        self.show()

    def submit(self):
        print("Submmited")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())