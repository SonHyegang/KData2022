from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QStyle, QSlider, QFileDialog, QLabel, QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("fish.ico"))
        self.setWindowTitle("fishChecker")
        #self.setGeometry(350, 100, 1000, 700) #(350, 100, 700, 500)
        self.resize(1200, 800)
        self.center()
        
        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)
        
        self.create_player()
    
    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget = QVideoWidget()
        
        self.title = QLabel('                                   Fish checker Rotate', self)
        #self.title.move(300,200)
        self.title.resize(450,450)
        title_font = self.title.font()
        title_font.setPointSize(22)
        self.title.setFont(title_font)  
        
        #이전 페이지(video_page)로 이동하는 버튼
        self.btn = QPushButton("Prev Page", self)
        self.btn.move(20, 10)
        self.btn.resize(170,40) #
        btn_font = self.btn.font()
        btn_font.setPointSize(10)
        self.btn.setFont(btn_font)
        self.btn.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )
        
        #첫 번째 페이지로 돌아가는 버튼
        self.btn2 = QPushButton("First Page", self)
        self.btn2.move(1010, 10)
        self.btn2.resize(170,40) #
        btn2_font = self.btn2.font()
        btn2_font.setPointSize(12)
        self.btn2.setFont(btn2_font)
        self.btn2.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(240, 114, 114);"+
                           "color:white;}"
                           )
        
        #영상을 트는 버튼
        self.openBtn = QPushButton('Video2')
        self.openBtn.clicked.connect(self.open_video)
        openBtn_font = self.openBtn.font()
        openBtn_font.setPointSize(12)
        self.openBtn.setFont(openBtn_font)
        self.openBtn.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )
        
        #영상 재생 버튼
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setStyleSheet("*{color: rgb(30, 93, 193);"+
                           "background-color: white;"+
                           "border: 2px solid rgb(30, 93, 193);"+
                           "border-radius: 20px;}"+
                           "*:hover{background-color: rgb(241, 176, 15);"+
                           "color:white;}"
                           )
        
        #영상 슬라이더
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_pos)
        
        ################# 배치하기 ##################
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title, stretch=1)
        vbox.addWidget(videowidget, stretch=4)
        vbox.addLayout(hbox)
        
        #hbox.addWidget(self.btn) #
        
        self.mediaPlayer.setVideoOutput(videowidget)
        
        self.setLayout(vbox) #vbox
        ############################################
        
        self.mediaPlayer.stateChanged.connect(self.state_changed)
        self.mediaPlayer.positionChanged.connect(self.pos_changed)
        self.mediaPlayer.durationChanged.connect(self.dur_changed)

    def open_video(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl("./result2.mp4"))) #경로 바꿔야 함
        self.playBtn.setEnabled(True)
        
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        
        else:
            self.mediaPlayer.play()
        
    def state_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            
    def pos_changed(self, position):
        self.slider.setValue(position)
    
    def dur_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_pos(self, position):
        self.mediaPlayer.setPosition(position)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())