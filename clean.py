def clean_for_data(list):

    table = []
    for pos, element in enumerate(list):
        table.append((list[pos]["code"], list[pos]["product_name"], list[pos]["ingredients_text_fr"], list[pos]["labels"], list[pos]["nutriscore_grade"]))
    return table   

def clean_for_categories(list):

    table = []
    for pos, element in enumerate(list):
        table.append()
    return table  
