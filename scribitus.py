# coding=utf-8

from PySide.QtCore import *
from PySide.QtGui import *

import widgetUtils
from file import *
from mainwindow import Ui_MainWindow
from rule import *
from widgetUtils import *
import sys
import os


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
        self.btnUpRule.clicked.connect(self.upRule)
        self.btnDownRule.clicked.connect(self.downRule)

    # Methodes pour toggle les radio selon quels champs des regles sont édités
    def toggleRadioDelete(self):
        self.radioDelete.setChecked(True)

    def toggleRadioAdd(self):
        self.radioAdd.setChecked(True)

    def toggleRadioReplace(self):
        self.radioReplace.setChecked(True)

    # Ajoute une regle
    def addRule(self):

        QToolTip.showText(self.mapToGlobal(self.deleteText.pos()), "coucou")

        # Create rule object
        selectedColor = self.listCouleur.itemData(self.listCouleur.currentIndex())

        # Recuperation des informations selon le radio selectionne
        rule = None
        if self.radioAdd.isChecked():
            position = 0
            if self.radioBegin.isChecked():
                position = 0
            if self.radioEnd.isChecked():
                position = sys.maxsize
            if self.radioPosition.isChecked():
                position = self.spinBoxPosition.value()
            rule = AddRule(selectedColor, self.addText.text(), position)

        if self.radioDelete.isChecked():
            rule = DeleteRule(selectedColor, self.deleteText.text())

        if self.radioReplace.isChecked():
            rule = ReplaceRule(selectedColor, self.replaceTextBy.text(), self.replaceTextFirst.text())


        self.listRules.append(rule)

        # Ajout ligne dans le tableau
        # textEdit = QTextEdit()
        # textEdit.append("cou<span style=\"background-color:#CCFFD9;\">co</span>u")

        rowIndex = self.tableRules.rowCount()
        self.tableRules.setRowCount(rowIndex + 1)

        # Colonne de couleur
        item = createTableItem(rule.color.name, rule)
        item.setBackground(QBrush(QColor(rule.color.hex)))

        self.tableRules.setItem(rowIndex, 0, item)
        self.tableRules.setItem(rowIndex, 1, createTableItem(rule.description, rule))
        # self.tableRules.setCellWidget(rowIndex, 1, textEdit)

        self.tableRules.resizeColumnsToContents()

        self.fillTableFile()

    # Suppression de règle avec message box de confirmation
    def deleteRule(self):
        listLigne = self.getListRowIndex()

        listLigne = list(set(listLigne))  # Elimine les doublons

        if len(listLigne) > 0:
            messageBox = createMessageBoxOuiNon("Etes vous sur de supprimer cette ligne ?", "Suppression")
            response = messageBox.exec_()
            if response == QMessageBox.Yes:
                # List à l'envers pour supprimer correctement les lignes du tableaux
                for indexRow in reversed(listLigne):
                    self.tableRules.removeRow(indexRow)
                    del self.listRules[indexRow]

    def upRule(self):

        selectedItem = self.tableRules.selectedItems()
        swapRow = True
        for item in selectedItem:
            # Switch d'item avec la ligne au dessus
            row = item.row()
            column = item.column()
            if row is not 0:
                tempItem = self.tableRules.takeItem(row - 1, column)
                tempItem2 = self.tableRules.takeItem(row, column)
                self.tableRules.setItem(row - 1, column, tempItem2)
                self.tableRules.setItem(row, column, tempItem)
                self.tableRules.selectRow(row - 1)

                if swapRow:
                    self.listRules[row - 1], self.listRules[row] = self.listRules[row], self.listRules[row - 1]  # Swap
                    swapRow = False

        self.fillTableFile()

    def downRule(self):
        selectedItem = self.tableRules.selectedItems()
        swapRow = True
        for item in selectedItem:
            # Switch d'item avec la ligne au dessus
            row = item.row()
            column = item.column()
            if row is not self.tableRules.rowCount() - 1:
                tempItem = self.tableRules.takeItem(row + 1, column)
                tempItem2 = self.tableRules.takeItem(row, column)
                self.tableRules.setItem(row + 1, column, tempItem2)
                self.tableRules.setItem(row, column, tempItem)
                self.tableRules.selectRow(row + 1)

                if swapRow:
                    self.listRules[row + 1], self.listRules[row] = self.listRules[row], self.listRules[row + 1]  # Swap
                    swapRow = False

        self.fillTableFile()

    def fillTableFile(self):
        # Reinitialisation du tableau
        self.tableFiles.clearContents()
        self.tableFiles.setRowCount(0)

        for file in self.listFiles:
            rowIndex = self.tableFiles.rowCount()
            self.tableFiles.setRowCount(rowIndex + 1)

            # Colonne chemin filepath
            self.tableFiles.setItem(rowIndex, 0, QTableWidgetItem(file.path))

            # Colonne ancien nom
            textEdit = widgetUtils.createScribitusQTextEdit()
            textEdit.append(file.getFilename())
            self.tableFiles.setCellWidget(rowIndex, 1, textEdit)

            # Colonne nouveau nom
            newName = self.applyRules(file.name)

            textEdit = widgetUtils.createScribitusQTextEdit()
            textEdit.append(newName + file.extension)
            self.tableFiles.setCellWidget(rowIndex, 2, textEdit)
            self.tableFiles.resizeColumnsToContents()

        self.tableFiles.clearFocus()

    # Applique la liste des régles sur le nom de fichier
    def applyRules(self, nomFichier):

        nouveauNom = nomFichier
        for rule in self.listRules:
            nouveauNom = rule.applyRule(nouveauNom)
            print(nouveauNom)

        return nouveauNom

    # Ajoute un fichier au tableau des fichiers
    def addFile(self, filePath):

        file = File(filePath)
        print(file.name)
        print(file.path)
        self.listFiles.append(file)
        # Rafraichir la liste de fichier avec le nouveau nom (Voir pour une méthode unitaire si les perfs suivent pas)
        self.fillTableFile()

    def deleteFile(self):
        selected = self.tableFiles.selectedIndexes()
        listLigne = []
        for index in selected:
            listLigne.append(index.row())

        listLigne = list(set(listLigne))  # Elimine les doublons

        if len(listLigne) > 0:
            messageBox = createMessageBoxOuiNon("Etes vous sur de supprimer cette/ces ligne(s) ?", "Suppression")
            response = messageBox.exec_()
            if response == QMessageBox.Yes:
                # List à l'envers pour supprimer correctement les lignes du tableaux
                for indexRow in reversed(listLigne):
                    self.tableFiles.removeRow(indexRow)
                    del self.listFiles[indexRow]

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
            allDragIsFile = True
            for url in event.mimeData().urls():
                if not os.path.isfile(url.toLocalFile()):
                    allDragIsFile = False

            if allDragIsFile:
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    # Gestion du drop
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if os.path.isfile(url.toLocalFile()):
                    self.addFile(url.toLocalFile())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
