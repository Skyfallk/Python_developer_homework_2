age = '1799'
day = '6.06'
input_age = input('Введите год рождения Пушкина А.С.\n')
if age == input_age:

    input_day = input('Введите день рождения в формате ДД.ММ\n')
    if input_day == day:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')