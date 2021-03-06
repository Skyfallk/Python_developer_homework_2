"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return simbol*count

def input_fl_chek(count):
    try:
        count = float(count)
        if count > 0:
            return count
        else:
            print('Ошибка! Введите положительное число.\n')
            return False

    except:
        print('Ошибка! Введите положительное число.\n')
        return False

def top_up():
    global account
    count = input_fl_chek(input('Введите сумму на которую хотите пополнить счет\n'))
    if count != False:
        account += count
        print('Счет успешно пополнен на', count)

def buy():
    global account, history
    buy_name = input('Введите название покупки\n')
    buy_cost = input_fl_chek(input('Введите стоимость покупки\n'))
    if buy_cost != False:
        if buy_check(buy_cost):
            history.append((buy_name, buy_cost))
            account -= buy_cost
            print('Покупка успешно сохранена.\n')

def get_history():
    global history
    for n, buy in enumerate(history):
        print(separator('-', 10))
        print('№', n+1)
        print('Название:', buy[0])
        print('Стоимость:', buy[1])
    print(separator('-', 10))
    input('Нажимте enter для перехода в Главное меню.\n')

def buy_check(cost):
    global account
    if cost > account:
        print('Нельзя совершить покупку! Нехватает денег на счету.')
        return False
    else:
        return True

def personal_bill():
    global account, history
    while True:

        print('На счету ', account)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню\n')
        if choice == '1':
            top_up()
        elif choice == '2':
            buy()
        elif choice == '3':
            get_history()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

account = 0
history = []

if __name__ == '__main__':
    personal_bill()
