"""
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран

Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4

Вывод: [2, 4, 5]
"""
while True:
    n = input("Введите количество элементов: ")
    try:
        n = int(n)
        break
    except:
        print("Пожалуйста введите целое число.")

list_ = []

print("Введите {} любых цифр".format(n))
for i in range(n):
    while True:
        element = input("Введите " + str(i+1) + " элемент: " )
        try:
            element = int(element)
            if element >= 0 and element < 10:
                list_.append(element)
                break
            else:
                print("Пожалуйста введите цифру от 0 до 9.")
        except:
            print("Пожалуйста введите цифру от 0 до 9.")
list_.sort()
print(list_)