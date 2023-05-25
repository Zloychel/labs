import tkinter as tk
def z1():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}, Кухня: {self.cuisine_type}")

    class IceCreamStand(Restaraunt):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print("Виды мороженного:")
            print(*self.flavors, sep = "\n")

    type_ice_cream = IceCreamStand("B U S I D O", "Японская", ["Пломбир", "Клубника", "Шоколад"])
    type_ice_cream.ice_flavors()

def z2():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name} | Кухня: {self.cuisine_type}")

    class IceCreamStand(Restaraunt):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def describe_ice_cafe(self):
            print(f"Ресторан: {self.restaurant_name} | Кухня: {self.cuisine_type} | Место: Токио, Япония | Время работы: 08:00 - 18:00")

        def ice_flavors(self):
            print("Виды мороженного:")
            print(*self.flavors, sep = "\n")

        def add(self):
            self.flavors.append(input("Добавить мороженое: "))

        def delete(self):
            self.flavors.remove(input("Удалить мороженное: "))

        def poisk(self):
            if input("Напишите вкус мороженного: ") in self.flavors:
                print("Есть в наличии")
            else:
                print("Нет в наличии")

    class ice_palochka(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, leight):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.leight = leight

        def palochka(self):
            print("Длина палочки: ", self.leight)

    class ice_stakan(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, height):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.height = height

        def stakan(self):
            print("Размер стакана: ", self.height)

    type_ice_cream = IceCreamStand("B U S I D O", "Японская", ["Пломбир", "Клубника", "Шоколад"], "Токио, Япония", "08:00 - 18:00")
    type_ice_cream.describe_ice_cafe()
    type_ice_cream.ice_flavors()
    type_ice_cream.poisk()

    p = ice_palochka("B U S I D O", "Японская", ["Пломбир", "Клубника", "Шоколад"], "Токио, Япония", "08:00 - 18:00", "10 см")
    p.palochka()

    s = ice_stakan("B U S I D O", "Японская", ["Пломбир", "Клубника", "Шоколад"], "Токио, Япония", "08:00 - 18:00", "Средний")
    s.stakan()

def z3():
    class IceCreamStand:
        def __init__(self):
            self.flavors = ["Пломбир", "Клубника", "Шоколаж"]
            self.prices = [50, 60, 70]

        def get_flavors(self):
            return self.flavors

        def get_prices(self):
            return self.prices

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("IceCreamStand")

            self.ice_cream_stand = IceCreamStand()

            self.flavors_label = tk.Label(master, text="Мороженое", font="Arial 12 bold")

            self.flavors_listbox = tk.Listbox(master, font="Helvetica 12", height=len(self.ice_cream_stand.get_flavors()))

            for flavor in self.ice_cream_stand.get_flavors():
                self.flavors_listbox.insert(tk.END, flavor)

            self.prices_label = tk.Label(master, text="Цена", font="Arial 12 bold")

            self.prices_listbox = tk.Listbox(master, font="Helvetica 12", height=len(self.ice_cream_stand.get_prices()))

            for price in self.ice_cream_stand.get_prices():
                self.prices_listbox.insert(tk.END, price)

            self.flavors_label.grid(row=0, column=0)
            self.flavors_listbox.grid(row=1, column=0)
            self.prices_label.grid(row=0, column=1)
            self.prices_listbox.grid(row=1, column=1)

    root = tk.Tk()
    ice = IceCreamStandGUI(root)
    root.mainloop()

z3()