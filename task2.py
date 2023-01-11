from hw import cook_book
from pprint import pprint


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict[str: dict]:
    ingreds_to_buy = {}
    for dish in dishes:
        for ingred in cook_book[dish]:
            if ingred['ingredient_name'] in ingreds_to_buy.keys():
                ingreds_to_buy['ingredient_name']['quantity'] += ingred['quantity']
            else:
                ingreds_to_buy[ingred.pop('ingredient_name')] = ingred
    for item in ingreds_to_buy.values():
        item['quantity'] *= 2
    return ingreds_to_buy

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

