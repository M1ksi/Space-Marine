from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit)

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_title = 'Space Marine'
txt_hello = 'Добро пожаловать в игру, которая взорвет шаблоны мироздания!'
txt_lore = 'Человечество содрогалось под ударами бесчисленных врагов...\nС каждым днем становилось всё хуже. Все ресурсы были мобилизованы ради одного единственного супероружия...\nКоторое возглавил командир МегаМаксон9000'
txt_next = 'Начать'