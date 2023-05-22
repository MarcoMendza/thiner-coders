import os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QMessageBox, QPushButton, QSlider, QVBoxLayout, QWidget
import moviepy.editor as mp

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.setWindowTitle("Reproductor de Video")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        self.openButton = QPushButton("Abrir Archivo")
        self.openButton.clicked.connect(self.openFile)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setText("Reproducir")
        self.playButton.clicked.connect(self.play)

        self.convertButton = QPushButton("Convertir a MP4")
        self.convertButton.clicked.connect(self.convertFile)

        self.helpButton = QPushButton("Ayuda")
        self.helpButton.clicked.connect(self.showHelp)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.sliderMoved.connect(self.setVolume)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(QLabel("Abrir:"))
        controlLayout.addWidget(self.openButton)
        controlLayout.addWidget(QLabel("Reproducir:"))
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(QLabel("Convertir:"))
        controlLayout.addWidget(self.convertButton)
        controlLayout.addWidget(QLabel("Ayuda:"))
        controlLayout.addWidget(self.helpButton)
        controlLayout.addWidget(QLabel("Volumen:"))
        controlLayout.addWidget(self.volumeSlider)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addWidget(QLabel("Progreso:"))
        layout.addWidget(self.positionSlider)
        layout.addLayout(controlLayout)

        self.setLayout(layout)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Video")

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.currentFile = fileName

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def convertFile(self):
        if hasattr(self, 'currentFile'):
            clip = mp.VideoFileClip(self.currentFile)
            clip.write_videofile("output.mp4")

    def showHelp(self):
        QMessageBox.information(self, "Ayuda", "Este es un reproductor de video básico...")

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setText("Pausar")
        else:
            self.playButton.setText("Reproducir")

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def setVolume(self, volume):
        self.mediaPlayer.setVolume(volume)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())

