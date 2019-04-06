import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QMainWindow, qApp,
                             QVBoxLayout, QPushButton, QMenuBar, QMenu, QAction)

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NiseTaiga - skr47ch")
        self.statusBar().showMessage("This is a status bar")
        self.setGeometry(50, 50, 400, 200)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        file_menu.addMenu('Library Folders')


        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit  Program')
        exit_action.triggered.connect(qApp.quit)

        file_menu.addAction(exit_action)
        # self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = Example()
    window.show()
    sys.exit(app.exec_())