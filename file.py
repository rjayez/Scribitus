from os.path import basename
import re


class File:
    # path + name + extension give complete filepath
    path = ""
    name = ""
    extension = ""

    def __init__(self, filePath):
        self.path = filePath
        file = open(filePath)
        filename = basename(file.name)
        match = re.match("(\w+)(([\.]\w+)+)", filename)
        self.name = match.group(1)  # capture name without extension
        self.extension = match.group(2)  # capture only extension

    def getFilename(self):
        return self.name + self.extension
