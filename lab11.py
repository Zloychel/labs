def z1():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}, Кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} ОТКРЫТ")

    new_Restaurant = Restaraunt("B U S I D O","Японская")
    print(new_Restaurant.restaurant_name)
    print(new_Restaurant.cuisine_type)

    new_Restaurant.describe_restaurant() # Описание ресторана
    new_Restaurant.open_restaurant()     # Открыто/Закрыто

def z2():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}, Кухня: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} ОТКРЫТ")

    new_Restaurant1 = Restaraunt("B U S I D O","Японская")

    new_Restaurant2 = Restaraunt("P A R I S","Французская")

    new_Restaurant3 = Restaraunt("V I C T O R Y","Русская")

    o = input("Введите интересующую вас кухню: ")

    if o == str(new_Restaurant1.cuisine_type):
        new_Restaurant1.describe_restaurant()
        new_Restaurant1.open_restaurant()
    elif o == str(new_Restaurant2.cuisine_type):
        new_Restaurant2.describe_restaurant()
        new_Restaurant2.open_restaurant()
    elif o == str(new_Restaurant3.cuisine_type):
        new_Restaurant3.describe_restaurant()
        new_Restaurant3.open_restaurant()
    else:
        print("Такой кухни нет!")

def z3():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} ОТКРЫТ")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} был обновлен до  {self.rating}.")

    new_Restaurant = Restaraunt("B U S I D O","Японская",5)
    print(new_Restaurant.restaurant_name)
    print(new_Restaurant.cuisine_type)
    print(new_Restaurant.rating)

    new_Restaurant.describe_restaurant() # Описание ресторана
    new_Restaurant.open_restaurant()     # Открыто/Закрыто

    new_Restaurant.new_rating = int(input("Введите вашу оценку: "))
    new_Restaurant.update_rating(new_Restaurant.new_rating)
z1()