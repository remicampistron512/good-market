#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Customer import Customer
from Product import Product
from Order import Order
from Inventory import Inventory
from UserInput import UserInput


def review(orders, inventory : Inventory) -> None:

    Customer.print_customers()

    print("\n=== Details des commandes des clients ===")
    for order in orders:
        order.print_order()
        print("\n")

    print("=== Stock Restant ===")
    inventory.print_inventory()


def main():
    user_input = UserInput()
    id_customer = 1
    orders = []
    inventory = Inventory()


    while True:

        print("\nVeuillez choisir une option :")
        print("1 - Passer une commande")
        print("2 - Voir le bilan de la journée")
        choice = input("Entrez votre choice (1 ou 2, ou 'QUIT' pour quitter) : ")
        if choice == '1':

            first_name_choice = user_input.is_non_empty("Entrez votre prénom : ")
            last_name_choice = user_input.is_non_empty("Entrez votre nom : ")
            current_customer = Customer(id_customer, first_name_choice, last_name_choice)
            current_order = Order("ongoing", current_customer)
            while True:
                print(f"Bienvenue au bon marché {current_customer.firstname} {current_customer.lastname}")
                inventory.print_inventory()

                product_choice = input("Choisissez un produit par son id : ")
                if product_choice == "" or not product_choice.isdigit():
                    print("merci de rentrer une id de produit valide")
                    continue
                elif product_choice.isdigit() and not any(product.id == int(product_choice) for product in inventory.stock):
                    print("merci de rentrer une id de produit valide")
                    continue

                quantity_choice = user_input.is_int("Quelle quantité ? :")


                current_product = ""

                if product_choice:
                    for item in inventory.stock:
                        if int(product_choice) == item.id:
                            current_product = Product(id=item.id, name=item.name, quantity=int(quantity_choice),
                                                      price=item.price,
                                                      unit=item.unit)
                            current_order.add_line_order(current_product)

                inventory.update_stock(current_product)

                continue_shopping_choice = input("Continuer mes achats (c) / voir ma commande (v) / terminer mes achats (q) ?")

                if continue_shopping_choice == "q":
                    if current_order:
                        current_order.print_order()
                        orders.append(current_order)
                        Customer.create_customer(current_customer)
                        id_customer+=1
                    break
                elif continue_shopping_choice == "c":
                    continue
                elif continue_shopping_choice == "v" :
                    current_order.print_order()

        elif choice == '2':
            review(orders = orders, inventory = inventory)

        elif choice.upper() == 'QUIT':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 'QUIT' pour quitter.")


if __name__ == "__main__":
    main()
