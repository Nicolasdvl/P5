class Cleaner:

    def cleaner_prod(data):

        ''' data : product list collected in 'collect()'
            Clean the list and arrange it in aim to insert it in the product table '''

        table = []
        for pos, element in enumerate(data):
            table.append((data[pos]["code"], data[pos]["product_name"], data[pos]["ingredients_text_fr"], data[pos]["brands"], data[pos]["labels"], data[pos]["nutriscore_grade"]))
        return table   

    def cleaner_cat(data):

        ''' data : product list collected in 'collect()'
            Clean the list and arrange it in aim to insert it in the category table '''

        table = []
        for pos, element in enumerate(data):
            cat = data[pos]["categories"].split(',')
            for pos_2, element_2 in enumerate(cat):
                table.append(cat[pos_2].strip())
        return table 

    def cleaner_store(data):

        ''' data : product list collected in 'collect()'
            Clean the list and arrange it in aim to insert it in the store table '''

        table =[]
        for pos, element in enumerate(data):
            store = data[pos]["stores"].split(',')
            for pos_2, element_2 in enumerate(store):
                table.append(store[pos_2].strip())
        return table