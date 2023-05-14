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
    def __init__(self, restaurant_name, cuisine_type, rating, flavors):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors

    def flavors_list(self):
        print('Список всех существующих вкусов:')
        for i in self.flavors:
            print(i)


rest = IceCreamStand('Holy Moly', 'Мороженое', '4.6', ['Клубничный', 'Ванильный', 'Шоколадный', 'Фисташковый', 'Банановый'])
rest.flavors_list()
