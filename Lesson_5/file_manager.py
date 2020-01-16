import sys
import os
import shutil

#полный путь к исполняемому файлу
script_directory = os.path.abspath(__file__)
#путь к рабочей дирректории
worked_directory = os.getcwd()

def create_directory(name, worked_directory):
    try:
        os.makedirs(os.path.join(worked_directory, name), exist_ok=False)
        print('Папка {} успешно создана'.format(name))
    except FileExistsError:
        print('Папка с названием "{}" уже существует.'.format(name))

def delete_dir_file(name, worked_directory):
    del_path = os.path.join(worked_directory, name)
    if os.path.isdir(del_path):
        try:
            os.rmdir(del_path)
            print('Папка "{}" успешно удалена.'.format(name))
        except OSError:
            while True:
                print('Папка не пуста. Хотите удалить её вместе со всем содержимым?')
                answer =  input('Да/Нет\n')
                if answer == 'Да':
                    shutil.rmtree(del_path)
                    print('Папка "{}" со всем содержимым удалена.'.format(name))
                    break
                elif answer == 'Нет':
                    break
                else:
                    print('Введите корректный ответ')

    elif os.path.isfile(del_path):
        os.remove(del_path)
        print('Файл "{}" успешно удален.'.format(name))
    else:
        print('Нет папки или файла с названием "{}".'.format(name))

def copy_dir(name, worked_directory):
    name_path = os.path.join(worked_directory, name)
    #print('name_path',name_path)
    if os.path.isdir(name_path):
        shutil.copytree(name_path, name_path + '(copy)')
        print('Папка "{}" успешно скопирована.'.format(name))
    elif os.path.isfile(name_path):
        f_name = os.path.basename(name_path)
        #print('f_name', f_name)
        #print('os.path.abspath(name_path)', os.path.abspath(name_path))
        shutil.copyfile(
            name_path,
            os.path.join(
                worked_directory, f_name[:f_name.index('.')] + '(copy)' + f_name[f_name.index('.'):]
                        ),
            follow_symlinks=True
            )
        print('Файл "{}" успешно скопирован.'.format(name))

def get_list_dir(worked_directory):
    #dir_list = os.listdir()
    print('<---------------------------------------->')
    for i, name in enumerate(os.listdir(worked_directory)):
        print(str(i) + ')', name)
    print('<---------------------------------------->')

def get_folders_list(worked_directory):
    folders_list = []
    print('<----------------- Папки ----------------->')
    for name in os.listdir(worked_directory):
        if os.path.isdir(os.path.join(worked_directory, name)):
            folders_list.append(name)
    for i, name in enumerate(folders_list):
        print(str(i) + ')', name)
    print('<----------------------------------------->')

def get_files_list(worked_directory):
    files_list = []
    print('<----------------- Файлы ----------------->')
    for name in os.listdir(worked_directory):
        if os.path.isfile(os.path.join(worked_directory, name)):
            files_list.append(name)
    for i, name in enumerate(files_list):
        print(str(i) + ')', name)
    print('<----------------------------------------->')

def get_OS_info():
    print(sys.platform, '(', os.name, ')')
print(script_directory)

