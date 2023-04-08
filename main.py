# Generateur de mots de passe
import fonctions as fct

def main():
    choix = int(input("Un mot de passe avec quel niveau de difficulté voulez-vous créer ?"))
    if choix == 1:
        print(fct.mdpNiv1(longueur=int(input("longueur ?"))))
    elif choix == 2:
        return fct.mdpNiv2()
    elif choix == 3:
        return fct.mdpNiv3
    elif choix == 4:
        return fct.mdpNiv4()
    else:
        print("Vous devez saisir un nombre entre 1 et 4 inclus")
    
main()