class UserInput:
    """
    Gère toutes les interactions utilisateur
    """

    @staticmethod
    def is_non_empty(msg:str) -> str:
        while True:
            choice = input(msg).strip()
            if choice:
                return choice
            print("Veuillez rentrer une valeur non vide")
    @staticmethod
    def is_int(msg:str) -> str | None:
        while True:
            choice = input(msg).strip()
            if not choice.isdigit():
                print("Veuillez entrer un nombre entier.")
                continue
            return choice