#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Customer import Customer
from Product import Product
from Order import Order
from Inventory import Inventory


def review(id_customer : int, id_product : int, orders, inventory : Inventory) -> None:

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

    Customer.print_customers()

    print("\n=== Details des commandes des clients ===")
    for order in orders:
        order.print_order()
        print("\n")

    print("=== Stock Restant ===")
    inventory.print_inventory()


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
            inventory = Inventory()
            current_customer = Customer(1, "remi", "campistron")
            current_order = Order("ongoing", current_customer)
            while True:
                inventory.print_inventory()

                product_choice = input("Choisissez un produit par son id : ")
                if product_choice == "" or not product_choice.isdigit():
                    print("merci de rentrer une id de produit valide")
                    continue
                elif product_choice.isdigit() and not any(product.id == int(product_choice) for product in inventory.stock):
                    print("merci de rentrer une id de produit valide")
                    continue

                quantity_choice = input("Quelle quantité ? : ")
                if not quantity_choice.isdigit():
                    print("merci de rentrer une quantité valide")
                    continue

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
                    break
                elif continue_shopping_choice == "c":
                    continue
                elif continue_shopping_choice == "v" :
                    current_order.print_order()

        elif choice == '2':
            review(id_customer = id_customer, id_product = id_product, orders = orders, inventory = inventory)

        elif choice.upper() == 'QUIT':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 'QUIT' pour quitter.")


if __name__ == "__main__":
    main()
