# Generateur de mots de passe
import fonctions as fct

def main():
    choix = ""
    while choix != -1:
        choix = int(input("Un mot de passe avec quel niveau (1 à 4 inclus) de difficulté voulez-vous créer ? (-1 pour quitter)"))
        if choix == 1:
            print(fct.mdpNiv1(longueur=int(input("Combien de caractères souhaitez-vous dans votre mot de passe ?"))))
        elif choix == 2:
            print(fct.mdpNiv2(longueurMot=int(input("Combien de minuscules souhaitez-vous dans votre mot de passe ?")),longueurChiffre=int(input("Combien de chiffre(s) souhaitez-vous ?"))))
        elif choix == 3:
            print(fct.mdpNiv3(longueurMot=int(input("Combien de minuscules souhaitez-vous dans votre mot de passe ?")),lettresMaj=int(input("Combien de lettre(s) en majuscules souhaitez-vous ?")),nbChiffres=int(input("Combien de chiffre(s) souhaitez vous ?"))))
        elif choix == 4:
            print(fct.mdpNiv4(longueurMot=int(input("Combien de minuscules souhaitez-vous dans votre mot de passe ?")),lettresMaj=int(input("Combien de lettre(s) en majuscules souhaitez-vous ?")),nbChiffres=int(input("Combien de chiffre(s) souhaitez vous ?")),longueurCarS=int(input("Combien de Caractères Spéciaux souhaitez-vous ?"))))
    return "Merci d'avoir utilisé mon programme"
    
print(main())
