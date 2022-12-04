import os
current = os.getcwd()
folder = 'test_file'
file_name = 'text_recept.txt'
full_path = os.path.join(current, folder, file_name)
print(f'Полный путь: {full_path}')


with open('text_recept.txt', 'r', encoding='utf-8') as file:
    file.read()