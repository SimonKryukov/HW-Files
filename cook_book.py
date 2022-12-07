import os
current = os.getcwd()
folder = 'test_file'
file_name = 'text_recept.txt'
full_path = os.path.join(current, folder, file_name)
print(f'Полный путь: {full_path}')

with open('text_recept.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_count = int(file.readline())
        ingridients = []
        cook_book[dish_name] = ingridients
        for ingridient in range(dish_count):
            recipe = file.readline().strip()
            ing, quan, meas = recipe.split(' | ')
            ingridients.append({
                'ingridient_name': ing,
                'quantity': int(quan),
                'measure': meas
            })
        file.readline()
    
    from pprint import pprint

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for ingridient in cook_book[dish]:
                shop_list_item = dict(ingridient)
                shop_list_item['quantity'] *= person_count
                if shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[shop_list_item['ingridient_name']] = shop_list_item
                else:
                    shop_list[shop_list_item['ingridient_name']]['quantity'] += shop_list_item['quantity']
                del shop_list_item['ingridient_name']
        return shop_list
    
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    

    

            

    
    
    



   
    # def get_cook_book():
    #     cook_book = {}
    #     key_list = []
    #     for dish in file:
    #         if "\n" in dish:
    #             dish = dish[: dish.index("\n")]
    #         dish = dish.strip()
    #         dish_count = int(file.readline())
    #         key_list.append(dish)
    #         ingridients = []
    #         for ingridient in range(dish_count):
    #             ingridient = file.readline().strip()
    #             ing, quantity, measure = ingridient.split(' | ')
    #             ingridients.append({
    #                 'ingredient_name': ing,
    #                 'quantity': quantity,
    #                 'measure': measure
    #             })
    #         file.readline()
    #     cook_book = dict.fromkeys(key_list, ingridients)
    #     return cook_book

    # def find_by_key(iterable, key, value):
    #     for index, dict_ in enumerate(iterable):
    #         if key in dict_ and dict_[key] == value:
    #             return (index, dict_)
    
    # def find_all_by_key(iterable, key, value):
    #     for index, dict_ in enumerate(iterable):
    #         if key in dict_ and dict_[key] == value:
    #             yield (index, dict_)
    
    # print(find_by_key(['Омлет'], 'ingredient_name', '' ))
    
