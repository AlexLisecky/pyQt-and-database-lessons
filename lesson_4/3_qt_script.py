import sys
from PyQt5.QtWidgets import QApplication, QWidget , QLabel , QPushButton , QVBoxLayout
from PyQt5 import QtWidgets
app = QApplication(sys.argv)



window = QWidget()
window.resize(300,70)
window.setWindowTitle('hello world')
window.move(300,300)
label = QLabel('<center>hello world<center>')
btnQuit = QPushButton('Close window')
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(btnQuit)
window.setLayout(layout)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())

