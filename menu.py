import random

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
        self.back = False
        
        
    def menu_state_1(self, App: object):
    
    ''' 
    Selection between installation or use 
    '''
    
        while True :

            for key, element in self.cmd_state_1.items() :
                print (f'{key} : {element}')

            entry = input('\nEntrer un chiffre pour sélectionner l\'option correspondante : ')

            if entry == '1':
                App.create_db()

            elif entry == '2':
                self.menu_state_2(App)

            elif entry == '0':
                break
            
            else:
                print('\nCommande non reconnu')

    def menu_state_2(self, App: object):
    
    ''' 
    Selection between product search or substitutes display
    '''
    
        while True :

            print('-'*50)
            for key, element in self.cmd_state_2.items() :
                print (f'{key} : {element}')

            entry = input('\nEntrer un chiffre pour sélectionner l\'option correspondante : ')

            if entry == '1' :
                self.menu_state_3(App)
                
            elif entry == '2' :
                save = App.view_save()
                print('-'*50+'\nSubstitut(s) enregistré(s) :\n') 
                for x in save:
                    print(x)

            elif entry == '0' :
                break 

            else :
                print('\nCommande incorrecte')

    def menu_state_3(self, App: object):

    ''' 
    Display 10 random categories and allow selction 
    '''

        while True :

            if self.back :
                break

            else :
                self.cmd_state_3 = App.view_cat()
                rand_cat = random.sample(list(self.cmd_state_3), 10)
                print('-'*50)
                for x in rand_cat :
                    print (f'{x} : {self.cmd_state_3[x]}')

                entry = input('\nEntrer un chiffre pour sélectionner la catégorie correspondante : ')
                
                if entry in self.cmd_state_3 :
                    if entry == '0':
                        break
                    else :
                        self.menu_state_4(App, entry)

                else :
                    print('\nCommande incorrecte')
            
    def menu_state_4(self, App: object, entry: str):
    
    ''' 
    Display product of the category chosen
    '''
    
        while True :

            if self.back :
                break

            else :
                self.cmd_state_4 = App.view_prod(entry)
                print('-'*50)
                for key, element in self.cmd_state_4.items() :
                    print (f'{key} : {element}')

                entry = input('\nEntrer un chiffre pour sélectionner le produit correspondant : ')

                if entry in self.cmd_state_4 :
                    if entry == '0':
                        break
                    else :
                        self.menu_state_5(App, entry)
                        
                        
                else :
                    print('\nCommande incorrecte')

    def menu_state_5(self, App: object, entry: str) :
    
    ''' 
    Display substiute found and allow it saving 
    '''

        while True :

            prod = self.cmd_state_4.get(entry)
            alt = App.search_alt(prod)
            sub = App.relevance(alt)
            print('-'*50)
            print(f'\nSubstitut trouvé pour le produit {prod} : {sub}')
            entry = input('\nVoulez vous enregistrer le substitut dans votre liste ? (y/n)')

            if entry == 'y':
                feedback = App.insert_sub(sub)
                print(feedback)
                self.back = True
                break

            elif entry == 'n':
                self.back = True
                break

            else :
                print('\nCommande incorrecte')
