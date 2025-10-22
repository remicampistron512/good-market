#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

# classe Customer

from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Customer:
    """Classe représentant un client
        — id_customer : Identifiant du client
        – firstname : prénom du client
        — lastname : nom du client
    """
    id_customer: int
    firstname: str
    lastname: str
    customers: ClassVar[List['Customer']] = []

    def __init__(self, id_customer: int, firstname: str, lastname: str) -> None:
        """
         Permet la création d'un client
        :param firstname: Prenom du client
        :param lastname: Nom du client
        """
        self.id_customer = id_customer
        self.firstname = firstname
        self.lastname = lastname
        Customer.customers.append(self)

    def __str__(self) -> str:
        """
        Permet de configurer l'affichage d'un client
        :return: Prenom et nom du client
        """
        return f"{self.firstname} {self.lastname}"

    def __repr__(self) -> str:
        """
        Permet de configurer l'affichage d'un client pour le développement
        :return: Prenom et nom du client
        """
        return f"Customer({self.id_customer}, {self.firstname}, {self.lastname})"


    @classmethod
    def nb_customers(cls) -> int:
        """
        Permet de l'affichage du nombre de clients passés ce jour
        :return: nombre de clients passés ce jour
        """
        return len(cls.customers)


    @classmethod
    def print_customers(cls) -> None:
        """
        Permet d'affichage de la liste des clients
        :return: None
        """
        if not cls.customers:
            print("Aucun client passé aujourd'hui")
        else:
            print("Liste des clients passé aujourd'hui :")
            for client in cls.customers:
                print(f"- {client}")
