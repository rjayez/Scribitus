# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Jun 13 21:00:05 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 871)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableFiles = QtGui.QTableWidget(self.centralwidget)
        self.tableFiles.setGeometry(QtCore.QRect(20, 350, 611, 192))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableFiles.sizePolicy().hasHeightForWidth())
        self.tableFiles.setSizePolicy(sizePolicy)
        self.tableFiles.setAcceptDrops(False)
        self.tableFiles.setDragEnabled(True)
        self.tableFiles.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableFiles.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableFiles.setObjectName("tableFiles")
        self.tableFiles.setColumnCount(3)
        self.tableFiles.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableFiles.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableFiles.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableFiles.setHorizontalHeaderItem(2, item)
        self.tableFiles.horizontalHeader().setCascadingSectionResizes(False)
        self.tableFiles.horizontalHeader().setDefaultSectionSize(150)
        self.tableRules = QtGui.QTableWidget(self.centralwidget)
        self.tableRules.setGeometry(QtCore.QRect(20, 100, 611, 192))
        self.tableRules.setAcceptDrops(False)
        self.tableRules.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableRules.setObjectName("tableRules")
        self.tableRules.setColumnCount(2)
        self.tableRules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(1, item)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 70, 101, 16))
        self.label.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(720, 30, 551, 531))
        self.groupBox.setObjectName("groupBox")
        self.radioDelete = QtGui.QRadioButton(self.groupBox)
        self.radioDelete.setGeometry(QtCore.QRect(30, 160, 82, 17))
        self.radioDelete.setObjectName("radioDelete")
        self.radioReplace = QtGui.QRadioButton(self.groupBox)
        self.radioReplace.setGeometry(QtCore.QRect(30, 210, 82, 17))
        self.radioReplace.setObjectName("radioReplace")
        self.deleteText = QtGui.QLineEdit(self.groupBox)
        self.deleteText.setGeometry(QtCore.QRect(130, 160, 351, 20))
        self.deleteText.setObjectName("deleteText")
        self.replaceTextFirst = QtGui.QLineEdit(self.groupBox)
        self.replaceTextFirst.setGeometry(QtCore.QRect(130, 210, 351, 20))
        self.replaceTextFirst.setObjectName("replaceTextFirst")
        self.replaceTextBy = QtGui.QLineEdit(self.groupBox)
        self.replaceTextBy.setGeometry(QtCore.QRect(130, 240, 351, 20))
        self.replaceTextBy.setObjectName("replaceTextBy")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 47, 13))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(150, 70, 241, 17))
        self.checkBox.setObjectName("checkBox")
        self.radioAdd = QtGui.QRadioButton(self.groupBox)
        self.radioAdd.setGeometry(QtCore.QRect(30, 310, 82, 17))
        self.radioAdd.setObjectName("radioAdd")
        self.addText = QtGui.QLineEdit(self.groupBox)
        self.addText.setGeometry(QtCore.QRect(130, 310, 351, 20))
        self.addText.setObjectName("addText")
        self.radioBegin = QtGui.QRadioButton(self.groupBox)
        self.radioBegin.setGeometry(QtCore.QRect(130, 340, 82, 17))
        self.radioBegin.setObjectName("radioBegin")
        self.radioEnd = QtGui.QRadioButton(self.groupBox)
        self.radioEnd.setGeometry(QtCore.QRect(230, 340, 82, 17))
        self.radioEnd.setObjectName("radioEnd")
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(360, 340, 42, 20))
        self.spinBox.setObjectName("spinBox")
        self.listCouleur = QtGui.QComboBox(self.groupBox)
        self.listCouleur.setGeometry(QtCore.QRect(130, 410, 161, 22))
        self.listCouleur.setObjectName("listCouleur")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 410, 47, 13))
        self.label_5.setObjectName("label_5")
        self.buttonRule = QtGui.QPushButton(self.groupBox)
        self.buttonRule.setGeometry(QtCore.QRect(140, 470, 211, 23))
        self.buttonRule.setObjectName("buttonRule")
        self.radioPosition = QtGui.QRadioButton(self.groupBox)
        self.radioPosition.setGeometry(QtCore.QRect(290, 340, 71, 17))
        self.radioPosition.setObjectName("radioPosition")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 110, 41, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 360, 41, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 160, 41, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 200, 41, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 21))
        self.menubar.setObjectName("menubar")
        self.menuScribitus = QtGui.QMenu(self.menubar)
        self.menuScribitus.setObjectName("menuScribitus")
        self.menuA_Propos = QtGui.QMenu(self.menubar)
        self.menuA_Propos.setObjectName("menuA_Propos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuScribitus.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuScribitus.menuAction())
        self.menubar.addAction(self.menuA_Propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.setToolTip(QtGui.QApplication.translate("MainWindow", "Glisser un/des fichier(s)", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Chemin", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(2).setText(
            QtGui.QApplication.translate("MainWindow", "Nouveau nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Couleur", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Régle", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("MainWindow", "Liste régles", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(
            QtGui.QApplication.translate("MainWindow", "Régles", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDelete.setText(
            QtGui.QApplication.translate("MainWindow", "Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.radioReplace.setText(
            QtGui.QApplication.translate("MainWindow", "Remplacer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "par", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Accepter Regex (Expression réguliére)", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.radioAdd.setText(
            QtGui.QApplication.translate("MainWindow", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
        self.radioBegin.setText(
            QtGui.QApplication.translate("MainWindow", "Début", None, QtGui.QApplication.UnicodeUTF8))
        self.radioEnd.setText(QtGui.QApplication.translate("MainWindow", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(
            QtGui.QApplication.translate("MainWindow", "Couleur", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRule.setText(
            QtGui.QApplication.translate("MainWindow", "Ajouter régle", None, QtGui.QApplication.UnicodeUTF8))
        self.radioPosition.setText(
            QtGui.QApplication.translate("MainWindow", "position", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "^", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(
            QtGui.QApplication.translate("MainWindow", "\\/", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScribitus.setTitle(
            QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_Propos.setTitle(
            QtGui.QApplication.translate("MainWindow", "A Propos", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(
            QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
