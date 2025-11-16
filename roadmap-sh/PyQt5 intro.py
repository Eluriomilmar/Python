# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing Stuff")
        self.setGeometry(0, 0, 400, 400)
        self.setWindowIcon(QIcon("patchouli.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label2 = QLabel(self)
        label2.setGeometry(0,0, 400, 400)
        label2.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("patchouli.png")
        label2.setPixmap(pixmap)
        label1 = QLabel("IDK TBH man", self)
        label1.setFont(QFont("Wingdings", 24))
        label1.setGeometry(0, 0, 400, 400)
        label1.setStyleSheet("color: #000000;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label1.setAlignment(Qt.AlignCenter)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()