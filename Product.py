#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Product:
    """
    Classe représentant un produit
    """
    id: int
    name: str
    stock: int
    price: float
    unit: str