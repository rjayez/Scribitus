# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Apr 08 10:25:14 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1447, 925)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/scribitus_burned.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxRules = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxRules.setGeometry(QtCore.QRect(760, 30, 521, 389))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRules.sizePolicy().hasHeightForWidth())
        self.groupBoxRules.setSizePolicy(sizePolicy)
        self.groupBoxRules.setMinimumSize(QtCore.QSize(521, 389))
        self.groupBoxRules.setAutoFillBackground(True)
        self.groupBoxRules.setFlat(False)
        self.groupBoxRules.setObjectName("groupBoxRules")
        self.radioDelete = QtGui.QRadioButton(self.groupBoxRules)
        self.radioDelete.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.radioDelete.setChecked(True)
        self.radioDelete.setObjectName("radioDelete")
        self.radioReplace = QtGui.QRadioButton(self.groupBoxRules)
        self.radioReplace.setGeometry(QtCore.QRect(30, 100, 82, 17))
        self.radioReplace.setObjectName("radioReplace")
        self.deleteText = QtGui.QLineEdit(self.groupBoxRules)
        self.deleteText.setGeometry(QtCore.QRect(130, 50, 351, 20))
        self.deleteText.setAcceptDrops(False)
        self.deleteText.setObjectName("deleteText")
        self.replaceTextFirst = QtGui.QLineEdit(self.groupBoxRules)
        self.replaceTextFirst.setGeometry(QtCore.QRect(130, 100, 351, 20))
        self.replaceTextFirst.setAcceptDrops(False)
        self.replaceTextFirst.setObjectName("replaceTextFirst")
        self.replaceTextBy = QtGui.QLineEdit(self.groupBoxRules)
        self.replaceTextBy.setGeometry(QtCore.QRect(130, 130, 351, 20))
        self.replaceTextBy.setAcceptDrops(False)
        self.replaceTextBy.setObjectName("replaceTextBy")
        self.label_2 = QtGui.QLabel(self.groupBoxRules)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtGui.QCheckBox(self.groupBoxRules)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(130, 20, 241, 17))
        self.checkBox.setObjectName("checkBox")
        self.radioAdd = QtGui.QRadioButton(self.groupBoxRules)
        self.radioAdd.setGeometry(QtCore.QRect(30, 190, 82, 17))
        self.radioAdd.setObjectName("radioAdd")
        self.listCouleur = QtGui.QComboBox(self.groupBoxRules)
        self.listCouleur.setGeometry(QtCore.QRect(130, 280, 351, 22))
        self.listCouleur.setObjectName("listCouleur")
        self.label_5 = QtGui.QLabel(self.groupBoxRules)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 47, 13))
        self.label_5.setObjectName("label_5")
        self.buttonRule = QtGui.QPushButton(self.groupBoxRules)
        self.buttonRule.setGeometry(QtCore.QRect(190, 320, 211, 23))
        self.buttonRule.setObjectName("buttonRule")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBoxRules)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 180, 371, 91))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
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
        self.groupBoxTableRule = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxTableRule.setGeometry(QtCore.QRect(20, 30, 711, 391))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxTableRule.sizePolicy().hasHeightForWidth())
        self.groupBoxTableRule.setSizePolicy(sizePolicy)
        self.groupBoxTableRule.setMinimumSize(QtCore.QSize(711, 391))
        self.groupBoxTableRule.setAutoFillBackground(True)
        self.groupBoxTableRule.setFlat(False)
        self.groupBoxTableRule.setObjectName("groupBoxTableRule")
        self.tableRules = QtGui.QTableWidget(self.groupBoxTableRule)
        self.tableRules.setGeometry(QtCore.QRect(10, 20, 611, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableRules.sizePolicy().hasHeightForWidth())
        self.tableRules.setSizePolicy(sizePolicy)
        self.tableRules.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableRules.setAcceptDrops(False)
        self.tableRules.setAutoFillBackground(False)
        self.tableRules.setStyleSheet("")
        self.tableRules.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableRules.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableRules.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableRules.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableRules.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableRules.setShowGrid(True)
        self.tableRules.setObjectName("tableRules")
        self.tableRules.setColumnCount(2)
        self.tableRules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableRules.setHorizontalHeaderItem(1, item)
        self.tableRules.horizontalHeader().setHighlightSections(False)
        self.tableRules.horizontalHeader().setStretchLastSection(True)
        self.tableRules.verticalHeader().setHighlightSections(True)
        self.btnDownRule = QtGui.QPushButton(self.groupBoxTableRule)
        self.btnDownRule.setEnabled(True)
        self.btnDownRule.setGeometry(QtCore.QRect(630, 130, 41, 31))
        self.btnDownRule.setMinimumSize(QtCore.QSize(41, 31))
        self.btnDownRule.setMaximumSize(QtCore.QSize(41, 31))
        self.btnDownRule.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/fleche_bas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDownRule.setIcon(icon1)
        self.btnDownRule.setObjectName("btnDownRule")
        self.btnUpRule = QtGui.QPushButton(self.groupBoxTableRule)
        self.btnUpRule.setEnabled(True)
        self.btnUpRule.setGeometry(QtCore.QRect(630, 90, 41, 31))
        self.btnUpRule.setMinimumSize(QtCore.QSize(41, 31))
        self.btnUpRule.setMaximumSize(QtCore.QSize(41, 31))
        self.btnUpRule.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/fleche_haut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpRule.setIcon(icon2)
        self.btnUpRule.setObjectName("btnUpRule")
        self.btnDeleteRule = QtGui.QPushButton(self.groupBoxTableRule)
        self.btnDeleteRule.setEnabled(True)
        self.btnDeleteRule.setGeometry(QtCore.QRect(630, 50, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteRule.sizePolicy().hasHeightForWidth())
        self.btnDeleteRule.setSizePolicy(sizePolicy)
        self.btnDeleteRule.setMinimumSize(QtCore.QSize(41, 31))
        self.btnDeleteRule.setMaximumSize(QtCore.QSize(41, 31))
        self.btnDeleteRule.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/moins-rouge-enlevez-icone-8984-32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btnDeleteRule.setIcon(icon3)
        self.btnDeleteRule.setObjectName("btnDeleteRule")
        self.groupBoxTableFile = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxTableFile.setGeometry(QtCore.QRect(20, 430, 1261, 321))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxTableFile.sizePolicy().hasHeightForWidth())
        self.groupBoxTableFile.setSizePolicy(sizePolicy)
        self.groupBoxTableFile.setMinimumSize(QtCore.QSize(699, 321))
        self.groupBoxTableFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBoxTableFile.setAutoFillBackground(True)
        self.groupBoxTableFile.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.groupBoxTableFile.setObjectName("groupBoxTableFile")
        self.tableFiles = QtGui.QTableWidget(self.groupBoxTableFile)
        self.tableFiles.setEnabled(True)
        self.tableFiles.setGeometry(QtCore.QRect(10, 20, 611, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableFiles.sizePolicy().hasHeightForWidth())
        self.tableFiles.setSizePolicy(sizePolicy)
        self.tableFiles.setMinimumSize(QtCore.QSize(611, 251))
        self.tableFiles.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableFiles.setAcceptDrops(False)
        self.tableFiles.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableFiles.setDragEnabled(True)
        self.tableFiles.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableFiles.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableFiles.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableFiles.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableFiles.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableFiles.setWordWrap(False)
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
        self.tableFiles.horizontalHeader().setDefaultSectionSize(250)
        self.tableFiles.horizontalHeader().setSortIndicatorShown(False)
        self.tableFiles.horizontalHeader().setStretchLastSection(False)
        self.btnDeleteFile = QtGui.QPushButton(self.groupBoxTableFile)
        self.btnDeleteFile.setEnabled(True)
        self.btnDeleteFile.setGeometry(QtCore.QRect(630, 50, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteFile.sizePolicy().hasHeightForWidth())
        self.btnDeleteFile.setSizePolicy(sizePolicy)
        self.btnDeleteFile.setMinimumSize(QtCore.QSize(41, 31))
        self.btnDeleteFile.setMaximumSize(QtCore.QSize(41, 31))
        self.btnDeleteFile.setText("")
        self.btnDeleteFile.setIcon(icon3)
        self.btnDeleteFile.setObjectName("btnDeleteFile")
        self.btnRename = QtGui.QPushButton(self.groupBoxTableFile)
        self.btnRename.setGeometry(QtCore.QRect(210, 280, 221, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.btnRename.sizePolicy().hasHeightForWidth())
        self.btnRename.setSizePolicy(sizePolicy)
        self.btnRename.setMinimumSize(QtCore.QSize(221, 23))
        self.btnRename.setMaximumSize(QtCore.QSize(221, 23))
        self.btnRename.setAutoFillBackground(False)
        self.btnRename.setFlat(False)
        self.btnRename.setObjectName("btnRename")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1447, 21))
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
        self.groupBoxRules.setTitle(
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
        self.groupBoxTableRule.setTitle(
            QtGui.QApplication.translate("MainWindow", "Liste régles", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Couleur", None, QtGui.QApplication.UnicodeUTF8))
        self.tableRules.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Régle", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxTableFile.setTitle(
            QtGui.QApplication.translate("MainWindow", "Liste fichiers", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.setToolTip(QtGui.QApplication.translate("MainWindow", "Glisser un/des fichier(s)", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("MainWindow", "Nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(1).setText(
            QtGui.QApplication.translate("MainWindow", "Nouveau nom fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFiles.horizontalHeaderItem(2).setText(
            QtGui.QApplication.translate("MainWindow", "Chemin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRename.setText(
            QtGui.QApplication.translate("MainWindow", "Renommer fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScribitus.setTitle(
            QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_Propos.setTitle(
            QtGui.QApplication.translate("MainWindow", "A Propos", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(
            QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
