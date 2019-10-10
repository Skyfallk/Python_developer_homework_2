age = '1799'
day = '6.06'
input_age = input('Введите год рождения Пушкина А.С.\n')
while age != input_age:
    input_age = input('Неверный год. Попробуйте еще.\n')

input_day = input('Введите день рождения в формате ДД.ММ\n')
while input_day != day:
    input_day = input('Неверно. попробуйте щее раз.Введите день рождения в формате ДД.ММ\n')
print('Верно')