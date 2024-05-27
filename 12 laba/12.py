def task1():
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

    class IceCreamStand(Restaurant):
        def __init__(self, flavors):
            self.flavors = flavors

        def describe_flavors(self):
            for i in self.flavors:
                print(i)

    icecream = IceCreamStand(['пломбир', 'шоколадное'])
    icecream.describe_flavors()

def task2():
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

    class IceCreamStand(Restaurant):
        def __init__(self, flavors, location, worktime):
            self.flavors = flavors
            self.location = location
            self.worktime = worktime

        def add_flavors(self):
            self.flavors.append(input('Введите вкус, кот-й хотите добавить: '))

        def delete_flavors(self):
            self.flavors.remove(input('Введите вкус, кот-й хотите удалить: '))

        def describe_flavors(self):
            for i in self.flavors:
                print(i)

        def check_flavors(self):
            a = input('Введите вкус, кот-й хотите проверить: ')
            if a in self.flavors:
                print(f'Вкус "{a}" есть в меню')
            else:
                print(f'Вкусa "{a}" нет в меню')

    icecream = IceCreamStand(['пломбир', 'шоколадный', 'ванильный'], 'Primorskaya 24', '08:00-22:00')
    icecream.add_flavors()
    icecream.delete_flavors()
    icecream.check_flavors()
    icecream.describe_flavors()

def task3():
    import tkinter as tk
    class IceCreamStand:

        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def create_gui(self):
            self.window = tk.Tk()          #создаём окно
            self.window.title(self.name)
            self.window.geometry('400x300')

            self.flavors_frame = tk.Frame(self.window, padx = 10, pady = 10) #создаём рамку для списка вкусов
            self.flavors_frame.pack(expand = True)

            self.flavors_label = tk.Label(self.flavors_frame, text='Выберите вкус:') #создаём заголовок
            self.flavors_label.grid(row=1,column=1)

            self.flavors_listbox = tk.Listbox(self.flavors_frame) #создаём листбокс
            self.flavors_listbox.grid(row=3, column=1)

            self.order_label = tk.Label(self.flavors_frame, text='Ваш заказ:')     #заголовок
            self.order_label.grid(row=1, column=5)

            self.order_list = tk.Listbox(self.flavors_frame)       #листбокс с заказом
            self.order_list.grid(row=3, column=5)

            for flavor in self.flavors:                              #заполняем листбокс c меню
                self.flavors_listbox.insert(tk.END, flavor)

            self.add_button = tk.Button(self.flavors_frame, text="Добавить в заказ", command=self.add_flavor) #кнопка добавления вкуса в заказ
            self.add_button.grid(row=3, column=2)
            self.remove_button = tk.Button(self.flavors_frame, text="Убрать из заказа", command=self.remove_flavor) #удалить вкус
            self.remove_button.grid(row=4, column=2)

            self.order_button = tk.Button(self.flavors_frame, text="Заказ", command=self.place_order)
            self.order_button.grid(row=4, column=5)

            self.close_button = tk.Button(self.window, text="Закрыть", command=self.window.destroy) #кнопка закрыть
            self.close_button.pack()

            self.window.mainloop()

        def add_flavor(self):
            selected_flavor = self.flavors_listbox.get(tk.ACTIVE)
            self.order_list.insert(tk.END, selected_flavor)

        def remove_flavor(self):
            selected_flavor = self.order_list.get(tk.ACTIVE)
            self.order_list.delete(tk.ACTIVE)

        def place_order(self):
            print("Вы заказали: ")
            s = []
            for i in self.order_list.get(0, tk.END):
                s.append(i)
                print(f' - {i}')
            tkinter.messagebox.showinfo(title='Ваш заказ: ', message=[i for i in s])

    ice_cream_stand = IceCreamStand("IceCreamWorld", ["шоколадное", "ванильное", "клубничное", "банановое", "пломбир"])
    ice_cream_stand.create_gui()


task1()
task2()
task3()