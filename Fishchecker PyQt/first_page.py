from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QDesktopWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui

class First(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setWindowIcon(QIcon("fish.ico"))
    p = self.palette()
    p.setColor(QPalette.Window, QColor(30, 93, 193))
    self.setPalette(p)

    self.initUI()
  
  def initUI(self):
    
    self.setWindowTitle('Initial page')
    #self.setStyleSheet("background : #ffffff;")
    self.resize(800, 800)
    self.center()   

    title = QLabel('  fishChecker', self)
    title.move(250,-75) #move(300,-150)
    title.resize(450,450)
    title_font = title.font()
    title_font.setPointSize(30)
    title_font.setWeight(600)
    title.setFont(title_font)
    title.setStyleSheet("color: white;")
    
    #logo
    #image = QPixmap('./fishchecker.PNG')
    #logo = QLabel()
    #logo.setPixmap(image)
    #logo.move(250,-75)          

    info = QLabel('  2022 데이터 청년 캠퍼스', self)
    info.move(225, 460) #move(250, 550)
    info.resize(600,200)
    info_font = info.font()
    info_font.setPointSize(20)
    info.setFont(info_font)
    info.setStyleSheet("color: white;")      

    info2 = QLabel('고려대학교 지능정보시스템 개발 과정 11팀', self)
    info2.move(135, 510) #수정
    info2.resize(600,200)
    info2_font = info2.font()
    info2_font.setPointSize(20)
    info2.setFont(info2_font)
    info2.setStyleSheet("color: white;")          

    self.btn = QPushButton("Fish checker run", self)
    #self.btn.setFont(QFont('Times', 15, QFont.Bold))
    #self.btn.setFont(QFont(20, QFont.Bold))
    self.btn.resize(500,100)
    self.btn.move(150, 230) #move(150, 160)
    self.btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.btn.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )
    #255 202         
    btn_font = self.btn.font()
    btn_font.setPointSize(17)
    self.btn.setFont(btn_font)
    
    self.btn2 = QPushButton("Fish checker info", self)
    #self.btn2.setFont(QFont('Times', 15, QFont.Bold))
    self.btn2.resize(500,100)
    self.btn2.move(150, 380) #move(150, 320)
    self.btn2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.btn2.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )  
    btn2_font = self.btn2.font()
    btn2_font.setPointSize(17)
    self.btn2.setFont(btn2_font)
    
    #self.btn3 = QPushButton("info_3", self)
    #self.btn3.resize(500,100)
    #self.btn3.move(150, 480)     


    
  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())
    
    #self.pixmap = QPixmap('main.jpg')
    #self.label =QLabel(self)
    #self.label.setPixmap(QPixmap(self.pixmap))
    #self.label.resize(self.pixmap.width(), self.pixmap.height())

    #palette = QPalette()
    #palette.setBrush(QPalette.Background, QColor(255,0,255))#QBrush(QPixmap("main.jpg")))
    #self.setAutoFillBackground(True)
    #self.setPalette(palette)
