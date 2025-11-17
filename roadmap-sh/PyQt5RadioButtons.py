# PyQt5 Radio Buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QVBoxLayout, QWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 300, 250)
        self.game1 = QRadioButton("Deadlock", self)
        self.game2 = QRadioButton("League of Legends", self)
        self.game3 = QRadioButton("Valorant", self)
        self.game4 = QRadioButton("Counter-Strike", self)
        self.store1 = QRadioButton("Steam", self)
        self.store2 = QRadioButton("GOG", self)
        self.store3 = QRadioButton("Epic Games", self)
        self.store4 = QRadioButton("Microsoft Store", self)
        self.bg1 = QButtonGroup(self)
        self.bg2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.game1, 0)
        layout.addWidget(self.game2, 1)
        layout.addWidget(self.game3, 2)
        layout.addWidget(self.game4, 3)
        layout.addWidget(self.store1, 4)
        layout.addWidget(self.store2, 5)
        layout.addWidget(self.store3, 6)
        layout.addWidget(self.store4, 7)
        self.bg1.addButton(self.game1)
        self.bg1.addButton(self.game2)
        self.bg1.addButton(self.game3)
        self.bg1.addButton(self.game4)
        self.bg2.addButton(self.store1)
        self.bg2.addButton(self.store2)
        self.bg2.addButton(self.store3)
        self.bg2.addButton(self.store4)


        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;"
                           "font-family: Arial;"
                           "}")

        self.game1.toggled.connect(self.radio_button_changed)
        self.game2.toggled.connect(self.radio_button_changed)
        self.game3.toggled.connect(self.radio_button_changed)
        self.game4.toggled.connect(self.radio_button_changed)
        self.store1.toggled.connect(self.radio_button_changed)
        self.store2.toggled.connect(self.radio_button_changed)
        self.store3.toggled.connect(self.radio_button_changed)
        self.store4.toggled.connect(self.radio_button_changed)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())