from victory import victorina
from personal_bill import personal_bill
import file_manager as fm
import os

def show_worked_dir(worked_directory, description = "Рабочая дирректория:"):
    symbols = len(description + worked_directory)

    print('-' * symbols)
    print(description, worked_directory)
    print('-' * symbols)

def main():
    script_directory = os.path.split(os.path.abspath(__file__))[0]
    worked_directory = os.getcwd()
    blocks = ['Создать папку',
              'Удалить файл/папку',
              'Копировать файл/папку',
              'Посмотреть содержиое рабочей дирректории',
              'Посмотреть только папки',
              'Посмотреть только файлы',
              'Просмотр информации об операционной системе',
              'Создатель программы',
              'Играть в "Викторину"',
              'Мой банковский счет',
              'Смена рабочей дирректории',
              'Выход']
    exit = 0
    while exit == 0:
        show_worked_dir(worked_directory)
        for n,item in enumerate(blocks):
            print(str(n+1)+'.', item)
        choose_item = int(input())
        if choose_item == 9:
            victorina()

        elif choose_item == 1:
            new_dir = input('Введите название новой папки\n')
            fm.create_directory(name=new_dir, worked_directory=worked_directory)

        elif choose_item == 2:
            del_dir = input('Введите название папки или файла который хотите удалить\n')
            fm.delete_dir_file(del_dir, worked_directory)

        elif choose_item == 3:
            copy_name = input('Введите название папки/файла который хотите скопировать\n')
            fm.copy_dir(copy_name, worked_directory)

        elif choose_item == 4:
            fm.get_list_dir(worked_directory)

        elif choose_item == 5:
            fm.get_folders_list(worked_directory)

        elif choose_item == 6:
            fm.get_files_list(worked_directory)

        elif choose_item == 7:
            fm.get_OS_info()

        elif choose_item == 8:
            print("Кириллов Евгений Вадимович")

        elif choose_item == 11:
            new_worked_directory = input("Введите новую рабочую дирректорию\n")
            if new_worked_directory in os.listdir(script_directory):
                worked_directory = os.path.join(script_directory, new_worked_directory)
                print('Новая рабочая дирректория', worked_directory)
            elif os.path.isdir(new_worked_directory):
                worked_directory = new_worked_directory
                print('Новая рабочая дирректория', worked_directory)
            elif os.path.isdir(os.path.join(worked_directory, new_worked_directory)):
                worked_directory = os.path.join(worked_directory, new_worked_directory)
                print('Новая рабочая дирректория', worked_directory)
            else:
                print('Такой дирректории не существует. Проверьте правильность ввода или создайте необходимую дирректорию.')
        elif choose_item == 10:
            personal_bill()

        elif choose_item == 12:
            exit = 1

        else:
            print('В разработке')

if __name__ == '__main__':
    main()

