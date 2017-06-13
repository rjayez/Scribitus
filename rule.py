class TypeRule:
    def __init__(self):
        pass

    ADD = "add"
    REPLACE = "replace"
    DELETE = "delete"


class Color:
    hex = ""
    name = ""

    def __init__(self, name, hex):
        self.name = name
        self.hex = hex


class ColorRule:
    def __init__(self):
        pass

    RED = Color("Rouge", "#FF8080")
    GREEN = Color("Vert", "#80FF80")
    BLUE = Color("Bleu", "#80BFFF")
    YELLOW = Color("Jaune", "#FFFFB3")
    GREY = Color("Gris", "#CCCCCC")
    PINK = Color("Rose", "#FFB3FF")
    PURPLE = Color("Violet", "#BF80FF")

    colors = [RED, GREEN, BLUE, YELLOW, GREY, PINK, PURPLE]


class Rule:
    ruleType = ""
    position = 0
    elementAjout = ""
    elementSuppression = ""
    color = ColorRule.BLUE
    description = ""

    def __init__(self, ruleType, color, elementAjout, elementSuppression="", position=0):
        self.ruleType = ruleType
        self.color = color
        self.elementAjout = elementAjout
        self.elementSuppression = elementSuppression
        self.position = position
        self.description = self.getDescription()

    def getDescription(self):
        # sys.maxint
        typeDescription = {TypeRule.REPLACE: "Remplace %s par %s" % (self.elementSuppression, self.elementAjout),
                           TypeRule.DELETE: "Supprime %s" % self.elementSuppression,
                           TypeRule.ADD: "Ajout %s " % self.elementAjout}

        return typeDescription[self.ruleType]
