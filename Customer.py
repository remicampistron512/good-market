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
    def create_customer(cls, customer: 'Customer') -> 'Customer':
        """
        Ajoute un objet Customer à la liste des clients.
        :param customer: Instance de Customer à ajouter
        :return: L'objet Customer ajouté
        """
        cls.customers.append(customer)
        return customer


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
        Affiche la liste des clients passés aujourd'hui
        :return: None
        """
        if not cls.customers:
            print("Aucun client n'est passé aujourd'hui.")
        else:
            print(f"\nListe des {Customer.nb_customers()} clients passés aujourd'hui :")
            print("-" * 40)
            for i, client in enumerate(cls.customers, start=1):
                print(f"{client.id_customer}. {client.firstname} {client.lastname}")
            print("-" * 40)
