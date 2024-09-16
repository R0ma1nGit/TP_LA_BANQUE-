# 2022-2023 RT2 TP1

# https://docs.python.org/fr/3/tutorial/classes.html

# Classe Client à compléter
from Compte import Compte

# Ex 1.1
# Ex 3.1  Ajout attribue "__compte_courant" de type Compte 
class Client:
    __nom: str
    __prenom: str  
    __compte_courant = Compte


    
# Ex 1.2
# Ex 3.2
    def __init__(self,n : str,p : str, compte : Compte):
        self.__nom = n
        self.__prenom = p
        self.__compte_courant = compte
       
# Ex 1.3
    def get_prenom(self) -> str:
        return self.__prenom

    def get_nom(self)-> str:
        return self.__nom

    def get__compte_courant(self) -> Compte:
        return self.__compte_courant

# Ex 3.3 

    def get__solde(self) -> float:
        return self.__compte_courant.get_solde()



# Ex 1.4
# if __name__ == "__main__":
#     client = Client(n="Leon" , p="Romain")
#     print('Bonjours', client.get_nom() , client.get_prenom()) 

# Ex 3.2
    def afficher_info_client(self):
        print("Client:" , self.__nom)
        print("Compte n°" , self.__compte_courant.get_numero())
        self.__compte_courant.afficher_solde()

# Ex 3.3 
    def afficher_solde(self):
        print("Le solde du client" , self.__nom , self.__prenom , "est de :" , self.get__solde() , "$")

# Ex 4.1

class ClientMultiComptes:
    __nom: str
    __prenom: str
    __list: list
    __nbComptes: int

    def __init__(self, nom: str, prenom: str):
        self.__nom = nom
        self.__prenom = prenom
        self.__list= []  
        self.__nbComptes = 0    
#Ex 4.2
    def ajouter_compte(self, c: Compte):
        self.__list.append(c)  
        self.__nbComptes += 1            
#Ex 4.5
    def afficher_etat_client(self):
        print("Client :" , self.__prenom , self.__nom)
        print("Comptes bancaires :" , self.__nbComptes)
        if not self.__list:
            print("Aucun compte.")
        else:
            for compte in self.__list:
                print(" - Compte n°" , compte.get_numero() , "Solde =" , compte.get_solde() , "$")
        
        print("Le solde total de vos compte est de :" , self.get_solde() , "$")
    
    def get_nbComptes(self):
        return self.__nbComptes
   
    def get_solde(self) -> float:
        total_solde = sum(compte.get_solde() for compte in self.__list)
        return total_solde

    def afficher_info_client(self):
        print("Client :" , self.__prenom , self.__nom)
        print("Nombre total de vos comptes :" , self.__nbComptes)
        print("Détail de vos comptes :")
        for compte in self.__list:
            print(" - Compte n°" , compte.get_numero() , "Solde =" , compte.get_solde() , "$")
