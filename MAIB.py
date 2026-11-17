from PyQt5 import QtCore, QtGui, QtWidgets
from style import use_style
from PyQt5.QtGui import QIcon
from home import Home
from transporteurs import Transp
from PyQt5.QtWidgets import QWidget
import mysql.connector
import traceback
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.MainWindow = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("T.P.V 2.0")
#================taille screen============================
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        #===========pocentge========
        percentage = 85
        window_width = int(screen_width * percentage / 100)
        window_height = int(screen_height * percentage / 100)
        MainWindow.resize(window_width, window_height)

        #===========centre screen======
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        MainWindow.move(x, y)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.showMaximized()
#==========layout pricipale====================
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        #=================group menu=========================
        self.group_menu = QtWidgets.QGroupBox()
        self.group_menu.setObjectName("group_menu")
        #=====================group content=========================
        self.main_content = QtWidgets.QGroupBox()
        self.main_content.setObjectName("main_content")
 
        #=================add layout=========================
        self.main_layout.addWidget(self.group_menu, 2)
        self.main_layout.addWidget(self.main_content, 8)
        # ================= pages =========================
        self.pages = QtWidgets.QStackedWidget()
        self.content_layout = QtWidgets.QVBoxLayout(self.main_content)
        self.content_layout.setContentsMargins(10, 10, 10, 10)
        self.content_layout.addWidget(self.pages) 
        self.pages.setStyleSheet("""QStackedWidget { background-color: #DCE8DF;}""")
#=====================add button=========================
        #============bouton home============
        self.btn_home = QtWidgets.QPushButton(self.group_menu)
        self.btn_home.setText("Tableau de bord | لوحة التحكم")
        self.btn_home.setIcon(QtGui.QIcon("icons/home.png"))
        self.btn_home.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        self.btn_home.setObjectName("btn_menu")
        self.btn_home.clicked.connect(self.home_button_clicked)       
        #============bouton transporteur============
        self.btn_transp = QtWidgets.QPushButton(self.group_menu)
        self.btn_transp.setText("Transporteurs | الناقلين ")
        self.btn_transp.setIcon(QtGui.QIcon("icons/transp.png"))
        self.btn_transp.setIconSize(QtCore.QSize(int(screen_height * 5.5/ 100), int(screen_height * 5.5 / 100)))
        self.btn_transp.setObjectName("btn_menu")
        self.btn_transp.clicked.connect(self.transp_button_clicked)   
        
        #========bouton selected===============
        self.menu_group = QtWidgets.QButtonGroup(MainWindow)
        self.menu_group.setExclusive(True)
        self.btn_home.setCheckable(True)
        self.btn_transp.setCheckable(True)

        self.menu_group.addButton(self.btn_home)  
        self.menu_group.addButton(self.btn_transp) 
        #=====================add layout menu=========================
        self.menu_layout = QtWidgets.QVBoxLayout(self.group_menu)
        self.menu_layout.setContentsMargins(10, 20, 10, 10)
        self.menu_layout.setSpacing(10)
        self.menu_layout.addWidget(self.btn_home) 
        self.menu_layout.addWidget(self.btn_transp)   
#=====================Functions Boutons=========================  
    #bouton home==========      
    def home_button_clicked(self):
        home_page = Home()
        self.pages.addWidget(home_page)
        self.pages.setCurrentWidget(home_page)   
    #bouton transporteurs========    
    def transp_button_clicked(self):
        trans_page = Transp() 
        self.pages.addWidget(trans_page)
        self.pages.setCurrentWidget(trans_page)    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    use_style(app)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())