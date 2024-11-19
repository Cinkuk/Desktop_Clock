import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(' ')
        self.setGeometry(300, 300, 300, 100)
        self.show()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.timeLabel = QLabel('00:00:00', self)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("QLabel { color : white; font-size : 128px; }")
        self.layout.addWidget(self.timeLabel)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(0, 0, 0))  # 背景黑色

    def updateTime(self):
        time = self.currentTime()
        self.timeLabel.setText(time)

    def currentTime(self):
        from datetime import datetime
        now = datetime.now()
        return now.strftime('%H:%M')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Clock()
    sys.exit(app.exec_())