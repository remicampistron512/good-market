#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from Product import Product
from Customer import Customer
import uuid

@dataclass
class Order:
    """
    Classe représentant une commande

    Attributs
        status : l'état de la commande "finished" ou "ongoing"
        customer : client (Costumer) qui a créé la commande
        uid : identifiant unique de la commande
        date : la date à laquelle la commande a été réalisée, ici, par défaut la date courante
        line_orders : la liste des élements (Product) de la commande
    """


    status: str
    customer: Customer
    uid: str = field(default_factory=uuid.uuid4)
    date: datetime = field(default_factory=datetime.now)
    line_orders: List[Product] = field(default_factory=list)

    def add_line_order(self, product: Product) -> None:
        self.line_orders.append(product)

    def print_order(self) -> None:
        """
        Permet l'affichage de la liste des produits de la commande
        """
        if not self.line_orders:
            print("Aucun produit enregistré")
        else:
            print(f"{f'{self.customer.firstname.title()} {self.customer.lastname.title()} voici votre commande du {self.date:%d/%m/%Y %H:%M}':^50}")
            print(f"numéro de commande: {self.uid}")
            for line_order in self.line_orders:
                print(f"- {line_order.name:<22} {line_order.stock:>3} {line_order.unit:<6} : {line_order.stock * line_order.price:>10.2f} €")
            print("- "*25)

            print(f"Total {self.compute_total():>42.2f} €")

    def compute_total(self) -> float:
        return sum(line_order.stock * line_order.price for line_order in self.line_orders)
