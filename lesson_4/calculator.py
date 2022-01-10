import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = QWidget()
    main_window.resize(400,400)
    main_window.move(300,300)
    main_window.setWindowTitle('Калькулятор')
    main_window.show()

    sys.exit(app.exec_())

