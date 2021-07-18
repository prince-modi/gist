
from PyQt5 import QtCore, QtWidgets
import sys


class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(317, 370)
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(110, 50, 84, 32))
        self.btnSearch.setObjectName("btnSearch")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 20, 234, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.searchBar = QtWidgets.QLineEdit(self.splitter)
        self.searchBar.setObjectName("searchBar")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(30, 89, 256, 221))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter_2)
        self.textBrowser.setObjectName("textBrowser")
        self.op_Label = QtWidgets.QLabel(self.splitter_2)
        self.op_Label.setObjectName("op_Label")
        mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        mainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWin)
        self.statusbar.setObjectName("statusbar")
        mainWin.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(mainWin)
        self.actionNew.setObjectName("actionNew")
        self.actionSave_Output = QtWidgets.QAction(mainWin)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionExit = QtWidgets.QAction(mainWin)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave_Output)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "Smri"))
        self.btnSearch.setText(_translate("mainWin", "Search"))
        self.label.setText(_translate("mainWin", "Enter Video Name"))
        self.op_Label.setText(_translate("mainWin", "TextLabel"))
        self.menuFile.setTitle(_translate("mainWin", "File"))
        self.actionNew.setText(_translate("mainWin", "New"))
        self.actionSave_Output.setText(_translate("mainWin", "Save Output"))
        self.actionExit.setText(_translate("mainWin", "Exit"))

    def btnclk(self):
        self.btnSearch.clicked.connect(self.btc)

    def btc(self):
        self.btnSearch.setText("mainWin", "Plejsgkhskdjfghsjdg")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWin()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
