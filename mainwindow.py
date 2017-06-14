# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jun 14 17:12:38 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 673)
        MainWindow.setMouseTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/scribitus_burned.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(720, 10, 511, 491))
        self.groupBox.setObjectName("groupBox")
        self.radioDelete = QtGui.QRadioButton(self.groupBox)
        self.radioDelete.setGeometry(QtCore.QRect(30, 70, 82, 17))
        self.radioDelete.setChecked(True)
        self.radioDelete.setObjectName("radioDelete")
        self.radioReplace = QtGui.QRadioButton(self.groupBox)
        self.radioReplace.setGeometry(QtCore.QRect(30, 120, 82, 17))
        self.radioReplace.setObjectName("radioReplace")
        self.deleteText = QtGui.QLineEdit(self.groupBox)
        self.deleteText.setGeometry(QtCore.QRect(130, 70, 351, 20))
        self.deleteText.setAcceptDrops(False)
        self.deleteText.setObjectName("deleteText")
        self.replaceTextFirst = QtGui.QLineEdit(self.groupBox)
        self.replaceTextFirst.setGeometry(QtCore.QRect(130, 120, 351, 20))
        self.replaceTextFirst.setAcceptDrops(False)
        self.replaceTextFirst.setObjectName("replaceTextFirst")
        self.replaceTextBy = QtGui.QLineEdit(self.groupBox)
        self.replaceTextBy.setGeometry(QtCore.QRect(130, 150, 351, 20))
        self.replaceTextBy.setAcceptDrops(False)
        self.replaceTextBy.setObjectName("replaceTextBy")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(140, 30, 241, 17))
        self.checkBox.setObjectName("checkBox")
        self.radioAdd = QtGui.QRadioButton(self.groupBox)
        self.radioAdd.setGeometry(QtCore.QRect(30, 210, 82, 17))
        self.radioAdd.setObjectName("radioAdd")
        self.listCouleur = QtGui.QComboBox(self.groupBox)
        self.listCouleur.setGeometry(QtCore.QRect(120, 300, 361, 22))
        self.listCouleur.setObjectName("listCouleur")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 47, 13))
        self.label_5.setObjectName("label_5")
        self.buttonRule = QtGui.QPushButton(self.groupBox)
        self.buttonRule.setGeometry(QtCore.QRect(120, 430, 211, 23))
        self.buttonRule.setObjectName("buttonRule")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 200, 371, 91))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBoxPosition = QtGui.QSpinBox(self.groupBox_2)
        self.spinBoxPosition.setGeometry(QtCore.QRect(250, 40, 42, 20))
        self.spinBoxPosition.setObjectName("spinBoxPosition")
        self.radioPosition = QtGui.QRadioButton(self.groupBox_2)
        self.radioPosition.setGeometry(QtCore.QRect(180, 40, 71, 17))
        self.radioPosition.setObjectName("radioPosition")
        self.addText = QtGui.QLineEdit(self.groupBox_2)
        self.addText.setGeometry(QtCore.QRect(10, 10, 351, 20))
        self.addText.setAcceptDrops(False)
        self.addText.setObjectName("addText")
        self.radioEnd = QtGui.QRadioButton(self.groupBox_2)
        self.radioEnd.setGeometry(QtCore.QRect(100, 40, 82, 17))
        self.radioEnd.setObjectName("radioEnd")
        self.radioBegin = QtGui.QRadioButton(self.groupBox_2)
        self.radioBegin.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioBegin.setChecked(True)
        self.radioBegin.setObjectName("radioBegin")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 681, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableFiles = QtGui.QTableWidget(self.groupBox_3)
        self.tableFiles.setEnabled(True)
        self.tableFiles.setGeometry(QtCore.QRect(10, 20, 611, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableFiles.sizePolicy().hasHeightForWidth())
        self.tableFiles.setSizePolicy(sizePolicy)
        self.tableFiles.setMinimumSize(QtCore.QSize(611, 251))
        self.tableFiles.setMaximumSize(QtCore.QSize(16777215, 251))
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
        self.btnDeleteFile = QtGui.QPushButton(self.groupBox_3)
        self.btnDeleteFile.setEnabled(True)
        self.btnDeleteFile.setGeometry(QtCore.QRect(630, 50, 41, 31))
        self.btnDeleteFile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/moins-rouge-enlevez-icone-8984-32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnDeleteFile.setIcon(icon1)
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 681, 201))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableRules = QtGui.QTableWidget(self.groupBox_5)
        self.tableRules.setGeometry(QtCore.QRect(10, 20, 611, 171))
        self.tableRules.setAcceptDrops(False)
        self.tableRules.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableRules.setObjectName("tableRules")
        self.tableRules.setColumnCount(2)
        self.tableRules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(1, item)
        self.btnDownRule = QtGui.QPushButton(self.groupBox_5)
        self.btnDownRule.setEnabled(True)
        self.btnDownRule.setGeometry(QtCore.QRect(630, 130, 41, 31))
        self.btnDownRule.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/fleche_bas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDownRule.setIcon(icon2)
        self.btnDownRule.setObjectName("btnDownRule")
        self.btnUpRule = QtGui.QPushButton(self.groupBox_5)
        self.btnUpRule.setEnabled(True)
        self.btnUpRule.setGeometry(QtCore.QRect(630, 90, 41, 31))
        self.btnUpRule.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/fleche_haut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpRule.setIcon(icon3)
        self.btnUpRule.setObjectName("btnUpRule")
        self.btnDeleteRule = QtGui.QPushButton(self.groupBox_5)
        self.btnDeleteRule.setEnabled(True)
        self.btnDeleteRule.setGeometry(QtCore.QRect(630, 50, 41, 31))
        self.btnDeleteRule.setText("")
        self.btnDeleteRule.setIcon(icon1)
        self.btnDeleteRule.setObjectName("btnDeleteRule")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 21))
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
        QtCore.QObject.connect(self.spinBoxPosition, QtCore.SIGNAL("valueChanged(QString)"), self.radioPosition.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "Scribitus", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_5.setText(
            QtGui.QApplication.translate("MainWindow", "Couleur", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonRule.setText(
            QtGui.QApplication.translate("MainWindow", "Ajouter régle", None, QtGui.QApplication.UnicodeUTF8))
        self.radioPosition.setText(
            QtGui.QApplication.translate("MainWindow", "position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioEnd.setText(QtGui.QApplication.translate("MainWindow", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.radioBegin.setText(
            QtGui.QApplication.translate("MainWindow", "Début", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(
            QtGui.QApplication.translate("MainWindow", "Liste fichiers", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.setToolTip(QtGui.QApplication.translate("MainWindow", "Glisser un/des fichier(s)", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Chemin", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(2).setText(
            QtGui.QApplication.translate("MainWindow", "Nouveau nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(
            QtGui.QApplication.translate("MainWindow", "Liste régles", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Couleur", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Régle", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScribitus.setTitle(
            QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_Propos.setTitle(
            QtGui.QApplication.translate("MainWindow", "A Propos", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(
            QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
