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
