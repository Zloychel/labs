def z1():
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Введено не число!")
    else:
        if number % 3 == 0:
            print(f"{number} делится на 3")
        elif number == 0:
            print("Введен 0!")
        else:
            print(f"{number} не делится на 3")

def z2():
    try:
        n = int(input("Введите число: "))
        v = 100 / n
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("Введен 0!")
    else:
        print(f"100 : {n} = {v}")

def z3():
    d = input("Введите дату: ")
    d = d.split(".")
    if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
        print("Дата магическая, ура!")
    else:
        print("Дата не магическая")

def z4():
    ch = input("Введите номер билета: ")
    x = 0
    y = 0
    if len(ch) % 2 == 0:
        for i in ch[0:int(len(ch) / 2)]:
            x = x + int(i)
        for i in ch[int(len(ch) / 2):int(len(ch)) + 1]:
            y = y + int(i)
        if x == y:
            print("Билет счастливый!")
        else:
            print("Билет не является счастливым!")
    else:
        print("Количество цифр нечётно!")