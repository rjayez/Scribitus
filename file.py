# coding=utf-8
from os.path import basename, dirname
import re


class File:
    # path + name + extension give complete filepath
    path = ""
    name = ""
    extension = ""
    newName = ""
    dirpath = ""


    def __init__(self, filePath):
        self.path = filePath
        file = open(filePath)
        filename = basename(file.name)
        match = re.match("(\w+)(([\.]\w+)+)", filename)
        self.name = match.group(1)  # capture name without extension
        self.newName = match.group(1)
        self.extension = match.group(2)  # capture only extension
        self.dirpath = dirname(filePath)

    # Renvoie le nom du fichier
    def getFilename(self):
        return self.name + self.extension

    def getNewFilename(self):
        return self.newName + self.extension
