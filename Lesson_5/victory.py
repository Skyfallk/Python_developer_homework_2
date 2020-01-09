"""
Толстой Л.Н. 1828
Петр I 1672
Эйнштейн 1879
Гагарин Ю. 1934
Никулин Ю. 1921
"""
def victorina():
    names_and_years = [
        ('Толстого Л.Н.', '1828'),
        ('Петра I', '1672'),
        ('Эйнштейна', '1979'),
        ('Юрия Гагарина', '1934'),
        ('Юрия Никулина', '1921')
                      ]
    playing = True

    while playing == True:
        error_count = 0
        right_count = 0
        for i in names_and_years:
            year = input('Введите год рождения {}\n'.format(i[0]))
            if year == i[1]:
                right_count += 1
            else:
                error_count += 1
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
