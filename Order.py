#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from Product import Product

@dataclass
class Order:
    """
    Classe représentant une commande

    Attributs
        products: la liste des produits composant la commande
        date: la date à laquelle la commande a été réalisée
        status: l'état de la commande "finished" ou "ongoing"
    """

    date: datetime
    status: str
    total: float
    line_orders: List[Product] = field(default_factory=list)

    def add_line_order(self, product: Product) -> None:
        self.line_orders.append(product)

    def print_order(self) -> None:
        """
        Permet d'affichage de la liste des produits
        """
        if not self.line_orders:
            print("Aucun produit enregistré")
        else:
            print("Voici votre commande :")
            for line_order in self.line_orders:
                print(f"- {line_order.name} ({line_order.unit}) — {line_order.price:.2f} €")

    def total(self):
        return sum(product.price for product in self.line_orders)




