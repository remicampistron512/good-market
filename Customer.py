from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Customer:
    firstName: str
    lastName: str
    customers: ClassVar[List['Customer']] = []

    def __init__(self, firstname: str, lastname: str):
        self.firstName = firstname
        self.lastName = lastname
        Customer.customers.append(self)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def __repr__(self):
        return f"Customer({self.firstName}, {self.lastName})"

    @classmethod
    def print_customers(cls):
        if not cls.customers:
            print("Aucun client passé aujourd'hui")
        else:
            print("Liste des clients passé aujourd'hui :")
            for client in cls.customers:
                print(f"- {client}")
