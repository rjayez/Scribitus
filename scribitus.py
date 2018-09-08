#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from PySide.QtCore import *
from PySide.QtGui import *

import surligneur
import widgetUtils
from KeyEnum import *
from file import *
from mainwindow import Ui_MainWindow
from rule import *


class MainWindow(QMainWindow, Ui_MainWindow):
    listRules = [
        # ReplaceRule(color=ColorRule.PINK, elementAjout="1", elementSuppression="a"),
        # ReplaceRule(color=ColorRule.GREY, elementAjout="2", elementSuppression="b"),
        # ReplaceRule(color=ColorRule.RED, elementAjout="3", elementSuppression="c"),
        # ReplaceRule(color=ColorRule.BLUE, elementAjout="tt", elementSuppression="123")
        DeleteRule(color=ColorRule.BLUE, elementSuppression="3o")
                 ]
    listFiles = [
        # File("Resources/Test/ttd3o.txt"),
        File("Resources/Test/tete3o3o.txt"),
        # File("Resources/Test/te1zertyuiop.txt"),
        # File("Resources/Test/tetetete.txt")
    ]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.remplirListeCouleur()
        self.assignWidgets()
        self.configureWidgets()
        self.show()

        # Initialisation de la liste des fichiers et rules pour les tests
        self.fillTableFile()
        self.fillTableRule()
        self.tableFiles.resizeColumnsToContents()

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
        self.btnRename.clicked.connect(self.renameFile)

    # Paramètre les layouts pour l'interface
    def configureWidgets(self):
        # Layout pour l'écran
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.groupBoxTableRule, 0, 0)
        grid_layout.addWidget(self.groupBoxRules, 0, 1)
        grid_layout.addWidget(self.groupBoxTableFile, 1, 0, 1, 2)
        self.centralwidget.setLayout(grid_layout)

        # Layout pour la liste des règles
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.tableRules, 0, 0, 5, 1)
        grid_layout.addWidget(self.btnDeleteRule, 0, 1)
        grid_layout.addWidget(self.btnUpRule, 1, 1)
        grid_layout.addWidget(self.btnDownRule, 2, 1)
        grid_layout.setRowStretch(0, 100)
        self.groupBoxTableRule.setLayout(grid_layout)

        # Layout pour la liste des fichiers
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.tableFiles, 0, 0, 2, 1)
        grid_layout.addWidget(self.btnDeleteFile, 0, 1)
        grid_layout.addWidget(self.btnRename, 2, 0, 1, 2, Qt.AlignHCenter)
        self.groupBoxTableFile.setLayout(grid_layout)

        self.tableRules.installEventFilter(self)
        self.tableFiles.installEventFilter(self)

    # Methodes pour toggle les radio selon quels champs des regles sont édités
    def toggleRadioDelete(self):
        self.radioDelete.setChecked(True)

    def toggleRadioAdd(self):
        self.radioAdd.setChecked(True)

    def toggleRadioReplace(self):
        self.radioReplace.setChecked(True)

    # Ajoute une regle
    def addRule(self):

        # QToolTip.showText(self.mapToGlobal(self.deleteText.pos()), "coucou")

        # Create rule object
        current_index = self.listCouleur.currentIndex()
        selectedColor = self.listCouleur.itemData(current_index)
        # Changement de couleur automatique à chaque nouvelle règle
        if self.listCouleur.count() is current_index + 1:
            self.listCouleur.setCurrentIndex(0)
        else:
            self.listCouleur.setCurrentIndex(current_index + 1)

        # Recuperation des informations selon le radio selectionne
        rule = None
        if self.radioAdd.isChecked():
            position = 0
            if self.radioBegin.isChecked():
                position = 0
            if self.radioPosition.isChecked():
                position = self.spinBoxPosition.value()
            rule = AddRule(selectedColor, self.addText.text(), position)

            # Si c'est un ajout à la fin, alors création d'un type de régle spécifique
            if self.radioEnd.isChecked():
                rule = AddEndRule(selectedColor, self.addText.text())

        if self.radioDelete.isChecked():
            rule = DeleteRule(selectedColor, self.deleteText.text())

        if self.radioReplace.isChecked():
            rule = ReplaceRule(selectedColor, self.replaceTextBy.text(), self.replaceTextFirst.text())

        self.listRules.append(rule)

        # Affiche la modification des régles dans l'interface
        self.fillTableRule()
        self.fillTableFile()

    # Suppression de règle avec message box de confirmation
    def deleteRule(self):
        listLigne = widgetUtils.getListRowIndex(self.tableRules)

        listLigne = list(set(listLigne))  # Elimine les doublons

        if len(listLigne) > 0:
            messageBox = widgetUtils.createMessageBoxOuiNon("Etes vous sur de supprimer cette ligne ?", "Suppression")
            response = messageBox.exec_()
            if response == QMessageBox.Yes:
                # List à l'envers pour supprimer correctement les lignes du tableaux
                for indexRow in reversed(listLigne):
                    self.tableRules.removeRow(indexRow)
                    del self.listRules[indexRow]

        self.fillTableFile()

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

    # Methode pour mettre a jour la liste des fichiers avec l'application des regles
    def fillTableRule(self):
        # Reinitialisation du tableau
        self.tableRules.clearContents()
        self.tableRules.setRowCount(0)

        for rule in self.listRules:
            # Ajout ligne dans le tableau
            rowIndex = self.tableRules.rowCount()
            self.tableRules.setRowCount(rowIndex + 1)

            # Colonne de couleur
            item = widgetUtils.createTableItem(rule.color.name, rule)
            item.setBackground(QBrush(QColor(rule.color.hex)))

            self.tableRules.setItem(rowIndex, 0, item)
            self.tableRules.setItem(rowIndex, 1, widgetUtils.createTableItem(rule.description, rule))
            # self.tableRules.setCellWidget(rowIndex, 1, textEdit)

        self.tableRules.resizeColumnsToContents()

    # Methode pour mettre a jour la liste des fichiers avec l'application des regles
    def fillTableFile(self):
        # Reinitialisation du tableau
        self.tableFiles.clearContents()
        self.tableFiles.setRowCount(0)

        for file in self.listFiles:
            rowIndex = self.tableFiles.rowCount()
            self.tableFiles.setRowCount(rowIndex + 1)

            listSurligneurNomActuel, listSurligneurNomNouveau = surligneur.creerListSurligneur(file.name,
                                                                                               self.listRules)

            # Colonne ancien nom
            oldNameColored = widgetUtils.applySurligneur(file.name, listSurligneurNomActuel)
            textEdit = widgetUtils.createScribitusQTextEdit()
            textEdit.append(oldNameColored + file.extension)
            self.tableFiles.setCellWidget(rowIndex, 0, textEdit)

            # Colonne nouveau nom
            file.newName = self.applyRules(file.name)

            newNameColored = widgetUtils.applySurligneur(file.newName, listSurligneurNomNouveau)
            textEdit = widgetUtils.createScribitusQTextEdit()
            textEdit.append(newNameColored + file.extension)
            self.tableFiles.setCellWidget(rowIndex, 1, textEdit)

            # Colonne chemin filepath
            self.tableFiles.setItem(rowIndex, 2, QTableWidgetItem(file.path))

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
            messageBox = widgetUtils.createMessageBoxOuiNon("Etes vous sur de supprimer cette/ces ligne(s) ?",
                                                            "Suppression")
            response = messageBox.exec_()
            if response == QMessageBox.Yes:
                # List à l'envers pour supprimer correctement les lignes du tableaux
                for indexRow in reversed(listLigne):
                    self.tableFiles.removeRow(indexRow)
                    del self.listFiles[indexRow]

    def renameFile(self):
        messageBox = widgetUtils.createMessageBoxOuiNon(
            u"Etes vous sur de renommer les fichiers avec les régles défini ?",
            "Renommage")
        response = messageBox.exec_()
        if response == QMessageBox.Yes:
            for file in self.listFiles:
                print (file.dirpath + file.getFilename())
                print (file.dirpath + file.getNewFilename())
                os.rename(file.dirpath + "/" + file.getFilename(),
                          file.dirpath + "/" + file.getNewFilename())
                # update file object
                file.path = file.dirpath + "/" + file.getNewFilename()
                file.name = file.newName
        self.fillTableFile()

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
                typedUrl = QUrl(url)
                if not (os.path.isfile(url.toLocalFile()) or os.path.isdir(url.toLocalFile())):
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
                if os.path.isfile(url.toLocalFile()) or os.path.isdir(url.toLocalFile()):
                    self.addFile(url.toLocalFile())

    def focusInEvent(self, event):
        self.tableRules.clearSelection()
        self.tableFiles.clearSelection()

    def eventFilter(self, widget, event):

        if event.type() is QEvent.KeyPress and widget is self.tableRules:
            if event.key() == KeyEnum.KEY_DELETE:
                self.deleteRule()

        if event.type() is QEvent.KeyPress and widget is self.tableFiles:
            if event.key() == KeyEnum.KEY_DELETE:
                self.deleteFile()

        return QWidget.eventFilter(self, widget, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
