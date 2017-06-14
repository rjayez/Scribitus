from PySide.QtCore import *
from PySide.QtGui import *

import widgetUtils
from file import *
from mainwindow import Ui_MainWindow
from rule import *
from widgetUtils import *
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    listRules = []
    listFiles = []

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.remplirListeCouleur()
        self.assignWidgets()
        self.show()

    def assignWidgets(self):
        self.buttonRule.clicked.connect(self.addRule)
        self.deleteText.textEdited.connect(self.toggleRadioDelete)
        self.replaceTextBy.textEdited.connect(self.toggleRadioReplace)
        self.replaceTextFirst.textEdited.connect(self.toggleRadioReplace)
        self.addText.textEdited.connect(self.toggleRadioAdd)
        self.btnDeleteFile.clicked.connect(self.deleteFile)
        self.btnDeleteRule.clicked.connect(self.deleteRule)

    # Methodes pour toggle les radio selon quels champs des regles sont édités
    def toggleRadioDelete(self):
        self.radioDelete.setChecked(True)

    def toggleRadioAdd(self):
        self.radioAdd.setChecked(True)

    def toggleRadioReplace(self):
        self.radioReplace.setChecked(True)

    # Ajoute une regle
    def addRule(self):
        rowIndex = self.tableRules.rowCount()
        self.tableRules.setRowCount(rowIndex + 1)

        # Create rule object
        selectedColor = self.listCouleur.itemData(self.listCouleur.currentIndex())

        # Recuperation des informations selon le radio selectionne
        ruleType = ""
        position = 0
        elementAjout = ""
        elementSuppression = ""
        if self.radioAdd.isChecked():
            ruleType = TypeRule.ADD
            elementAjout = self.addText.text()

        if self.radioDelete.isChecked():
            ruleType = TypeRule.DELETE
            elementSuppression = self.deleteText.text()

        if self.radioReplace.isChecked():
            ruleType = TypeRule.REPLACE
            elementSuppression = self.replaceTextFirst.text()
            elementAjout = self.replaceTextBy.text()

        rule = Rule(ruleType, selectedColor, elementAjout, elementSuppression, position)
        self.listRules.append(rule)

        # Ajout ligne dans le tableau
        # textEdit = QTextEdit()
        # textEdit.append("cou<span style=\"background-color:#CCFFD9;\">co</span>u")

        # Colonne de couleur
        item = QTableWidgetItem()
        item.setBackground(QBrush(QColor(rule.color.hex)))
        self.tableRules.setItem(rowIndex, 0, item)
        self.tableRules.setItem(rowIndex, 1, QTableWidgetItem(rule.description))
        # self.tableRules.setCellWidget(rowIndex, 1, textEdit)

        self.tableRules.resizeColumnsToContents()

    def deleteRule(self):
        selected = self.tableRules.selectedIndexes()
        print("coucou")


    # Ajoute un fichier au tableau des fichiers
    def addFile(self, filePath):

        file = File(filePath)
        self.listFiles.append(file)

        rowIndex = self.tableFiles.rowCount()
        self.tableFiles.setRowCount(rowIndex + 1)

        # Colonne chemin filepath
        self.tableFiles.setItem(rowIndex, 0, QTableWidgetItem(filePath))

        # Colonne ancien nom
        textEdit = widgetUtils.createScribitusQTextEdit()
        textEdit.append(file.name)
        self.tableFiles.setCellWidget(rowIndex, 1, textEdit)

        # Colonne nouveau nom
        textEdit = QTextEdit()
        textEdit.append(file.newName)
        self.tableFiles.setCellWidget(rowIndex, 2, textEdit)

        self.tableFiles.resizeColumnsToContents()
        self.tableFiles.clearFocus()

    def deleteFile(self):
        selected = self.tableFiles.selectedIndexes()

    # Remplir liste de couleurs
    def remplirListeCouleur(self):

        model = self.listCouleur.model()
        for color in ColorRule.colors:
            item = QStandardItem(color.name)
            item.setBackground(QBrush(QColor(color.hex)))
            item.setData(color, Qt.UserRole)
            model.appendRow(item)

    # Gestion du drag & drop
    def dragEnterEvent(self, event):
        # Acception du type de drag pour les fichiers (hasUrls)
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # Gestion du drop
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addFile(url.toLocalFile())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
