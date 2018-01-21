# coding=utf-8

import sys


class TypeRule:
    def __init__(self):
        pass

    ADD = "add"
    ADD_END = "add_end"
    REPLACE = "replace"
    DELETE = "delete"


class Color:
    hex = ""
    name = ""

    def __init__(self, name, hexColor):
        self.name = name
        self.hex = hexColor


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


# Couleur regex101 : vert #c6e99d rouge #f5aba5
#  orange #ffbf6d
# bleu #c1cbeb
# vert pale #d7fde3
# vert fluo #e3ffac
# rose violet #e88dee
# vert caci #cfdd67
# rose #ffacc0
# bleu #84d6ee
# bleu fonce #c1cbeb
# bleu cyan #84d6ee
# gris bleu #c1cbeb
###


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
                           TypeRule.ADD: "Ajoute %s " % self.elementAjout,
                           TypeRule.ADD_END: u"Ajoute %s à la fin" % self.elementAjout}

        return typeDescription[self.ruleType]

    def applyRule(self, nomFichier):
        pass


class DeleteRule(Rule):
    def __init__(self, color, elementSuppression):
        Rule.__init__(self, TypeRule.DELETE, color, "", elementSuppression)

    def applyRule(self, nomFichier):
        return str(nomFichier).replace(self.elementSuppression, '')


class AddRule(Rule):
    def __init__(self, color, elementAjout, position=0):
        Rule.__init__(self, TypeRule.ADD, color, elementAjout, position=position)

    def applyRule(self, nomFichier):
        return nomFichier[:self.position] + self.elementAjout + nomFichier[self.position:]


class AddEndRule(Rule):
    def __init__(self, color, elementAjout):
        Rule.__init__(self, TypeRule.ADD_END, color, elementAjout, position=sys.maxint)

    def applyRule(self, nomFichier):
        return nomFichier + self.elementAjout


class ReplaceRule(Rule):
    def __init__(self, color, elementAjout, elementSuppression):
        Rule.__init__(self, TypeRule.REPLACE, color, elementAjout, elementSuppression)

    def applyRule(self, nomFichier):
        return nomFichier.replace(self.elementSuppression, self.elementAjout)
