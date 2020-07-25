class Cleaner:

    def cleaner(data: list) -> dict:

        ''' 
        Clean and formate api request 

        data format :
            x : {
                'code' :
                'product' : {
                    'name' : 
                    'ingredients' :
                    'brands' :
                    'labels' :
                    'score' :
                }
                'stores' : {
                    'x' :
                    'y' :
                }
                'categories' : {
                    'x' :
                    'y' :
                }
            }  
            y : {
                .
                .
                .
        '''

        table = {}
        for pos, element in enumerate(data):
            prod = data[pos]
            table[pos] = { 'code' : prod.get('code'),
                    'product' :{
                        'name' : prod.get('product_name', 'unamed'),
                        'ingredients' : prod.get('ingredients_text_fr'),
                        'brands' : prod.get('brands'),
                        'labels' : prod.get('labels'),
                        'score' : prod.get('nutriscore_grade')
                    },
                    'stores' :{},
                    'categories':{}
            }
            if data[pos].get('stores') :
                stores = data[pos]['stores'].split(',')
                for pos_2, element_2 in enumerate(stores):
                    if stores[pos_2] != None :
                        table[pos]['stores'][pos_2] = stores[pos_2]

            if data[pos].get('categories') :
                categories = data[pos]['categories'].split(',')
                for pos_2, element_2 in enumerate(categories):
                    if categories[pos_2] != None :
                        add = categories[pos_2]
                        table[pos]['categories'][pos_2] = add.strip()

        return table
