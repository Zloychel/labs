def z1():
    a = input("Введите цвета в форме (красный и синий = rb) （красный и желтый = rj） （синий и желтый = bj): ")
    if (a == "rb") or (a == "br"):
        print("фиолетовый")
    elif (a == "rj") or (a == "jr"):
        print("оранжевый")
    elif (a == "bj") or (a == "jb"):
        print("зеленый")

def z2():
    a = input("Введите пароль: ")
    b = input("Подтвердите пароль: ")

    if a == b and len(a) >= 5:
        print("Пароли совпадают")
        if a[0:6] == "qwerty":
            print("Пароль ненадежный!")
    else:
        print("Пароли не совпадают!")

def z3():
    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 36:
        print('Ваше место - боковое.')
    elif n % 2:
        print('Ваше место в купе внизу.')
    else:
        print('Ваше место в купе наверху.')

def z4():
    s = int(input("Количество слов "))
    n = str("")
    word = str("")
    for i in range(s):
        word = input("СЛОВА")
        n = n + " " + word
    print(n)

def z5():
    god = int(input("Введите год: "))

    if (god % 4 == 0) and (god % 100 != 0):
        print("Высокосный")
    else:
        print("Нет")

