from tokenize import Double
from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QDesktopWidget, QLabel, QTableWidget, QAbstractItemView, QTableWidgetItem
from algorithm import *
from utils.info import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QUrl

class Second(QWidget):
  def __init__(self):
    super().__init__()
    
    p = self.palette()
    p.setColor(QPalette.Window, Qt.white)
    self.setPalette(p)
    
    self.setWindowIcon(QIcon("fish.ico"))
    self.current = [-1]      
    self.initUI()  
  
  def initUI(self):
    self.setWindowTitle('Ready Page') 
    self.resize(1200, 800)
    self.center()      

    title = QLabel('Fish checker {}'.format(str(' ')), self)
    title.move(400,-120) #move(430,-170)
    title.resize(450,450)
    title_font = title.font()
    title_font.setPointSize(40)
    title.setFont(title_font)            

    #첫번째 페이지(first_page)로 이동하는 버튼
    self.btn = QPushButton("First Page", self)
    self.btn.move(20, 10)
    self.btn.resize(170,40) #
    btn_font = self.btn.font()
    btn_font.setPointSize(10)
    self.btn.setFont(btn_font)
    self.btn.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(240, 114, 114);"+
                           "color:white;}"
                           )   

    #다음 페이지(video_page)로 이동하는 버튼
    self.btn2 = QPushButton("Next Page", self)
    self.btn2.move(1010, 10)
    self.btn2.resize(170,40) #
    btn_font = self.btn2.font()
    btn_font.setPointSize(10)
    self.btn2.setFont(btn_font)
    self.btn2.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           ) 

    self.table = QTableWidget(self)
    self.table.setRowCount(1)
    self.table.setColumnCount(2)
    self.table.resize(550, 100)
    self.table.move(550, 200) #move(550, 100)
    self.table.setHorizontalHeaderLabels(['ID', 'Video path'])

    clear = QPushButton('Clear', self)
    clear.clicked.connect(self.table.clearContents)
    clear.resize(80,40) #추가
    clear.move(1020, 308) #위치 바꿈
    clear.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )     
    val = QTableWidgetItem("1")
    self.table.setItem(0, 0, val)
    val = QTableWidgetItem("./inference/test.mp4")
    self.table.setItem(0, 1, val)
    
    ready = QPushButton('Ready', self)
    ready.clicked.connect(self.save)
    ready.resize(80,40) #추가
    ready.move(920, 308) #위치 바꿈
    ready.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )    

    self.cb1 = QCheckBox('어종 종합 정보', self)
    self.cb1.move(100, 200) #move(100, 100)
    self.cb1.resize(300,30)
    self.cb2 = QCheckBox('어종 길이 계산, 무게 예측', self)
    self.cb2.move(100, 230) #move(100, 130)
    self.cb2.resize(300,30)
    self.cb3 = QCheckBox('양(인분) 계산', self)
    self.cb3.move(100, 260) #move(100, 160)
    self.cb3.resize(300,30)
    self.cb4 = QCheckBox('GPS 기반 위치별 시세 안내', self)
    self.cb4.move(100, 290) #move(100, 190)
    self.cb4.resize(300,30)
    #self.cb5 = QCheckBox('Check box 1', self)
    #self.cb5.move(100, 220)
    #self.cb5.resize(300,30)
    #self.cb6 = QCheckBox('Check box 1', self)
    #self.cb6.move(100, 250)
    #self.cb6.resize(300,30)
    #self.cb7 = QCheckBox('Check box 1', self)
    #self.cb7.move(100, 280)
    #self.cb7.resize(300,30)

    #GBox = QLabel(self)
    #GBox.setStyleSheet("color: dark;"
    #                         "border-style: solid;"
    #                         "border-width: 3px;"
    #                         "border-color: #000000;"
    #                         "border-radius: 3px")
    #GBox.move(100, 250-7) #move(100, 250-7)
    #GBox.resize(1000, 300) 

    self.GB = QLabel(self)    
    self.times = []
    self.lines = []
    self.labels = []
    for i in range(50):
        time = QLabel(self)
        line = QLabel(self)
        label = QLabel(self)
        time.resize(30,30)
        line.resize(30,30)
        label.resize(30,30)

        self.times.append(time)
        self.lines.append(line)
        self.labels.append(label)

    #gb = QLabel(self)
    #gb.setStyleSheet("color: dark;"
    #                         "border-style: solid;"
    #                         "border-width: 3px;"
    #                         "border-color: #000000;"
    #                         "border-radius: 3px")
    #gb.move(100, 313-70) #move(100, 313-70)
    #gb.resize(130, 40)    

    #Gant = QLabel('   Video', self)
    #Gant.move(105, 250)
    #gant_font = Gant.font()
    #gant_font.setPointSize(20)
    #Gant.setFont(gant_font)    

    #self.name은 어디에 쓰이는 것이지???!
    self.name = QLabel('                    ', self)
    self.name.move(115, 360)
    self.name_font = self.name.font()
    self.name_font.setPointSize(18)
    self.name.setFont(self.name_font)      

    #prev = QPushButton('<', self)
    #prev.clicked.connect(self.prev)
    #prev.move(980, 500)

    #next = QPushButton('>', self)
    #next.clicked.connect(self.next)
    #next.move(1030, 500)        

    #이것들을 조금만 밑으로 내려야겠다
    output = QLabel(self)
    output.setStyleSheet("color: blue;"
                       "background-color: #ffffff;"
                       "border-style: solid;"
                       "border-width: 3px;"
                       "border-color: #000000")   
    output.move(100, 313+100) #move(100, 313-70)
    output.resize(1000, 50)     

    output2 = QLabel(self)
    output2.setStyleSheet("color: blue;"
                        "background-color: #ffffff;"
                       "border-style: solid;"
                       "border-width: 3px;"
                       "border-color: #000000")   
    output2.move(100, 313+50+100) #move(100, 313-70+50)
    output2.resize(1000, 100) 

    output3 = QLabel(self)
    output3.setStyleSheet("color: blue;"
                        "background-color: #ffffff;"
                       "border-style: solid;"
                       "border-width: 3px;"
                       "border-color: #000000")   
    output3.move(100, 313+100+100) #move(100, 313-70+100)
    output3.resize(1000, 200)    

    output4 = QLabel(self)
    output4.setStyleSheet("color: blue;"
                        "background-color: #ffffff;"
                       "border-style: solid;"
                       "border-width: 3px;"
                       "border-color: #000000")   
    output4.move(100, 313+200+100) #move(100, 313-70+200)
    output4.resize(1000, 100) 

    self.text1 = QLabel('Species:                                                                                                                                                                                                                                                              ', self)
    self.text1.move(100+10, 313+10+100) #move(100+10, 313-70+10)
    self.text1.setBaseSize(1000,10)
    
    self.text1_font = self.text1.font()
    self.text1_font.setPointSize(20)
    self.text1.setFont(self.text1_font) 

    self.text2 = QLabel('Info 1:                                                                                                                                                                                                                                                                        ', self)
    self.text2.move(100+10, 313+50+10+100) #move(100+10, 313-70+50+10)
    self.text2_font = self.text2.font()
    self.text2_font.setPointSize(15)
    self.text2.setFont(self.text2_font) 

    self.text3 = QLabel('Info 2:                                                                                                                                                                                                                                                                                                                                                                                              ', self)
    self.text3.move(100+10, 313+100+10+100) #move(100+10, 313-70+100+10) 
    self.text3_font = self.text3.font()
    self.text3_font.setPointSize(15)
    self.text3.setFont(self.text3_font) 

    self.text4 = QLabel('Info 3:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ', self)                             
    self.text4.move(100+10, 313+200+10+100) #move(100+10, 313-70+200+10)
    self.text4_font = self.text4.font()
    self.text4_font.setPointSize(15)
    self.text4.setFont(self.text4_font)

    self.text5 = QLabel('                                                                                                                                                                                                            ',self)                             
    self.text5.move(300, 730)
    self.text5_font = self.text5.font()
    self.text5_font.setPointSize(25)
    self.text5.setFont(self.text5_font)        

    clear.clicked.connect(self.text1.clear)
    clear.clicked.connect(self.text2.clear)
    clear.clicked.connect(self.text3.clear)
    clear.clicked.connect(self.text4.clear)

    # self.table2 = QTableWidget(self)
    # self.table2.setRowCount(3)
    # self.table2.setColumnCount(1)
    # self.table2.resize(550, 150)
    # self.table2.move(550, 620)
    # self.table2.setVerticalHeaderLabels(['Fish IL', 'Fish TL', 'Fish WW'])
    # self.table2.setEditTriggers(QAbstractItemView.NoEditTriggers)    

    # text5 = QLabel('OUTPUT', self)
    # text5.move(550, 570)
    # text5_font = text5.font()
    # text5_font.setPointSize(20)
    # text5.setFont(text5_font) 

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())   

  def save(self):
      rowcount = self.table.rowCount()
      columncount = self.table.columnCount()
      self.data = []
      self.ID = []
      print("Input data checking...")
      
      
      for row in range(0, rowcount):
          if self.table.item(row,0) is None:
              break
          
          self.data.append([])
          idx = self.table.item(row,0)
          self.ID.append(str(idx.text()))
   
          for column in range(0, columncount):
              value = self.table.item(row, column)
              if value is not None:
                  if column != 0:
                      self.data[row].append(str(value.text())) # ['ID', 'Video path'] 순서로 value가 들어감
                  else:
                      self.data[row].append(str(value.text()))
              else:
                  self.data[row].append(0)


      #self.table2.setHorizontalHeaderLabels(self.ID)           
      self.list = []

      #for cb, name in [(self.cb1, 'Check box1'), (self.cb2, 'Check box2'), (self.cb3, 'Check box3'), (self.cb4, 'Check box4'), (self.cb5, 'Check box5'), (self.cb6, 'Check box6'), (self.cb7, 'Check box7')]:
      #    if cb.isChecked():
      #        self.list.append(name)
      print(self.data)
      
      
      self.scheduling()

  def scheduling(self):
      self.output = []
      #if self.list is None:
      #    return None

      #else:   
      #    self.output = []
      #    speciesinfo, fishTL, fishIL, bongIT  = run(self.data)
      #    self.output.append([speciesinfo, fishTL, fishIL, bongIT, data[0][1]])

      #    self.recommendation()
      #    self.draw_output()
      print('Detect run...')
      species = 'Species'
      speciesinfo = ['Info1','Info2','Info3']
      fishTL = 0
      fishIL = 0
      bongIT = 0
      species, speciesinfo, fishTL, fishIL, bongIT  = run()
      
      self.output.append([species, speciesinfo, fishTL, fishIL, bongIT])
      print(self.output)
      self.draw_output()

  def recommendation(self):
      self.rec1 = sorted(self.output, key = lambda x : (x[-4], x[-3], x[-2]))
      self.rec2 = sorted(self.output, key = lambda x : (x[-3], x[-2], x[-4]))
      self.rec3 = sorted(self.output, key = lambda x : (x[-2], x[-3], x[-4]))
      self.top1 = self.rec1[0][-1]  
      self.top2 = self.rec2[0][-1]
      self.top3 = self.rec3[0][-1]

      result = set((self.top1, self.top2, self.top3))
      result = list(result)

      self.text4.setText('Recommendation:')

      if len(result) == 3:
          self.text5.setText(' {}, {}, {}'.format(result[0], result[1], result[2]))
      elif len(result) == 2:
          self.text5.setText(' {}, {}'.format(result[0], result[1]))
      elif len(result) == 1:
          self.text5.setText(' {}'.format(result[0]))                    

  def draw_output(self, alpha = 1):
      #if alpha == 1:
      #  self.current = [self.list[0], 0]

      #self.name.setText('{}'.format(self.current[0]))

      #self.show_video()
      self.draw_remain()
      

  def prev(self):
      if len(self.list) != 0:
        if self.current[-1] != 0:
            self.current = [self.list[self.current[-1] - 1], self.current[-1] - 1]
            self.draw_output(alpha = 0)
        else:
            pass
      else:
          pass

  def next(self):
      if len(self.list) != 0:      
        if self.current[-1] != len(self.list) - 1:
            self.current = [self.list[self.current[-1] + 1], self.current[-1] + 1]
            self.draw_output(alpha = 0)
        else:
            pass
      else:
          pass  

  def show_video(self):       
      pass

  def cal_weight(self):
    print("Cal_weight...")
    s = 'G'
    l = str(31.91)
    print(s, l)

    weighttable = {
      'C' : [0.027, 2.819],
      'G' : [0.005, 3.126],
      'J' : [0.007, 3.058],
      'S' : [0.017, 2.792],
      'N' : [0.016, 2.928],
      'K' : [0,0],
      'O' : [0,0]
    }
    print(l)
    w = 0.005 * (Double(l) ** 3.126)
    #w = float(weighttable[s][0])*(float(l)**float(weighttable[s][1])) # if weighttable[s] is not None else '무게 예측 불가'
    print(w)
    return w

  def draw_remain(self):
    #for i in range(len(self.output)):
    #    if self.current[0] in self.output[i]:
    #        index = i
    #        break
    index = 0
    print("Draw_remain...")


    Fish_IL = self.output[index][3]
    Fish_TL = self.output[index][2]
    print(self.output[index][0], Fish_TL)
    s = self.output[index][0]
    print(s)
    print(weighttable)
    Fish_WW = weighttable[s][0]*(Fish_TL**weighttable[s][1])#cal_weight(self.output[index][0], Fish_TL)
    print(Fish_WW)
    #   for i in range(len(Fish_IL)):
    #       val = QTableWidgetItem(str(Fish_IL[i]))
    #       self.table2.setItem(0, i, val)

    #   for i in range(len(Fish_TL)):
    #       val = QTableWidgetItem(str(Fish_TL[i]))
    #       self.table2.setItem(1, i, val)

    #   for i in range(len(Fish_TW)):
    #       val = QTableWidgetItem(str(Fish_TW[i]))
    #       self.table2.setItem(2, i, val)


    
    # val = QTableWidgetItem(str(Fish_IL))
    # self.table2.setItem(0, 0, val)
    # val = QTableWidgetItem(str(Fish_TL))
    # self.table2.setItem(1, 0, val)
    # val = QTableWidgetItem(str(Fish_WW))
    # self.table2.setItem(2, 0, val)

    f = open("result.txt", 'a')
    print(str(round(Fish_IL,3)) + '/' + str(round(Fish_TL,3)) + '/' + str(round(Fish_WW,3)))    
    f.write(str(round(Fish_IL,3)) + '/' + str(round(Fish_TL,3)) + '/' + str(round(Fish_WW,3)))
    f.close()

    
    self.text1.setText('Species: {}'.format(speciesinfo[s][0])) #species, speciesinfo, fishTL, fishIL, bongIT
    self.text1_font.setPointSize(10)
    self.text2.setText('기본정보 : ' + speciesinfo[s][1])
    self.text2_font.setPointSize(4)
    self.text3.setText('고르는 법: ' + speciesinfo[s][2])
    self.text3_font.setPointSize(4)
    self.text4.setText('추천음식: ' + speciesinfo[s][3])
    self.text4_font.setPointSize(4)
    self.text2.setWordWrap(True)
    self.text3.setWordWrap(True)
    self.text4.setWordWrap(True)


