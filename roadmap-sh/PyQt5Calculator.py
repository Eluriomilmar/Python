import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

num1 = ""
operacao = "0"
num2 = ""
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
        self.buttonclear.setObjectName("buttonclear")
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.buttonsum.setObjectName("buttonsum")
        self.button4.setObjectName("button4")
        self.button5.setObjectName("button5")
        self.button6.setObjectName("button6")
        self.buttonsubtract.setObjectName("buttonsubtract")
        self.button7.setObjectName("button7")
        self.button8.setObjectName("button8")
        self.button9.setObjectName("button9")
        self.buttonmultiply.setObjectName("buttonmultiply")
        self.buttoncomma.setObjectName("buttoncomma")
        self.button0.setObjectName("button0")
        self.buttonresult.setObjectName("buttonresult")
        self.buttondivide.setObjectName("buttondivide")

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
        self.button1.clicked.connect(self.click)
        self.button2.clicked.connect(self.click)
        self.button3.clicked.connect(self.click)
        self.button4.clicked.connect(self.click)
        self.button5.clicked.connect(self.click)
        self.button6.clicked.connect(self.click)
        self.button7.clicked.connect(self.click)
        self.button8.clicked.connect(self.click)
        self.button9.clicked.connect(self.click)
        self.button0.clicked.connect(self.click)

        self.buttonsum.clicked.connect(self.click)
        self.buttonsubtract.clicked.connect(self.click)
        self.buttonmultiply.clicked.connect(self.click)
        self.buttondivide.clicked.connect(self.click)
        self.buttoncomma.clicked.connect(self.click)
        self.buttonclear.clicked.connect(self.click)
        self.buttonresult.clicked.connect(self.click)

    def click(self):
        global num1, operacao, num2
        match QApplication.focusWidget().objectName():
            case "button0":
                if operacao == "0":
                    num1 += "0"
                    self.line_edit.setText(num1)
                else:
                    num2 += "0"
                    self.line_edit.setText(num2)
            case "button1":
                if operacao == "0":
                    num1 += "1"
                    self.line_edit.setText(num1)
                else:
                    num2 += "1"
                    self.line_edit.setText(num2)
            case "button2":
                if operacao == "0":
                    num1 += "2"
                    self.line_edit.setText(num1)
                else:
                    num2 += "2"
                    self.line_edit.setText(num2)
            case "button3":
                if operacao == "0":
                    num1 += "3"
                    self.line_edit.setText(num1)
                else:
                    num2 += "3"
                    self.line_edit.setText(num2)
            case "button4":
                if operacao == "0":
                    num1 += "4"
                    self.line_edit.setText(num1)
                else:
                    num2 += "4"
                    self.line_edit.setText(num2)
            case "button5":
                if operacao == "0":
                    num1 += "5"
                    self.line_edit.setText(num1)
                else:
                    num2 += "5"
                    self.line_edit.setText(num2)
            case "button6":
                if operacao == "0":
                    num1 += "6"
                    self.line_edit.setText(num1)
                else:
                    num2 += "6"
                    self.line_edit.setText(num2)
            case "button7":
                if operacao == "0":
                    num1 += "7"
                    self.line_edit.setText(num1)
                else:
                    num2 += "7"
                    self.line_edit.setText(num2)
            case "button8":
                if operacao == "0":
                    num1 += "8"
                    self.line_edit.setText(num1)
                else:
                    num2 += "8"
                    self.line_edit.setText(num2)
            case "button9":
                if operacao == "0":
                    num1 += "9"
                    self.line_edit.setText(num1)
                else:
                    num2 += "9"
                    self.line_edit.setText(num2)
            case "buttondivide" | "buttonmultiply" | "buttonsum" | "buttonsubtract":
                operacao = QApplication.focusWidget().objectName()
                self.line_edit.setText(num2)
                case "buttoncomma":
                if operacao == "0":
                    if "." not in num1:
                        num1 += "."
                        self.line_edit.setText(num1)
                    else:
                        num1 = num1
                else:
                    if "." not in num2:
                        num2 += "."
                        self.line_edit.setText(num2)
                    else:
                        num2 = num2
            case "buttonclear":
                operacao = "0"
                num1 = ""
                num2 = ""
                self.line_edit.setText(num1)
            case "buttonresult":
                num1 = float(num1)
                num2 = float(num2)
                match operacao:
                    case "buttonsum":
                        result = num1 + num2
                        if float(result) == int(result):
                            result = int(result)
                        self.line_edit.setText(str(result))
                    case "buttonsubtract":
                        result = num1 - num2
                        if float(result) == int(result):
                            result = int(result)
                        self.line_edit.setText(str(result))
                    case "buttondivide":
                        result = num1 / num2
                        if float(result) == int(result):
                            result = int(result)
                        self.line_edit.setText(str(result))
                    case "buttonmultiply":
                        result = num1 * num2
                        if float(result) == int(result):
                            result = int(result)
                        self.line_edit.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())