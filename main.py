# Generateur de mots de passe
import fonctions as fct

def main():
    print("")
    choix = int(input("Un mot de passe avec quel niveau de difficulté voulez-vous créer ?"))
    if choix == 1:
        print(fct.mdpNiv1(longueur=int(input("De quelle longueur souhaitez vous votre mot de passe ?"))))
    elif choix == 2:
        return fct.mdpNiv2(longueurMot=int(input("De quelle longueur souhaitez-vous votre mot de passe ?")),longueurChiffre=int(input("Combien de chiffre(s) souhaitez-vous ?")))
    elif choix == 3:
        return fct.mdpNiv3(longueurMot=int(input("De quelle longueur souhaitez-vous votre mot de passe ?")),lettresMaj=int(input("Combien de lettre(s) en majuscules souhaitez-vous ?")),lettresMin=int(input("Combien de lettre(s) en minuscules souhaitez-vous ?")),nbChiffres=int(input("Combien de chiffre(s) souhaitez vous ?")))
    elif choix == 4:
        return fct.mdpNiv4(longueurMot=int(input("De quelle longueur souhaitez-vous votre mot de passe ?")),lettresMaj=int(input("Combien de lettre(s) en majuscules souhaitez-vous ?")),lettresMin=int(input("Combien de lettre(s) en minuscules souhaitez-vous ?")),nbChiffres=int(input("Combien de chiffre(s) souhaitez vous ?")),longueurCarS=int(input("Combien de Caractères Spéciaux souhaitez-vous ?")))
    else:
        print("Vous devez saisir un nombre entre 1 et 4 inclus")
    
print(main())
