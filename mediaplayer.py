from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton,QVBoxLayout,QLabel,QSlider,QStyle, QSizePolicy,QFileDialog
import sys 
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt,QUrl

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Media Player")
    self.setGeometry(450, 200, 1000, 700)
    self.setWindowIcon(QIcon('icon.png'))

    palette = self.palette()
    palette.setColor(QPalette.Window, Qt.black)
    self.setPalette(palette)

    self.ui()
    self.show() 
    
  def ui(self):

    # create media player object 
    self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

    # create videowidget object
    videowidget = QVideoWidget()

    # create open button
    openbtn = QPushButton('Open Video')
    openbtn.clicked.connect(self.open_file)

    # create button for playing
    self.playbtn = QPushButton()
    self.playbtn.setEnabled(False)
    self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
    self.playbtn.clicked.connect(self.play_video)

    #create slider
    self.slider = QSlider(Qt.Horizontal)
    self.slider.setRange(0,0)
    self.slider.sliderMoved.connect(self.set_position)

    #create label
    self.label = QLabel()
    self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

    # create hbox layout
    hboxLayout = QHBoxLayout()
    hboxLayout.setContentsMargins(0,0,0,0)

    # set widgets to the hbox layout
    hboxLayout.addWidget(openbtn)
    hboxLayout.addWidget(self.playbtn)
    hboxLayout.addWidget(self.slider)

    #create vbox layout
    vboxlayout = QVBoxLayout()
    vboxlayout.addWidget(videowidget)
    vboxlayout.addLayout(hboxLayout)
    vboxlayout.addWidget(self.label)
    self.setLayout (vboxlayout)
    self.mediaPlayer.setVideoOutput(videowidget)

    # media player signals

    self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
    self.mediaPlayer.positionChanged.connect(self.position_changed)
    self.mediaPlayer.durationChanged.connect(self.duration_changed)
      

  def open_file(self):
    filename, _ =QFileDialog.getOpenFileName(self, "Open Good Files ") 

    if filename != '':   
      self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
      self.playbtn.setEnabled(True)

  def play_video(self):
    if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
      self.mediaPlayer.pause()
    else:
      self.mediaPlayer.play()

  def mediastate_changed(self,state):
    if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
      self.playbtn.setIcon(
        self.style().standardIcon(QStyle.SP_MediaPause)
      )
    else:
      self.playbtn.setIcon(
        self.style().standardIcon(QStyle.SP_MediaPlay)
      )

  def position_changed(self, position):
    self.slider.setValue(position)

  def duration_changed(self, duration):
    self.slider.setRange(0, duration)
  
  def set_position(self, position):
    self.mediaPlayer.setPosition(position)
  
  def handle_errors(self):
    self.playbtn.setEnabled(False)
    self.label.setText("Error: " + self.mediaPlayer.errorString())
    

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())