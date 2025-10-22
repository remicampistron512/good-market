from dataclasses import dataclass

@dataclass
class Customer:
    firstName: str
    lastName: str

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f" {self.firstName} {self.lastName}"

    def __repr__(self):
        return f"Customer({self.firstName}, {self.lastName})"


