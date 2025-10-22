#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from dataclasses import dataclass

@dataclass
class Order:
    """
    Classe représentant une commande
    """
    product_list: list
    date: datetime