#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Product:
    """
    Classe représentant un produit

    Attributs :
        id : identifiant unique du produit
        name : nom du produit
        stock : quantité disponible
        price : prix en euros
        unit : unité de poids

    """
    id: int
    name: str
    quantity: int
    price: float
    unit: str
