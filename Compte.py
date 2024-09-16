# 2022-2023 RT2 TP1

# https://docs.python.org/fr/3/tutorial/classes.html

# Classe Compte à compléter

# Ex 2.1
class Compte:
    __numero: int 
    __solde: float 
    __decouvert: float 

    def __init__(self, num:int, sol:0.0, dec:0.0):
        self.__numero = num
        self.__solde = sol
        self.__decouvert = dec

# Ex 2.2
    def get_decouvert(self):
        return self.__decouvert

    def get_numero(self):
        return self.__numero

    def get_solde(self):
        return self.__solde

    def set_decouvert(self, montant: float):
        self.__decouvert =  montant

    def afficher_solde(self):
        print('Le solde de votre compte ' , self.__numero , 'est de :' , self.__solde , '$')
        return ""

#Ex 3.4
    def depot(self, montant : float):
        if montant > 0:
            self.__solde += montant
            print("Depot de " , montant , "$ effectuee sur le compte n°" , self.__numero)
        else:
            print("Le montant doit etre positif")

    def retrait(self, montant : float) -> str:
        montant_maximum_retrait = self.__solde + self.__decouvert
        if montant > 0 and montant <= montant_maximum_retrait :
            self.__solde -= montant
            print("Retrait de " , montant, "$ effectue.")
            return ""
        else:
            print("Retrait de" , montant , "$ refuse . Car votre solde est insuffisant")
            return ""
