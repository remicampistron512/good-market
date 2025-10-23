#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Customer import *
from Product import *


def main():
    id_customer = 0
    while True:

        print("\nVeuillez choisir une option :")
        print("1 - Passer une commande")
        print("2 - Voir le bilan de la journée")
        choice = input("Entrez votre choice (1 ou 2, ou 'QUIT' pour quitter) : ")

        if choice == '1':
            print("CODE REMI")
            #TESTS
            id_customer += 1
            Customer.create_customer(id_customer,"Pierre","Dupont")
            id_customer += 1
            Customer.create_customer(id_customer,"Vanessa","Dubois") # A MODIFIER PAR DES INPUTS FAIT A DES FINS DE TESTS
            id_customer += 1
            Customer.create_customer(id_customer,"Gustave","Fernand")
            continue
        elif choice == '2':
            Customer.create_customer(id_customer, "Pierre", "Dupont")
            id_customer += 1
            Customer.create_customer(id_customer, "Vanessa","Dubois")  # A MODIFIER PAR DES INPUTS FAIT A DES FINS DE TESTS
            id_customer += 1
            Customer.create_customer(id_customer, "Gustave", "Fernand")
            Customer.print_customers()
            Product(1,"Apple", 8,1.50,"kg")
            Product.print_products()
        elif choice.upper() == 'QUIT':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 'QUIT' pour quitter.")


if __name__ == "__main__":
    main()
