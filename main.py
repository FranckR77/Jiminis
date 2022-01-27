"""
Programme Jimini's : manger des insectes comestibles
Salés, sucrés ou naturés, les insectes de chez Jimini's suraont vous régaler tout au long de la journée
"""
from insecte import Insecte
from boite import Boite

def afficher(lesInsectes) -> None:
    for insecte in lesInsectes:
        print(insecte)

def afficherBoite(lesBoites) -> None:
    for boite in lesBoites:
        print(boite)

# Programme principal
#liste des insectes
lesInsectes = []

# création des insectes
# TODO 2 : instancier 3 insectes : le criquet (rnj : 28), le grillon (rnj : 25), le molitor (rnj : 28) [FAIT]
criquet = Insecte("Criquet", 28)
grillon = Insecte("Grillon", 25)
molitor = Insecte("Molitor", 28)

# TODO 3 : ajouter les insectes à la liste d'insectes [FAIT]
lesInsectes.append(criquet)
lesInsectes.append(grillon)
lesInsectes.append(molitor)

# TODO 6 : afficher l'ensemble des insectes (nom) [FAIT]
afficher(lesInsectes)

# TODO 7 : rédiger une fonction rnjMoyen retournant le rnj moyen pour une liste d'insectes fournies en paramètres. [FAIT]
def rnjMoyen(lesInsectes) -> int:
    moyenne = 0
    rnjInsecte = 0
    for unInsecte in range(len(lesInsectes)):
        insecte = lesInsectes[unInsecte]
        rnjInsecte = rnjInsecte + insecte.getRnj()
        moyenne = rnjInsecte/len(lesInsectes)
    return moyenne

# TODO 8 : tester la fonction rnjMoyen sur la liste d'insecte [FAIT]
print("La valeur nutrionnelle moyenne est de :", rnjMoyen(lesInsectes))

# Boite
lesBoites = [Boite("mangue douce", 5.95, 14, grillon), Boite("oignon fumé", 5.95, 14, grillon), Boite("paprika", 6.95, 10, criquet), Boite("poivre & tomates séchées", 6.95, 10, criquet), Boite("curry fruité", 6.95, 10, criquet), Boite("à la grecque", 5.95, 10, criquet), Boite("sésame & cumin", 6.95, 18, molitor), Boite("ail & fines herbes", 5.95, 18, molitor), Boite("soja impérial", 6.95, 18, criquet)]
afficherBoite(lesBoites)
