class Surligneur:
    indexDebut = 0
    indexFin = 0
    color = None

    def __init__(self, debut, fin, color):
        self.indexDebut = debut
        self.indexFin = fin
        self.color = color


# Insere un nouveau surligneur dans la liste
def insertSurligneur(listSurligneur: list, surligneur):
    # Si liste vide, on ajoute directement
    if len(listSurligneur) is 0:
        listSurligneur.append(surligneur)

    listSurligneurAModifier = []
    # On ajoute tous les surligneurs qui chevauche le surligneur à insérer
    for s in listSurligneur:
        if s.indexFin <= surligneur.indexDebut or s.indexDebut <= surligneur.indexFin:
            listSurligneurAModifier.append(s)

            # TODO CONTINUER LA CLASSE PATATE


def getEle(l, i):
    try:
        return l[i]
    except IndexError:
        return None
