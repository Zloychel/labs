def z1():
    spisok = []
    word = input("Введите слово: ")
    while word != "stop":
        spisok += word.split()
        word = input("Введите слово: ")
        continue
    print(spisok)

def z2():
    word = input("Введите слово: ")
    f = "ф"
    if f in word:
        print("Ого, это редкое слово!")
    else:
        print("Эх, это не редкое слово!")

def z3():
    import random
    life = 3
    answer = 0
    while life <= 3:
        if life == 0:
            print(f"Игра окончена! Правильных ответов: {answer}")
            break
        chislo1 = random.randint(0, 9)
        chislo2 = random.randint(0, 9)
        v = chislo1 + chislo2
        v2 = int(input(f"Кол-во жизней: {life}. {chislo1} + {chislo2}? Ответ: "))
        if v == v2:
            print("Верно!")
            answer += 1
        else:
            print("Неверно!")
            life -= 1
        continue