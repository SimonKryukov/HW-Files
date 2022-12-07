import os
current = os.getcwd()
folder = 'test_file'
file_name = 'text_recept.txt'
full_path = os.path.join(current, folder, file_name)

# print(f'Полный путь: {full_path}')

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
    
    # pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    
def len_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        result = len(f.readlines())
    return result

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        file_list = []
        file_list.append(file), file_list.append(str(len_file(file)))
        for line in f:
            if "\n" in line:
                pos = line.index("\n")   # приходится убирать с каждой строки \n потому что он делает лишнии пробелы между строк, где
                a = line[:pos]           # задвоены \n
                file_list.append(a)
            else:
                file_list.append(line)
        return file_list

f = []
f.append(read_file('2.txt'))
f.append(read_file('1.txt'))
f.append(read_file('3.txt'))
f = [j + '\n' for line in f for j in line]

with open('4.txt', 'w', encoding='utf-8') as file:
    file.writelines(f)
