#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Customer import Customer
from Product import Product
from Order import Order
from Inventory import Inventory


def review():
    id_customer = 1
    id_product = 1
    orders = []
    Customer.create_customer(id_customer=id_customer, firstname="Pierre", lastname="Dupont")
    Customer.create_customer(id_customer=id_customer + 1, firstname="Vanessa", lastname="Dubois")
    apple = Product(id=id_product, name="Pomme", quantity=8, price=1.50, unit="kg")
    pear = Product(id=id_product + 1, name="Poire", quantity=5, price=2.50, unit="kg")
    Product.add_product(apple)
    Product.add_product(pear)

    order1 = Order(status="finished", customer=Customer.customers[0])
    order1.add_line_order(apple)
    order1.add_line_order(pear)
    orders.append(order1)

    order2 = Order(status="finished", customer=Customer.customers[1])
    order2.add_line_order(apple)
    orders.append(order2)

    # --- Affichage global ---
    Customer.print_customers()

    print("\n=== Details des commandes des clients ===")
    for order in orders:
        order.print_order()
        print("\n")

    print("=== Stock Restant ===")
    inventory = Inventory()
    inventory.print_inventory()


def main():
    while True:

        print("\nVeuillez choisir une option :")
        print("1 - Passer une commande")
        print("2 - Voir le bilan de la journée")
        choice = input("Entrez votre choice (1 ou 2, ou 'QUIT' pour quitter) : ")

        if choice == '1':
            inventory = Inventory()
            current_customer = Customer(1, "remi", "campistron")
            current_order = Order("ongoing", current_customer)
            while True:
                inventory.print_inventory()
                product_choice = input("Choisissez un produit par son id ")
                quantity_choice = input("Quelle quantité ?")
                current_product = ""
                if product_choice:
                    for item in inventory.stock:
                        if int(product_choice) == item.id:
                            current_product = Product(id=item.id, name=item.name, quantity=int(quantity_choice),
                                                      price=item.price,
                                                      unit=item.unit)
                            current_order.add_line_order(current_product)
                inventory.update_stock(current_product)

                continue_shopping_choice = input("Continuer mes achats (c) / voir ma commande (v) / quitter (q) ?")
                if continue_shopping_choice == "q":
                    break
                elif continue_shopping_choice == "c":
                    continue
                elif continue_shopping_choice == "v" :
                    current_order.print_order()

        elif choice == '2':
            review()

        elif choice.upper() == 'QUIT':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 'QUIT' pour quitter.")


if __name__ == "__main__":
    main()
