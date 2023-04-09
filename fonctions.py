# Nous allons définir des mots de passe selon n niveaux de complexité.
# Pour le niveau 1, il s'agira exclusivement de mots en minuscules basiques.
# Pour le niveau 2, mots avec des chiffres à la fin. 
# Pour le niveau 3, mots avec lettres en majuscules / minuscules et chiffres.
# Et enfin le niveau 4 avec des caractères spéciaux en plus des 3 autres complexités.

# Pour faire le choix des caractères aléatoirement
import random as r

# Création d'une liste pour les caractères de force 1
lstNv1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z']

lstNb = ['1','2','3','4','5','6','7','8','9',0]

lstMaj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lstCarS = ['&','é','~','#','{','}','(','[','-','|','è','`','_','ç','^','à',
           '@','=','+','ù','%','*','£','$','!',':','?']


def mdpNiv1(longueur: int) -> str:
    mdp = ""
    if longueur != 0:
        longueur -= 1
        for i in range(longueur+1):
            mdp += r.choice(lstNv1)
    return mdp

def mdpNiv2(longueurMot:int, longueurChiffre:int)->str:
    mdpMot = mdpNiv1(longueurMot)
    mdpChiffres = ""
    if longueurChiffre != 0:
        longueurChiffre -= 1
        for j in range(longueurChiffre+1):
            mdpChiffres += r.choice(lstNb)
    return mdpMot + mdpChiffres

def mdpNiv3(longueurMot:int, lettresMaj:int, nbChiffres:int)->str:
    mdpMot = mdpNiv1(longueurMot)
    mdpChiffres = ""
    partieNb = ""
    if lettresMaj != 0:
        lettresMaj -= 1
        for j in range(lettresMaj+1):
            mdpChiffres += r.choice(lstMaj)

    if nbChiffres != 0:
        nbChiffres -= 1
        for j in range(nbChiffres+1):
            partieNb += r.choice(lstNb[j])

    return mdpMot + mdpChiffres + partieNb

def mdpNiv4(longueurMot:int,lettresMaj:int,nbChiffres:int,longueurCarS:int)->str:
    mdp = mdpNiv3(longueurMot,lettresMaj,nbChiffres)
    partieCarS = ""
    if longueurCarS != 0:
        longueurCarS -= 1
        for i in range(longueurCarS+1):
            partieCarS += r.choice(lstCarS)
    return mdp + partieCarS
