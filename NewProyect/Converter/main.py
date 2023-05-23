import sys
import ffmpeg
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QMessageBox,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QMainWindow, QAction, QComboBox)

class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Cute Converter")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.convertButton = QPushButton("Convertir")
        self.convertButton.setEnabled(False)
        self.convertButton.clicked.connect(self.convert)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.sliderMoved.connect(self.setVolume)

        self.formatBox = QComboBox()
        self.formatBox.addItems(["mp4", "mp3", "avi", "mkv", "flv"])
        self.formatBox.setEnabled(False)

        self.helpMenu = self.menuBar().addMenu("&Ayuda")
        self.helpAction = QAction("&Instrucciones", self)
        self.helpAction.triggered.connect(self.showHelp)
        self.helpMenu.addAction(self.helpAction)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
        controlLayout.addWidget(self.volumeSlider)
        controlLayout.addWidget(self.formatBox)
        controlLayout.addWidget(self.convertButton)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        openButton = QPushButton("Abrir Video")
        openButton.clicked.connect(self.openFile)

        controlLayout.addWidget(openButton)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Video",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.convertButton.setEnabled(True)
            self.formatBox.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def setVolume(self, position):
        self.mediaPlayer.setVolume(position)

    def convert(self):
        inputFile = self.mediaPlayer.media().canonicalUrl().path()
        outputFile = "output." + self.formatBox.currentText()
        ffmpeg.input(inputFile).output(outputFile).run()
    
    def showHelp(self):
        helpText = """
        1. Haz clic en 'Abrir Video' para seleccionar un archivo de video.
        2. Usa el botón 'Play' para iniciar o pausar la reproducción.
        3. Usa el slider de la izquierda para ajustar la posición del video.
        4. Usa el slider de la derecha para ajustar el volumen.
        5. Selecciona un formato de salida en la lista desplegable.
        6. Haz clic en 'Convertir' para convertir el video al formato seleccionado.
        """
        helpWindow = QMessageBox()
        helpWindow.setText(helpText)
        helpWindow.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())

