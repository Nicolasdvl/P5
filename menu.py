import random


class Menu:
    def __init__(self):
        self.cmd_select_mode = {
            "1": "Installer le programme",
            "2": "Utiliser le programme",
            "0": "Quitter le programme",
        }
        self.cmd_select_option = {
            "1": "Trouver un aliment",
            "2": "Afficher les substitus enregistrés",
            "0": "Retour",
        }
        self.cmd_categories = {}
        self.cmd_products = {}
        self.back = False

    def menu_select_mode(self, app: object) -> None:
        """Selection between installation or use."""
        while True:
            for key, element in self.cmd_select_mode.items():
                print(f"{key} : {element}")
            entry = input(
                "\nEntrer un chiffre pour sélectionner l'option correspondante : "
            )
            if entry == "1":
                app.create_db()
            elif entry == "2":
                self.menu_select_option(app)
            elif entry == "0":
                break
            else:
                print("\nCommande non reconnu")

    def menu_select_option(self, app: object) -> None:
        """Selection between product search or substitutes display."""
        while True:
            self.back = False
            print("-" * 50)
            for key, element in self.cmd_select_option.items():
                print(f"{key} : {element}")
            entry = input(
                "\nEntrer un chiffre pour sélectionner l'option correspondante : "
            )
            if entry == "1":
                self.menu_categories(app)
            elif entry == "2":
                save = app.view_save()
                print("-" * 50 + "\nSubstitut(s) enregistré(s) :\n")
                for prod, sub in save.items():
                    print(f"Produit {prod} substitué par {sub} ")
            elif entry == "0":
                break
            else:
                print("\nCommande incorrecte")

    def menu_categories(self, app: object) -> None:
        """Display 10 random categories and allow selection."""
        while True:
            if self.back:
                break
            else:
                self.cmd_categories = app.view_cat()
                rand_cat = random.sample(list(self.cmd_categories), 10)
                print("-" * 50)
                for x in rand_cat:
                    print(f"{x} : {self.cmd_categories[x]}")
                entry = input(
                    "\nEntrer un chiffre pour sélectionner la catégorie correspondante : "
                )
                if entry in self.cmd_categories:
                    if entry == "0":
                        break
                    else:
                        self.menu_products(app, entry)
                else:
                    print("\nCommande incorrecte")

    def menu_products(self, app: object, entry: str) -> None:
        """Display product of the category chosen."""
        while True:
            if self.back:
                break
            else:
                self.cmd_products = app.view_prod(entry)
                print("-" * 50)
                for key, element in self.cmd_products.items():
                    print(f"{key} : {element}")
                entry = input(
                    "\nEntrer un chiffre pour sélectionner le produit correspondant : "
                )
                if entry in self.cmd_products:
                    if entry == "0":
                        break
                    else:
                        self.menu_saving(app, entry)
                else:
                    print("\nCommande incorrecte")

    def menu_saving(self, app: object, entry: str) -> None:
        """Display substiute found and allow it saving."""
        while True:
            prod = self.cmd_products.get(entry)
            alt = app.search_alt(prod)
            sub = app.relevance(alt)
            print("-" * 50)
            print(f"\nSubstitut trouvé pour le produit {prod} : {sub}")
            entry = input(
                "\nVoulez vous enregistrer le substitut dans votre liste ? (y/n)"
            )
            if entry == "y":
                feedback = app.insert_sub(prod, sub)
                print(feedback)
                self.back = True
                break
            elif entry == "n":
                self.back = True
                break
            else:
                print("\nCommande incorrecte")
