from os.path import basename


class File:
    path = ""
    name = ""

    def __init__(self, filePath):
        self.path = filePath
        file = open(filePath)
        self.name = basename(file.name)
