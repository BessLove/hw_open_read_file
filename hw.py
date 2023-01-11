def file_read(file_p: str) -> list[list[str]]:
    '''Функция группирует текст из файла в список вложенных списков,
     путем разделения элементов текста по переносу строки или двойному переносу строки'''
    with open(file_p, encoding='utf-8') as file_object:
        list_dish = []
        for element in file_object.read().split('\n\n'):
            list_dish.append(element.split('\n'))
    return list_dish


def dict_dish(some_list: list) -> list[dict[str]]:
    '''Функция формирует список словарей задавая им ключи,
     предварительно создав списоки из каждстроки с ингредиентом.
     Словари с игредиентами сгруппированы в списки по принадлежности к блюду.'''
    list_ingreds = []
    for i in some_list[2:]:
        ingred = dict(zip(['ingredient_name', 'quantity', 'measure'], i.split(' | ')))
        list_ingreds.append(ingred)
    return list_ingreds


def main(some_file: str) -> dict[str, list[dict[str]]]:
    '''Функция запускает программу '''
    list_dish = file_read(some_file)
    list_ingreds = [dict_dish(i) for i in list_dish]
    keys = [_[0] for _ in list_dish]
    vals = [_ for _ in list_ingreds]
    cook_book = dict(zip(keys, vals))
    return cook_book
cook_book = main('text.txt')


print(cook_book)
