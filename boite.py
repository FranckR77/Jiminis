from insecte import Insecte

class Boite:
    def __init__(self, assaisonnement : str, prix : float, poids : int, insecte : Insecte):
        self.setAssaisonnement(assaisonnement)
        self.setPrix(prix)
        self.setPoids(poids)
        self.setlInsecte(insecte)

    def getAssaisonnement(self) -> str:
        return self.__assaisonnement

    def setAssaisonnement(self, valeur : str) -> str:
        self.__assaisonnement = valeur

    def getPoids(self) -> int:
        return self.__poids

    def setPoids(self, valeur : int) -> int:
        self.__poids = valeur

    def getPrix(self) -> float:
        return self.__prix

    def setPrix(self, valeur : float) -> float:
        self.__prix = valeur

    def prixAukilo(self, prixKg : float) -> float:
        prixKg = self.__prix / self.__poids * 1000
        return prixKg

    def setlInsecte(self, valeur : str):
        self.__insecte = valeur

    def __str__(self) -> str:
        res = "Boite de " + self.__insecte.getNom() + " (" + str(self.__poids) + "g) - assaisonnés " + self.__assaisonnement
        return res
