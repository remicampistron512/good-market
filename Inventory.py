from dataclasses import dataclass, field
from Product import Product
from typing import ClassVar

@dataclass
class Inventory:
    """
    Permet de tenir un inventaire et de le mettre à jour
    """
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

    def __post_init__(self) -> None:
        if not self.stock:
            self.stock = list(self.INITIAL_STOCK)

    def update_stock(self,product) -> None:
        """
        Met à jour l'inventaire quand l'utilisateur ajoute un produit à sa commande
        :param product: Le produit ajouté à la commande
        """
        for item in self.stock:
           if product.id == item.id:
               if  item.quantity == 0:
                   print(f"Plus {product.name} disponible en stock, veuillez choisir un autre produit")
               elif  item.quantity >= product.quantity:
                   item.quantity = item.quantity - product.quantity
               elif item.quantity <= product.quantity:
                   print (f"pas assez de {product.name} disponible en stock, veuillez réduire la quantité")



    def print_inventory(self) -> None:
        """
        Affiche l'inventaire
        """
        print(f"voici l'état du stock")
        for item in self.stock:
          print(f"- {item.id:<3}{item.name:<19} {item.quantity:>3} {item.unit:<6}")




