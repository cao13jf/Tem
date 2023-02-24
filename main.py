from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
import tensorflow as tf

import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        layout = QVBoxLayout()
        label = QLabel("My simple app.")
        label.setMargin(10)
        layout.addWidget(label)

        button1 = QPushButton("Hide")
        button1.setIcon(QIcon("icons/hand.png"))
        button1.pressed.connect(self.lower)
        layout.addWidget(button1)

        button2 = QPushButton("Import TF")
        button2.setIcon(QIcon("icons/lightning.png"))
        button2.pressed.connect(self.import_tf)
        layout.addWidget(button2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.show()

    def import_tf(self):
        self.model = tf.keras.Sequential()
        QMessageBox.about(self, "Title", "TF imported")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()