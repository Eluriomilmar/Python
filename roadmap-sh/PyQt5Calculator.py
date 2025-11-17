import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 640, 450)
        self.line_edit = QLineEdit(self)
        self.button0 = QPushButton("0", self)
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.buttonsum = QPushButton("+",self)
        self.buttonsubtract = QPushButton("-", self)
        self.buttonmultiply = QPushButton("*", self)
        self.buttondivide = QPushButton("/", self)
        self.buttonclear = QPushButton("C", self)
        self.buttonresult = QPushButton("=", self)
        self.buttoncomma = QPushButton(",", self)
        self.initUI()


    def initUI(self):
        self.line_edit.setGeometry(0, 10, 480, 90)
        self.buttonclear.setGeometry(480, 10, 160, 90)
        self.button1.setGeometry(0, 100, 160, 90)
        self.button2.setGeometry(160,100, 160, 90)
        self.button3.setGeometry(320, 100, 160, 90)
        self.buttonsum.setGeometry(480, 100, 160, 90)
        self.button4.setGeometry(0, 190, 160, 90)
        self.button5.setGeometry(160,190, 160, 90)
        self.button6.setGeometry(320, 190, 160, 90)
        self.buttonsubtract.setGeometry(480, 190, 160, 90)
        self.button7.setGeometry(0, 280, 160, 90)
        self.button8.setGeometry(160,280, 160, 90)
        self.button9.setGeometry(320, 280, 160, 90)
        self.buttonmultiply.setGeometry(480, 280, 160, 90)
        self.buttoncomma.setGeometry(0, 370, 160, 90)
        self.button0.setGeometry(160, 370, 160, 90)
        self.buttonresult.setGeometry(320, 370, 160, 90)
        self.buttondivide.setGeometry(480, 370, 160, 90)
        self.setStyleSheet("QPushButton{font-size: 50px};")
        self.line_edit.setStyleSheet("font-size: 50px;")
        self.line_edit.setReadOnly(True)
        self.button1.clicked.connect(self.on_click)

    def on_click(self):
        self.button1.setText("Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())