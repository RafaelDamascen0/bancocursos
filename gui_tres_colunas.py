import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
 
class GuiTresColunas(QWidget):
 
 def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa do Mercado")


       
 