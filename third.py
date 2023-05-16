from tkinter import *
from tkinter import ttk


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.old_rating = rating

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name} \nТип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт!')

    def rating_update(self, new_rating):
        self.old_rating = new_rating
        print(f'Рейтинг {self.restaurant_name} изменился на {self.old_rating}')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, flavors, location, work_time):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.work_time = work_time

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name} \nТип кухни: {self.cuisine_type} \nАдрес: {self.location} \nВремя работы: {self.work_time} \nРейтинг заведения: {self.old_rating}')

    def flavors_list(self):
        return self.flavors

    def add_flavor(self, new_flavors):
        new_flavors = new_flavors.split(', ')
        if isinstance(new_flavors, str):
            self.flavors.append(new_flavors)
        elif isinstance(new_flavors, list):
            for i in new_flavors:
                if i not in self.flavors:
                    self.flavors.append(i)
        print('Вкусы с учетом добавления новых:')
        for i in self.flavors:
            print(i)

    def del_flavor(self, del_flavors):
        if isinstance(del_flavors, str):
            self.flavors.remove(del_flavors)
        elif isinstance(del_flavors, list):
            for i in del_flavors:
                if i in self.flavors:
                    self.flavors.remove(i)
        print('Вкусы с учетом удаления:')
        for i in self.flavors:
            print(i)

    def flavor_check(self, flavor):
        if flavor in self.flavors:
            print(f'Мороженное со вкусом {flavor} есть в наличии!')
        else:
            print(f'К сожалению, мороженного со вкусом {flavor} нет в наличии :(')


rest = IceCreamStand('Holy Moly', 'Мороженое', '4.6',
                     ['Клубничный', 'Ванильный', 'Шоколадный', 'Фисташковый', 'Банановый'], 'Думская, 39',
                     '10:00-22:00')



flavs = rest.flavors_list()

window = Tk()
window.title('Holy Moly')

lbl = Label(text='Список всех существующих вкусов:')
lbl.pack()

flav_var = Variable(value=flavs)
flav_listbox = Listbox(listvariable=flav_var)
flav_listbox.pack()

window.mainloop()
