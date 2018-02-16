# coding=utf-8

import re
from rule import TypeRule


class Surligneur:
    indexDebut = 0
    indexFin = 0
    color = None

    def __init__(self, debut, fin, color):
        self.indexDebut = debut
        self.indexFin = fin
        self.color = color

    def toString(self):
        return "Debut: %d Fin: %d Color: %s" % (self.indexDebut, self.indexFin, self.color.name)


# Cree la liste des surligneurs a appliquer dans le tableau
def creerListSurligneur(name, listRegle):
    # Reset des listes
    listSurligneurNomNouveau = []
    listSurligneurNomActuel = []

    newName = name

    for rule in listRegle:

        if rule.ruleType is TypeRule.REPLACE:
            if newName is not rule.applyRule(newName):
                newName = rule.applyRule(newName)
                listSurligneurNomActuel, listSurligneurNomNouveau = creerSurligneurReplace(rule,
                                                                                           listSurligneurNomActuel,
                                                                                           listSurligneurNomNouveau,
                                                                                           newName)
        elif rule.ruleType is TypeRule.ADD:
            # Ajout => surligneur pour le nouveau nom

            # Si la position depasse la longueur de nom alors appliquer les actions d'une régle ADD_END
            if rule.position > len(newName):
                surligneur = Surligneur(len(newName), len(newName) + len(rule.elementAjout), rule.color)
                listSurligneurNomNouveau.append(surligneur)
                newName = rule.applyRule(newName)
            else:
                surligneur = Surligneur(rule.position, rule.position + len(rule.elementAjout), rule.color)
                newName = rule.applyRule(newName)
                listSurligneurNomNouveau = insertSurligneurAjout(listSurligneurNomNouveau, surligneur)

        elif rule.ruleType is TypeRule.ADD_END:

            # Ajout => surligneur pour le nouveau nom
            surligneur = Surligneur(len(newName), len(newName) + len(rule.elementAjout), rule.color)
            newName = rule.applyRule(newName)
            listSurligneurNomNouveau.append(surligneur)

        elif rule.ruleType is TypeRule.DELETE:

            newName = rule.applyRule(newName)
            # Suppression => surligneur pour le nom actuel
            for match in re.finditer(rule.elementSuppression, newName):
                surligneur = Surligneur(match.start(), match.end(), rule.color)
                listSurligneurNomActuel = insertSurligneurSuppression(listSurligneurNomActuel, surligneur)

    return listSurligneurNomActuel, listSurligneurNomNouveau


def creerSurligneurReplace(rule, listSurligneurNomActuel, listSurligneurNomNouveau, newName):
    for match in re.finditer(rule.elementAjout, newName):
        surligneur = Surligneur(match.start(), match.end(), rule.color)
        # Difference de nombre de caracteres entre l'element ajoute et suprimmer pour décaller les
        # surligneurs en conséquence
        offset = len(rule.elementAjout) - len(rule.elementSuppression)
        listSurligneurNomNouveau = insertSurligneurReplace(listSurligneurNomNouveau, surligneur, offset)
    for match in re.finditer(rule.elementSuppression, newName):
        surligneur = Surligneur(match.start(), match.end(), rule.color)
        offset = len(rule.elementAjout) - len(rule.elementSuppression)  # TODO Verifier si c'est le bon sens
        listSurligneurNomActuel = insertSurligneurReplace(listSurligneurNomActuel, surligneur, offset)
    return listSurligneurNomActuel, listSurligneurNomNouveau


# Insere un nouveau surligneur dans la liste
def insertSurligneurReplace(listSurligneur, surligneur, offset):
    surligneurInsere = False
    # Si liste vide, on ajoute directement
    if len(listSurligneur) is 0:
        listSurligneur.append(surligneur)
        return listSurligneur

    listASupprimer = []
    print("surligneur a inserer %s " % surligneur.toString())
    for i, s in enumerate(listSurligneur):

        # surligneur avant le nouveau => pas de modif
        # Si l'insertion du surligneur a ete faite, decalle les positions des autres surligneurs
        # surligneur de la liste apres le surligneur a inserer => decaller la position des surligneurs
        if surligneurInsere:
            s.indexDebut = s.indexDebut + offset
            s.indexFin = s.indexFin + offset
            continue

        # nouveau surligneur apres le surligneur actuel -> surligneur suivant de la liste
        if s.indexFin <= surligneur.indexDebut:
            continue

        # nouveau surligneur avant le surligneur de la liste -> inserer avant
        if (surligneur.indexFin - offset) <= s.indexDebut:
            listSurligneur.insert(i, surligneur)
            surligneurInsere = True

        # nouveau surligneur chevauche a la fin le surligneur de la liste -> modification
        if s.indexDebut < surligneur.indexDebut < s.indexFin <= (surligneur.indexFin - offset):
            s.indexFin = surligneur.indexDebut
            continue

        # nouveau surligneur chevauche au debut le surligneur de la liste -> modification et insertion
        if surligneur.indexDebut <= s.indexDebut < (surligneur.indexFin - offset) < s.indexFin:
            s.indexDebut = (surligneur.indexFin - offset)
            listSurligneur.insert(i, surligneur)
            surligneurInsere = True
            continue

        # nouveau surligneur englobe le surligneur de la liste -> supprimer
        if surligneur.indexDebut <= s.indexDebut and s.indexFin <= (surligneur.indexFin - offset):
            listASupprimer.append(s)
            continue

        # nouveau surligneur a l'interieur du surligneur de la liste -> split le surligneur en 2
        if s.indexDebut < surligneur.indexDebut and (surligneur.indexFin - offset) < s.indexFin:
            s2 = Surligneur((surligneur.indexFin - offset), s.indexFin, s.color)  # s2 -> surligneur après le nouveau
            s.indexFin = surligneur.indexDebut
            listSurligneur.insert(i + 1, surligneur)  # Insertion apres sur le surligneur actuelle de la liste
            listSurligneur.insert(i + 2, s2)  # Insertion de la seconde parti du surligneur apres
            surligneurInsere = True
            continue

    # Si le surligneur n'a pas été inséré alors on ajoute le surligneur a la fin de la liste
    if not surligneurInsere:
        listSurligneur.append(surligneur)  # Ajoute le surligneur a la fin si

    # Supprimer les surligneur
    for suppr in listASupprimer:
        listSurligneur.remove(suppr)

    return listSurligneur


# Insere un surligneur lors d'une regle d'ajout
def insertSurligneurAjout(listSurligneur, nouveauSurligneur):
    surligneurInsere = False
    largeurSurligneurInsere = nouveauSurligneur.indexFin - nouveauSurligneur.indexDebut
    positionAInserer = 0
    listSurligneurSplit = []

    surligneurASupprimer = None

    if len(listSurligneur) is 0:
        listSurligneur.append(nouveauSurligneur)
        return listSurligneur

    for i, s in enumerate(listSurligneur):

        # surligneur avant le nouveau => pas de modif
        # Si l'insertion du surligneur a ete faite, decalle les positions des autres surligneurs
        # surligneur de la liste apres le surligneur a inserer => decaller la position des surligneurs
        if surligneurInsere:
            s.indexDebut = s.indexDebut + largeurSurligneurInsere
            s.indexFin = s.indexFin + largeurSurligneurInsere
            continue

        # debut du nouveau surligneur dans le surligneur de la liste => split
        if s.indexDebut < nouveauSurligneur.indexDebut < s.indexFin:
            # Split du surligneur avec creation de 2 nouveau surligneur
            surlLargeur = s.indexFin - s.indexDebut
            s1 = Surligneur(s.indexDebut, nouveauSurligneur.indexDebut, s.color)
            s1Largeur = s1.indexFin - s1.indexDebut
            s2 = Surligneur(nouveauSurligneur.indexFin, nouveauSurligneur.indexFin + (surlLargeur - s1Largeur), s.color)
            listSurligneurSplit.append(s1)
            listSurligneurSplit.append(s2)
            positionAInserer = i
            surligneurInsere = True
            surligneurASupprimer = s
        # Nouveau surligneur avant le surligneur de la liste
        elif nouveauSurligneur.indexDebut <= s.indexDebut:
            positionAInserer = i
            surligneurInsere = True
            s.indexDebut = s.indexDebut + largeurSurligneurInsere
            s.indexFin = s.indexFin + largeurSurligneurInsere

    if surligneurASupprimer is not None:
        listSurligneur.remove(surligneurASupprimer)

    if len(listSurligneurSplit) is not 0:
        listSurligneur.insert(positionAInserer, listSurligneurSplit[0])
        listSurligneur.insert(positionAInserer + 1, nouveauSurligneur)
        listSurligneur.insert(positionAInserer + 2, listSurligneurSplit[1])
    else:
        listSurligneur.insert(positionAInserer, nouveauSurligneur)

    return listSurligneur


# TODO
def insertSurligneurSuppression(listSurligneur, surligneur):
    surligneurInsere = False
    largeurSurligneurSupprimer = surligneur.indexFin - surligneur.indexDebut
    positionAInserer = 0
    listSurligneurSplit = []

    surligneurASupprimer = None

    if len(listSurligneur) is 0:
        listSurligneur.append(surligneur)
        return listSurligneur

    for i, s in enumerate(listSurligneur):

        # surligneur avant le nouveau => pas de modif
        # Si l'insertion du surligneur a ete faite, decalle les positions des autres surligneurs
        # surligneur de la liste apres le surligneur a inserer => decaller la position des surligneurs
        if surligneurInsere:
            s.indexDebut = s.indexDebut - largeurSurligneurSupprimer
            s.indexFin = s.indexFin - largeurSurligneurSupprimer

        # debut du nouveau surligneur dans le surligneur de la liste => split
        if s.indexDebut < surligneur.indexDebut < s.indexFin:
            # Split du surligneur avec creation de 2 nouveau surligneur
            surlLargeur = s.indexFin - s.indexDebut
            s1 = Surligneur(s.indexDebut, surligneur.indexDebut, s.color)
            s1Largeur = s1.indexFin - s1.indexDebut
            s2 = Surligneur(surligneur.indexFin, surligneur.indexFin + (surlLargeur - s1Largeur), s.color)
            listSurligneurSplit.append(s1)
            listSurligneurSplit.append(s2)
            positionAInserer = i
            surligneurInsere = True
            surligneurASupprimer = s
        elif surligneur.indexDebut <= s.indexDebut:
            positionAInserer = i
            surligneurInsere = True
            s.indexDebut = s.indexDebut + largeurSurligneurSupprimer
            s.indexFin = s.indexFin + largeurSurligneurSupprimer

    if surligneurASupprimer is not None:
        listSurligneur.remove(surligneurASupprimer)

    if len(listSurligneurSplit) is not 0:
        listSurligneur.insert(positionAInserer, listSurligneurSplit[0])
        listSurligneur.insert(positionAInserer + 1, surligneur)
        listSurligneur.insert(positionAInserer + 2, listSurligneurSplit[1])
    else:
        listSurligneur.insert(positionAInserer, surligneur)

    return listSurligneur
