class Car:
    """
    車クラス
    """

    country = "japan"
    year = 2019
    name = "Prius"  # プロパティ

    def print_name(self):
        print(self.name)


my_car = Car()  # インスタンス化
print(my_car.year)
my_car.print_name()
list_a = ["apple", "orange", Car()]
print(my_car.year)
# second_car = list_a[2]()
# second_car.print_name()
list_a[2].print_name()
help(Car)
