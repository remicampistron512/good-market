#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Product:
    """
    Classe représentant un produit

    Attributs:
        id: identifiant unique du produit
        name: nom du produit
        stock: quantité disponible
        price: prix en euros
        unit: unité de poids

    """
    id: int
    name: str
    stock: int
    price: float
    unit: str
    products: ClassVar[List['Product']] = []


    @classmethod
    def print_products(cls):
        """
        Permet d'affichage de la liste des produits
        """
        if not cls.products:
            print("Aucun produit enregistré")
        else:
            print("Voici la liste de produits :")
            for product in cls.products:
                print(f"- {product}")

    @classmethod
    def add_product(cls,product):
        """
        Ajoute un produit à la liste des produits
        :param product: un objet product à ajouter
        """
        cls.products.append(product)
