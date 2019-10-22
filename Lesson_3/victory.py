"""
Толстой Л.Н. 1828
Петр I 1672
Эйнштейн 1879
Гагарин Ю. 1934
Никулин Ю. 1921
"""
import random

names_and_years = [
    ('Толстого Л.Н.', '28.08.1828', 'двадцать восьемое августа 1828 года'),
    ('Петра I', '30.05.1672', 'тридцатое мая 1972 года'),
    ('Эйнштейна', '14.03.1879', 'четырнадцатое марта 1879 года'),
    ('Юрия Гагарина', '09.04.1934', 'девятое мая 1934 года'),
    ('Юрия Никулина', '18.12.1921', 'восемнадцатое декабря 1921 года'),
    ('Эрнесто Че Гевара', '14.07.1928', 'четырнадцатое июля 1928 года'),
    ('Курта Кобейна', '20.02.1967', 'двадцатое февраля 1967 года'),
    ('Стивена Хокинга', '08.01.1942', 'восьмое января 1942 года'),
    ('Сергея Павловича Королева', '30.12.1906', 'тридцатое декабря 1906 года'),
    ('Майкла Джексона', '29.08.1958', 'двадцать девятое августа 1958 года')
                  ]
playing = True
samples_count = 5


while playing == True:
    print("""Приветствуем Вас в игре "Викторина"! 
Мы загадали даты рождения знаментиостей, посмотрим соклько сможете угадать.
Даты нужно в водить в формате ДД.ММ.ГГ.
Например:
Вопрос: Дата рождения С.А. Пушкина
Ответ: 29.01.1799
Желаем удачи!
    """)
    sampels = random.sample(names_and_years, samples_count)
    error_count = 0
    right_count = 0
    for i in sampels:
        year = input('Введите дату рождения {}\n'.format(i[0]))
        if year == i[1]:
            right_count += 1
        else:
            error_count += 1
            print('Правильный ответ:', i[2])
    print('Всего ошибок:', error_count)
    print('Всего правильных ответов', right_count)
    print('Процент правильных ответов', int(right_count / len(names_and_years) * 100 ))
    while True:
        continue_ = input('Если хотите попробовать еще раз, введите "Да", если хотите закончить, введите "Нет"\n')
        if continue_ == 'Да':
            playing = True
            break
        elif continue_ == 'Нет':
            playing = False
            break
        else:
            print('Не верный ввод')