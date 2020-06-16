class Cleaner():

    def cleaner_prod(data):

        table = []
        for pos, element in enumerate(data):
            table.append((data[pos]["code"], data[pos]["product_name"], data[pos]["ingredients_text_fr"], data[pos]["brands"], data[pos]["labels"], data[pos]["nutriscore_grade"]))
        return table   

    def cleaner_cat(data):

        table = []
        for pos, element in enumerate(data):
            for pos_2, element_2 in enumerate(data[pos]["categories_tags"]):
                table.append((data[pos]["categories_tags"][pos_2]))
        return table 

    def cleaner_store(data):

        table =[]
        for pos, element in enumerate(data):
            for pos_2, element_2 in enumerate(data[pos]["stores_tags"]):
                table.append(data[pos]["stores_tags"][pos_2])
        return table