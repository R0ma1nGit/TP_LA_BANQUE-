#Ex 2.3

class Mabanque:
    __Numcompte: int 
    __solde_initial: float 
    __decouvert_autorise: float 

    def __init__(self, NC:int, SI:0.0, DA:0.0):
        self.__Numcompte = NC
        self. __solde_initial = SI
        self.__decouvert_autorise = DA


    def afficher_decouvert_autorise(self):
        print("Decouvert autorise du compte n°" , self.__Numcompte , "est de :" , self.__decouvert_autorise , "$")

    
    def modifier_decouvert_autorise(self, nouveau_decouvert):
        self.__decouvert_autorise = nouveau_decouvert
        print("Votre decouvert autorise est de :" , self.__decouvert_autorise , "$" )

    def afficher_solde(self):
        print("Solde du compte n° " , self.__Numcompte , "est de :" , self. __solde_initial , "$")

#Ex 2.4
    def depot(self, montant : float):
        if montant > 0:
            self.__solde_initial += montant
            print("Depot de " , montant , "$ effectuee sur le compte n°" , self.__Numcompte)
        else:
            print("Le montant doit etre positif")
#Ex 2.5
    def retrait(self, montant : float) -> str:
        montant_maximum_retrait = self.__solde_initial + self.__decouvert_autorise
        if montant > 0 and montant <= montant_maximum_retrait :
            self.__solde_initial -= montant
            print("Retrait de " , montant, "$ effectue.")
            return ""
        else:
            print("Retrait de" , montant , "$ refuse . Car votre solde est insuffisant")
            return ""
   
