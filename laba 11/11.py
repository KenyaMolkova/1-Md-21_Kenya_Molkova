def task1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f'Ресторан {self.restaurant_name}:  {self.cuisine_type} кухня')
        def open_restaurant(self):
            print(f'Ресторан {self.restaurant_name} открыт')

    newRestaurant = Restaurant(input("Введите имя ресторана: "), input("Введите тип кухни: "))
    
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f'Ресторан {self.restaurant_name}:  {self.cuisine_type} кухня')
        def open_restaurant(self):
            print(f'Ресторан {self.restaurant_name}  открыт')
            
    newRestaurant1 = Restaurant("Tokyo City", "Японская")
    newRestaurant2 = Restaurant("Babooshka", "Русская")
    newRestaurant3 = Restaurant("Bonjour", "Французская")

    newRestaurant1.describe_restaurant()
    newRestaurant2.describe_restaurant()
    newRestaurant3.describe_restaurant()

def task3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
                print(f'Ресторан {self.restaurant_name}:  {self.cuisine_type} кухня')
        def open_restaurant(self):
                print(f'Ресторан {self.restaurant_name} открыт')
        def newRating(self, new_rating):
            self.rating = new_rating
            print(f'Рейтинг: {self.rating} звёзд')
            
    newRestaurant1 = Restaurant("Tokyo City", "Японская")
    newRestaurant2 = Restaurant("Babooshka", "Русская")
    newRestaurant3 = Restaurant("Bonjour", "Французская")

    newRestaurant1.describe_restaurant()
    newRestaurant1.newRating(2)
    
    newRestaurant2.describe_restaurant()
    newRestaurant2.newRating(3)
    
    newRestaurant3.describe_restaurant()
    newRestaurant3.newRating(5)
    
