import os
current = os.getcwd()
folder = 'test_file'
file_name = 'text_recept.txt'
full_path = os.path.join(current, folder, file_name)
print(f'Полный путь: {full_path}')


def get_cook_book():
    with open('text_recept.txt', 'r', encoding='utf-8') as file:
        cook_book = {}
        key_list = []
        for dish in file:
            if "\n" in dish:
                dish = dish[: dish.index("\n")]
            dish = dish.strip()
            dish_count = int(file.readline())
            key_list.append(dish)
            ingridients = []
            for ingridient in range(dish_count):
                ingridient = file.readline().strip()
                ing, quantity, measure = ingridient.split(' | ')
                ingridients.append({
                    'ingredient_name': ing,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
        cook_book = dict.fromkeys(key_list, ingridients)
    return print(f"cook_book =  {cook_book}")

print(get_cook_book())

# for key, value in sorted(get_cook_book().items(), key=lambda x: x[1]):
#     print(f"{key} : {value}")

