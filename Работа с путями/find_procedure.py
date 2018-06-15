# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
#from chardet.universaldetector import UniversalDetector
import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def string_in_file(file_name, string):
        with open(file_name, 'r') as f:
            s = f.read()
        if string.lower() in s.lower():
            return True
        return False


def get_files_with_string(directory, file_list, string):
    result_list = []
    for i in file_list:

        if string_in_file(os.path.join(directory, i), string):
            print(os.path.join(migrations, i))
            result_list.append(i)
    return result_list




if __name__ == '__main__':

    fn = os.path.join(current_dir, migrations)
    files = [f for f in os.listdir(fn) if f.endswith('.sql')]

    while files:
        tmp_str = input('Введите строку:')
        files = get_files_with_string(os.path.join(current_dir, migrations), files, tmp_str)
        print(len(files))
    pass
