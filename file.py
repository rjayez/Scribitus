from os.path import basename
import re
from surligneur import *


class File:
    # path + name + extension give complete filepath
    path = ""
    name = ""
    extension = ""
    newName = ""
    # Les surligneurs definissent l'affichage dans le tableau de l'actuel et nouveau nom
    listSurligneurNomActuel = []
    listSurligneurNomNouveau = []

    def __init__(self, filePath):
        self.path = filePath
        file = open(filePath)
        filename = basename(file.name)
        match = re.match("(\w+)(([\.]\w+)+)", filename)
        self.name = match.group(1)  # capture name without extension
        self.extension = match.group(2)  # capture only extension

    # Renvoie le nom du fichier
    def getFilename(self):
        return self.name + self.extension

    #
    def creerListSurligneur(self, listRegle):
        name = self.name
        newName = name
        for rule in listRegle:
            newName = rule.applyRule(newName)
            for match in re.finditer(rule.elementAjout, newName):
                surligneur = Surligneur(match.start(), match.end(), rule.color)
                insertSurligneur(self.listSurligneurNomNouveau, surligneur)
            for match in re.finditer(rule.elementSuppression, newName):
                surligneur = Surligneur(match.start(), match.end(), rule.color)
                insertSurligneur(self.listSurligneurNomActuel, surligneur)
