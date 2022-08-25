import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from first_page import First
from second_page import Second
from video_page import Window
from video_page2 import Window2
#from second_page2 import Second2
from PyQt5.QtGui import QFontDatabase, QFont

if __name__ == '__main__':
  app = QApplication(sys.argv)

  fontDB = QFontDatabase()
  fontDB.addApplicationFont('./font/a옛날사진관3.ttf')
  app.setFont(QFont('a옛날사진관3'))
  
  first = First()
  second1 = Second()
  second2 = Second()
  video1 = Window()
  video2 = Window2()
  #second3 = Second3()

  first.show()
  first.btn.clicked.connect(second1.show)
  first.btn.clicked.connect(first.close)
  first.btn2.clicked.connect(second2.show)
  first.btn2.clicked.connect(first.close)
  #first.btn3.clicked.connect(second3.show)
  #first.btn3.clicked.connect(first.close)

  second1.btn.clicked.connect(first.show)
  second1.btn.clicked.connect(second1.close)
  second1.btn2.clicked.connect(video1.show) #
  second1.btn2.clicked.connect(second1.close)
  
  second2.btn.clicked.connect(first.show)
  second2.btn.clicked.connect(second2.close)
  #second3.btn.clicked.connect(first.show)
  #second3.btn.clicked.connect(second2.close)
  
  video1.btn.clicked.connect(second1.show) #
  video1.btn.clicked.connect(video1.close) #
  video1.btn2.clicked.connect(video2.show) #
  video1.btn2.clicked.connect(video1.close) #
  
  video2.btn.clicked.connect(video1.show) #
  video2.btn.clicked.connect(video2.close) #
  video2.btn2.clicked.connect(first.show) #
  video2.btn2.clicked.connect(video2.close) #
    

  sys.exit(app.exec_())
      
