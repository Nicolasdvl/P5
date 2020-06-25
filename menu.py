class Menu:

    def __init__ (self):
        self.cmd_state_1 = {
            '1' : 'Installer le programme',
            '2' : 'Utiliser le programme',
            '0' : 'Quitter le programme'
        }
        self.cmd_state_2 = {
            '1' : 'Trouver un aliment',
            '2' : 'Afficher les substitus enregistrés',
            '0' : 'Retour'
        }
        self.cmd_state_3 = {}
        self.cmd_state_4 = {}
        
    def menu_state_1(self, App):

        while True :

            for key, element in self.cmd_state_1.items() :
                print (f'{key} : {element}')

            entry = input('Entrer un chiffre pour sélectionner l\'option correspondante : ')

            if entry == '1':
                App.create_db()

            elif entry == '2':
                self.menu_state_2(App)

            elif entry == '0':
                break
            
            else:
                print('Commande non reconnu')

    def menu_state_2(self, App):

        while True :

            for key, element in self.cmd_state_2.items() :
                print (f'{key} : {element}')

            entry = input('Entrer un chiffre pour sélectionner l\'option correspondante : ')

            if entry == '1' :
                self.menu_state_3(App)
            
            elif entry == '2' :
                print('substituts')

            elif entry == '0' :
                break 

            else :
                print('Commande incorrecte')

    def menu_state_3(self, App):

        while True :

            self.cmd_state_3 = App.view_cat()
            for key, element in self.cmd_state_3.items() :
                print (f'{key} : {element}')

            entry = input('Entrer un chiffre pour sélectionner la catégorie correspondante : ')
            
            if entry in self.cmd_state_3 :
                if entry == '0':
                    break
                else :
                    #self.menu_state_4(App, entry)
                    print('categorie ok')
                    break

            else :
                print('Commande incorrecte')
            
    def menu_state_4(self, App, entry):

        while True :

            self.cmd_state_4 = App.view_prod(entry)
    