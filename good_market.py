#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Customer import *
from Product import *
from Order import *


def main():
    id_customer = 1
    id_product = 1
    orders = []
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
            Customer.create_customer(id_customer + 1, "Vanessa", "Dubois")
            Customer.create_customer(id_customer + 2, "Gustave", "Fernand")
            apple = Product(id_product, "Pomme", 8, 1.50, "kg")
            pear = Product(id_product + 1, "Poire", 5, 2.50, "kg")
            Product.add_product(apple)
            Product.add_product(pear)


            order1 = Order(status="finished", customer=Customer.customers[0])
            order1.add_line_order(apple)
            order1.add_line_order(pear)

            orders.append(order1)


            # --- Affichage global ---
            print("\n=== CLIENTS ===")
            Customer.print_customers()

            print("\n=== PRODUITS ===")
            Product.print_products()

            print("\n=== COMMANDES ===")
            for order in orders:
                order.print_order()

            continue

        elif choice.upper() == 'QUIT':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 'QUIT' pour quitter.")


if __name__ == "__main__":
    main()
