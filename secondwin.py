#Этот код писал я, Пермяков Максим Дмитриевич
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)
from finalwin import *
from instr import *
from project import *
class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_next2, self)
        self.n_text = QLabel(txt_n)
        self.settings_text1 = QLabel(txt_settings1)
        self.settings_text2 = QLabel(txt_settings2)
        self.settings_text3 = QLabel(txt_settings3)

        self.n_text.setFont(QFont("Times", 18, QFont.Bold))
        self.n_text.setStyleSheet("color: rgb(255,255,255)")

        self.settings_text1.setFont(QFont("Times", 16))
        self.settings_text1.setStyleSheet("color: rgb(255,255,255)")
        self.settings_text2.setFont(QFont("Times", 16))
        self.settings_text2.setStyleSheet("color: rgb(255,255,255)")
        self.settings_text3.setFont(QFont("Times", 16))
        self.settings_text3.setStyleSheet("color: rgb(255,255,255)")

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.n_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text1, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text2, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.settings_text3, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)             
        self.setLayout(self.layout_line)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{background-color:dark-blue}")   
#Этот код писал я, Пермяков Максим Дмитриевич