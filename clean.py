def clean_for_data(list):

    table = []
    for pos, element in enumerate(list):
        table.append((list[pos]["code"], list[pos]["product_name"], list[pos]["ingredients_text_fr"], list[pos]["labels"], list[pos]["nutriscore_grade"]))
    return table   

def clean_for_cat(list):

    table = []
    for pos, element in enumerate(list):
        for pos_2, element_2 in enumerate(list[pos]["categories_tags"]):
            table.append(list[pos]["categories_tags"][pos_2])
    return table 

def clean_for_store(list):

    table =[]
    for pos, element in enumerate(list):
        for pos_2, element_2 in enumerate(list[pos]["stores_tags"]):
            table.append(list[pos]["stores_tags"][pos_2])
    return table
