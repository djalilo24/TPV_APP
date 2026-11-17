from PyQt5 import QtCore, QtGui, QtWidgets
class Home(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.home_ui()

    def home_ui(self):
         
        self.group_home = QtWidgets.QVBoxLayout(self)
        self.setStyleSheet("""QWidget { background-color: #DCE8DF;}""")
        self.title = QtWidgets.QLabel("Welcome to the Home Page")
        self.group_home.addWidget(self.title)
