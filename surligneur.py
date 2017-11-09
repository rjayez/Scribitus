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

    listRegleApplication, listRegleSurligneur = listRegle, listRegle

    # Application des regles
    newName = name
    for rule in listRegle:
        newName = rule.applyRule(newName)

    # Creer liste surligneur
    for rule in listRegle:

        if rule.ruleType is TypeRule.ADD:
            surligneur = Surligneur(rule.position, rule.position + len(rule.elementAjout), rule.color)
            print
            surligneur.toString()
            inserSurligneurAjout(listSurligneurNomNouveau, surligneur)
        else:
            for match in re.finditer(rule.elementAjout, newName):
                surligneur = Surligneur(match.start(), match.end(), rule.color)
                print
                surligneur.toString()
                listSurligneurNomNouveau = insertSurligneur(listSurligneurNomNouveau, surligneur)
            for match in re.finditer(rule.elementSuppression, newName):
                surligneur = Surligneur(match.start(), match.end(), rule.color)
                print
                surligneur.toString()
                listSurligneurNomActuel = insertSurligneur(listSurligneurNomActuel, surligneur)

    while len(listRegleApplication) is not 0 and len(listRegleSurligneur):

        regleApplication = listRegleApplication.pop()
        if regleApplication.ruleType is TypeRule.REPLACE:
            break

    listReglePourSurligneur = []
    for rule in listRegle:

        if rule.ruleType is TypeRule.REPLACE:
            newName = rule.applyRule(newName)
            listReglePourSurligneur.append(rule)
            continue
        elif rule.ruleType is TypeRule.ADD:
            newName = rule.applyRule(newName)
        elif rule.ruleType is TypeRule.DELETE:
            newName = rule.applyRule(newName)

    print
    "list nouveau"
    for s in listSurligneurNomNouveau:
        print
        s.toString()

    return listSurligneurNomActuel, listSurligneurNomNouveau


# Insere un nouveau surligneur dans la liste
def insertSurligneur(listSurligneur, surligneur):
    # Si liste vide, on ajoute directement
    if len(listSurligneur) is 0:
        listSurligneur.append(surligneur)
        return listSurligneur

    listASupprimer = []
    print("surligneur a inserer %s " % surligneur.toString())
    for i, s in enumerate(listSurligneur):
        # nouveau surligneur avant le surligneur de la liste -> inserer avant
        if surligneur.indexFin <= s.indexDebut:
            listSurligneur.insert(i, surligneur)
            break

        # nouveau surligneur englobe le surligneur de la liste -> supprimer
        if surligneur.indexDebut <= s.indexDebut and surligneur.indexFin >= s.indexFin:
            listASupprimer.append(s)
            listSurligneur.insert(i, surligneur)
            break

        # nouveau surligneur chevauche au debut le surligneur de la liste -> modification
        if s.indexDebut < surligneur.indexFin < s.indexFin:
            s.indexDebut = surligneur.indexFin
            continue

        # nouveau surligneur chevauche a la fin le surligneur de la liste -> modification
        if s.indexFin > surligneur.indexDebut > s.indexDebut:
            s.indexFin = surligneur.indexDebut
            continue
    else:
        listSurligneur.append(surligneur)  # Ajoute le surligneur a la fin si

    # Supprimer les surligneur
    for suppr in listASupprimer:
        listSurligneur.remove(suppr)

    return listSurligneur


# Insere un surligneur lors d'une regle d'ajout
def inserSurligneurAjout(listSurligneur, surligneur):
    surligneurInsere = False
    largeurSurligneurInsere = surligneur.indexFin - surligneur.indexDebut
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
            s.indexDebut = s.indexDebut + largeurSurligneurInsere
            s.indexFin = s.indexFin + largeurSurligneurInsere

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
            s.indexDebut = s.indexDebut + largeurSurligneurInsere
            s.indexFin = s.indexFin + largeurSurligneurInsere

    if surligneurASupprimer is not None:
        listSurligneur.remove(surligneurASupprimer)

    if len(listSurligneurSplit) is not 0:
        listSurligneur.insert(positionAInserer, listSurligneurSplit[0])
        listSurligneur.insert(positionAInserer + 1, surligneur)
        listSurligneur.insert(positionAInserer + 2, listSurligneurSplit[1])
    else:
        listSurligneur.insert(positionAInserer, surligneur)

    return listSurligneur


# TODO
def inserSurligneurSuppression(listSurligneur, surligneur):
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
