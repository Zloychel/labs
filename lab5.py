def z1():
    n = [1, 2, 3, 4, 5]
    c = int(input("Введите число: "))
    if c in n:
        print("Поздравляю! Вы угадали число!")
    else:
        print("Нет такого числа!")

def z2():
    lst = [1, 2, 2, 3, 4, 4, 5, 6, 7]
    print(*filter(lambda x: lst.count(x) > 1, lst))

def z3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    n = int(input("Сколько нужно выходных дней? "))
    if n == 0:
        print("Выходных нет")
        print("Рабочие дни: ", *week)
    else:
        print("Выходные: ", *week[-n:])
        print("Рабочие дни: ", *week[:-n])

def z4():
    s_1 = ['Иванов', 'Петров', 'Дубкин', 'Шишкин']
    s_2 = ['Иванова', 'Петрова', 'Дубкина', 'Шишкина']
    s = tuple(s_1 + s_2)
    print("Первый список: ", *s_1)
    print("Второй список: ", *s_2)
    print("Новый кортеж: ", *sorted(s))
    print("Длина кортежа: ", len(s))
    print(s.count('Иванов'))