#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dataclasses import dataclass, field
from typing import List,Dict, Tuple
from Product import Product
from Customer import Customer
from Inventory import Inventory
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
            customer_name = f"{self.customer.firstname.title()} {self.customer.lastname.title()}"
            print(f"{customer_name} - Commande du {self.date:%d/%m/%Y %H:%M}".center(70))
            print(f"Numéro de commande : {self.uid}")
            print("-" * 70)

            agg = self.aggregate_lines()
            for pid, item in agg.items():
                qty = item["qty"]
                price = item["price"]
                total = qty * price
                print(f"- {item['name']:<22} {qty:>3} {item['unit']:<6} : {total:>10.2f} €")

            print("-" * 70)
            print(f"{'Total':>37} : {self.compute_total():>8.2f} €")

    def compute_total(self) -> float:
        return sum(line_order.quantity * line_order.price for line_order in self.line_orders)

    def aggregate_lines(self) -> Dict[int, dict]:
        """
        Regroupe les lignes par product.id et additionne les quantités.
        Retourne un dict: id -> {name, unit, price, qty}
        """
        agg: Dict[int, dict] = {}
        for product in self.line_orders:
            if product.id not in agg:
                agg[product.id] = {"name":product.name, "unit": product.unit, "price": product.price, "qty": 0}
            agg[product.id]["qty"] += product.quantity
        return agg
