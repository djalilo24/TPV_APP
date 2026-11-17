from PyQt5 import QtCore, QtGui, QtWidgets
class Transp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.transp_ui()

    def transp_ui(self):
         
        self.group_transp  = QtWidgets.QVBoxLayout()
        self.add_transp = QtWidgets.QHBoxLayout()
        self.group_transp.addLayout(self.add_transp)
        self.group_search = QtWidgets.QHBoxLayout()
        self.group_transp.addLayout(self.group_search)
        self.group_table = QtWidgets.QHBoxLayout()
        self.group_transp.addLayout(self.group_table)
        #self.setObjectName("transp_page")
        #====================Bouton add transportor=========================
        self.add_transp_button = QtWidgets.QPushButton("Ajouter un nouveau transporteur| إظافة ناقل جديد")   
        self.add_transp_button.setIcon(QtGui.QIcon("icons/add.png"))
        self.add_transp_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_transp_button.setToolTip("  Ajouter un nouveau transporteur")
        self.add_transp_button.setIconSize(QtCore.QSize(28, 28))
        self.add_transp_button.setObjectName("simple_btn")
        #self.group_transp.addWidget(self.add_transp_button)        
        #self.add_transp_button.clicked.connect(self.form_fournisseur)
        self.group_transp.addSpacing(20)
        self.add_transp.addWidget(self.add_transp_button,alignment=QtCore.Qt.AlignHCenter)
        
        self.setLayout(self.group_transp)
        #===================comobox choix research===========================
        self.lable_search = QtWidgets.QLabel("البحث بواس0000طة",self)
        self.group_search.addWidget(self.lable_search,alignment=QtCore.Qt.AlignRight)
        self.search_transp = QtWidgets.QComboBox(self)
        self.search_transp.addItems(["","choix1","choix2"])
        self.search_transp.setMinimumWidth(200)
        self.search_transp.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred)
        self.group_transp.addSpacing(25)       
        self.group_search.addWidget(self.search_transp,alignment=QtCore.Qt.AlignRight)
        self.group_transp.addStretch()

