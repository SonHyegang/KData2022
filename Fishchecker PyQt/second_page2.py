from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QDesktopWidget, QLabel, QTableWidget, QAbstractItemView, QTableWidgetItem

class Second2(QWidget):
  def __init__(self):
    super().__init__() 
    self.current = [-1]      
    self.initUI()  
  
  def initUI(self):
    self.setWindowTitle('Fishchecker Info') 
    self.resize(1200, 800)
    self.center()      
