# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing Stuff")
        self.setGeometry(0, 0, 1600, 900)
        self.setWindowIcon(QIcon("patchouli.png"))

        label = QLabel("IDK TBH man", self)
        label.setFont(QFont("Wingdings", 24))
        label.setGeometry(0, 0, 1600, 900)
        label.setStyleSheet("color: #999999;"
                            "background-color: ffffff;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()