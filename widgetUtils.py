# coding=utf-8
from PySide.QtCore import *
from PySide.QtGui import *


# Renvoie un QTextEdit avec tous les parametres souhaité pour l'interface
def createScribitusQTextEdit():
    textEdit = QTextEdit()
    textEdit.setFrameShape(QFrame.HLine)
    textEdit.setMidLineWidth(1)
    textEdit.setLineWrapMode(QTextEdit.NoWrap)
    textEdit.setTextInteractionFlags(Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse)
    textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    textEdit.setReadOnly(True)

    return textEdit


# Applique le formatage des surligneur sur un nom de fichier
def applySurligneur(nomFichier, listSurligneur):
    debutBalise = "<span style=\"background-color:%s;\">"
    finBalise = "</span>"

    nomAvecSurligneur = ""
    indexNom = 0

    if len(listSurligneur) is 0:
        return nomFichier

    for surligneur in listSurligneur:
        print "indexNom %d indexDebut %d indexFin %d" % (indexNom, surligneur.indexDebut, surligneur.indexFin)
        nomAvecSurligneur += nomFichier[indexNom:surligneur.indexDebut]
        nomAvecSurligneur += (debutBalise % surligneur.color.hex)
        nomAvecSurligneur += nomFichier[surligneur.indexDebut:surligneur.indexFin]
        nomAvecSurligneur += finBalise
        indexNom = surligneur.indexFin

    nomAvecSurligneur += nomFichier[indexNom:]
    return nomAvecSurligneur


# Renvoie un QTableWidgetItem avec un userData de set
def createTableItem(text, data):
    item = QTableWidgetItem(text)
    # Pour stocker des données dans la cellule du tableau
    # (Qt.UserRole sert à déterminer le type de data présent dans la cellule)
    item.setData(Qt.UserRole, data)
    return item


# Cree un message box Oui/Non
def createMessageBoxOuiNon(text, title):
    messageBox = QMessageBox()
    messageBox.setText(text)
    messageBox.setWindowTitle(title)
    messageBox.setIcon(QMessageBox.Question)
    messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    return messageBox


# Retourne la liste de tous les index des lignes selectionne
def getListRowIndex(table):
    selected = table.selectedIndexes()
    listLigne = []
    for index in selected:
        listLigne.append(index.row())

    listLigne = list(set(listLigne))  # Elimine les doublons
    return listLigne
