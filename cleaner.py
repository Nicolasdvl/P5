class Cleaner:

    def cleaner(data):
        table = {}
        for pos, element in enumerate(data):
            prod = data[pos]
            table[pos] = { 'code' : prod.get('code'),
                    'product' :{
                        'name' : prod.get('product_name'),
                        'ingredients' : prod.get('ingredients_text_fr'),
                        'brands' : prod.get('brands'),
                        'labels' : prod.get('labels'),
                        'score' : prod.get('nutriscore_grade')
                    },
                    'stores' :{},
                    'categories':{}
            }
            stores = data[pos]['stores'].split(',')
            for pos_2, element_2 in enumerate(stores):
                if stores[pos_2] != None :
                    table[pos]['stores'][pos_2] = stores[pos_2]

            categories = data[pos]['categories'].split(',')
            for pos_2, element_2 in enumerate(categories):
                if categories[pos_2] != None :
                    table[pos]['categories'][pos_2] = categories[pos_2]
        return table
