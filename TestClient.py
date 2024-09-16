#!/usr/bin/python3
# 2022-2023 RT2 TP1

# https://docs.python.org/fr/3/tutorial/appendix.html#executable-python-scripts

from Client import Client

# Ex 2.1
from Compte import Compte
# num = 4726
# sol=0.0
# dec=0.0

# if __name__ == "__main__":

#     compte = Compte(num, sol, dec)
#     print('Votre numero de compte est :', num )
#     print('Votre solde de compte est de :', sol , '$' )
#     print('Votre decouvert de compte est de :', dec ,'$' )
#     print(compte.afficher_solde())

# Ex 2.3
from Mabanque import Mabanque

# if __name__ == "__main__":
     
#      mabanque = Mabanque(NC=1, SI=0.0, DA=0.0)

#      mabanque.afficher_decouvert_autorise()

#      mabanque.modifier_decouvert_autorise(100)

#      mabanque.afficher_decouvert_autorise()

#      mabanque.afficher_solde()
# # Ex 2.4
#      mabanque.depot(300)

#      mabanque.afficher_solde()
# # Ex 2.5
#      mabanque.retrait(100)

#      mabanque.afficher_solde()

# Ex 2.6
# if __name__ == "__main__":

#     c_2 = Mabanque(NC=2, SI=0.0, DA=0.0)

#     c_2.depot(1000)

#     c_2.afficher_solde()

#     c_2.retrait(600)
    
#     c_2.afficher_solde()

#     c_2.retrait(700)

#     c_2.afficher_solde

#     c_2.modifier_decouvert_autorise(500)

#     c_2.retrait(700)

#     c_2.afficher_solde()

# Ex 3.2
# if __name__ == "__main__":  
#     compte_test = Compte(num= 111, sol=1000, dec= 500)
#     client_test = Client(n= "LEON", p= "Romain" , compte = compte_test)
#     client_test.afficher_info_client()
# Ex 3.3
#     client_test.afficher_solde()

# Ex 3.4
# if __name__ == "__main__": 
#     c2 = Compte (num= 2, sol= 0.0, dec= 0.0)
    
#     c2.depot(1000)
#     c2.afficher_solde()
#     print(c2.retrait(600))

#     c2.afficher_solde()
#     print(c2.retrait(700))

#     c2.afficher_solde()
#     c2.set_decouvert(500)
#     print(c2.retrait(700))
   
#     c2.afficher_solde()

#     client1 = Client(n="Leon" , p="Romain" , compte = c2)
#     client1.afficher_solde()
 

# Ex 4.2
from Client import ClientMultiComptes

# if __name__ == "__main__": 

#     c1 = Compte(num = 1, sol= 500, dec= 0.0)
#     c2 = Compte(num = 2, sol= 1500, dec= 0.0)
#     c3 = Compte(num = 3, sol= 2500, dec= 0.0)
#     client_multi = ClientMultiComptes(nom = "LEON", prenom = "Romain")
#     client_multi.ajouter_compte(c1)
#     client_multi.ajouter_compte(c2)
#     client_multi.ajouter_compte(c3)
#     client_multi.afficher_info_client()
# #Ex 4.3

#     print("Le solde total de vos compte est de :" , client_multi.get_solde() , "$")

# Ex 4.4
# if __name__ == "__main__":
#     compte10 = Compte(num=10, sol=1000, dec=0.0)
#     print("Compte n° 10 cree avec un depot de 1000$")

#     client_multi = ClientMultiComptes(nom = "LEON" , prenom="Romain")
#     client_multi.ajouter_compte(compte10)
#     print("ClienMultiCompte avec le compte n° 10 cree.")
#     print("Affichage du solde apres ajout du compte n°10:" )
#     print("Le solde total du client est de :", client_multi.get_solde() , "$")

#     compte20 = Compte(num=20, sol=2500, dec=0.0)
#     print("Compte n°20 cree avec un depot de 2000$")
#     client_multi.ajouter_compte(compte20)
#     print("Compte n°20 ajoute a client.")
#     compte20.afficher_solde()

#     print("Solde total du compte client est de :" , client_multi.get_solde() , "$") 


# Ex 4.5
if __name__ == "__main__": 

    c1 = Compte(num = 1, sol= 500, dec= 0.0)
    c2 = Compte(num = 2, sol= 1500, dec= 0.0)
    c3 = Compte(num = 3, sol= 2500, dec= 0.0)
    client_multi = ClientMultiComptes(nom = "LEON", prenom = "Romain")
    client_multi.ajouter_compte(c1)
    client_multi.ajouter_compte(c2)
    client_multi.ajouter_compte(c3)
    client_multi.afficher_etat_client()
 
    









