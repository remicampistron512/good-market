from dataclasses import dataclass, field
from Product import Product
from typing import ClassVar

@dataclass
class Inventory:
    # copie du stock pour pouvoir le modifier
    stock: list[Product] = field(default_factory=list)

    # Constante de classe tuple de tuples
    INITIAL_STOCK: ClassVar[tuple[Product, ...]] = (
        Product(1, "Clémentine", 6, 2.90, "kg"),
        Product(2, "Datte", 4, 7.00, "kg"),
        Product(3, "Grenade", 3, 3.50, "kg"),
        Product(4, "Kaki", 3, 4.50, "kg"),
        Product(5, "Kiwi", 5, 3.50, "kg"),
        Product(6, "Mandarine", 6, 2.80, "kg"),
        Product(7, "Orange", 8, 1.50, "kg"),
        Product(8, "Pamplemousse", 8, 2.00, "pièce"),
        Product(9, "Poire", 5, 2.50, "kg"),
        Product(10, "Pomme", 8, 1.50, "kg"),
        Product(11, "Carotte", 7, 1.30, "kg"),
        Product(12, "Choux de Bruxelles", 4, 4.00, "kg"),
        Product(13, "Chou vert", 12, 2.50, "pièce"),
        Product(14, "Courge butternut", 6, 2.50, "pièce"),
        Product(15, "Endive", 5, 2.50, "kg"),
        Product(16, "Épinard", 4, 2.60, "kg"),
        Product(17, "Poireau", 5, 1.20, "kg"),
        Product(18, "Potiron", 6, 2.50, "pièce"),
        Product(19, "Radis noir", 10, 5.00, "pièce"),
        Product(20, "Salsifis", 3, 2.50, "kg"),
    )

    def __post_init__(self):
        if not self.stock:
            self.stock = list(self.INITIAL_STOCK)

    def update_stock(self,product):
        for item in self.stock:
           if product.id == item.id:
                item.quantity = item.quantity - product.quantity

    def print_inventory(self):
        print(f"voici l'état du stock")
        for item in self.stock:
          print(f"- {item.name:<22} {item.quantity:>3} {item.unit:<6}")




