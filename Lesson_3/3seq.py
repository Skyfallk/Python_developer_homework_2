while True:
    input_str_1 = input("Введите первый набор цифр. Любое количесвто цифр через ',', ';' или '/': ")
    input_str_2 = input("Введите второй набор цифр. Любое количесвто цифр через ',', ';' или '/': ")
    c = 0
    for i in [',', ';', '/']:
        if input_str_1.find(i) != -1:
            separator_1 = i
            c += 1
        if input_str_2.find(i) != -1:
            separator_2 = i
            c += 1
    if c == 0:
        print('Не наден ни один из допустимых разделителей в обоих списках.')
    elif c == 1:
        print('Не наден ни один из допустимых разделителей одном из сисков.')
    elif c == 2:
        list_1 = input_str_1.split(separator_1)
        list_2 = input_str_2.split(separator_2)
        try:
            list_1 = [int(i) for i in list_1]
            list_2 = [int(i) for i in list_2]
            set_1 = set(list_1)
            set_2 = set(list_2)
            result_1 = list(list(set_1))
            result_2 = list(list(set_2))
            chek_1 = [i // 10 for i in result_1]
            chek_2 = [i // 10 for i in result_2]
            if max(chek_1) >= 1 or max(chek_2) >= 1 :
                print('Проверьте ввод списков. Числа вводить нельзя, только цифры от 0 до 9.')
            else:
                print(list(set_1.difference(set_2)))
                break
        except:
            print('Проверьте что вы ввели цифры')
    else:
        print('Использованы разные разделители. Введите цифры используя один из допустимых разделитедей.')