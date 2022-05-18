class Knife:
    def __init__(self, name) -> None:
        self.__name = name

    def cut_vegitables(self):
        print(f"野菜を{self.__name}でカットします")


class Boiler:
    def __init__(self, name) -> None:
        self.__name = name

    def boil_vegetables(self):
        print(f"野菜を{self.__name}でボイルします")


class Frier:
    def __init__(self, name) -> None:
        self.__name = name

    def fry_vegetables(self):
        print(f"野菜を{self.__name}でフライします")


class Cook:
    def __init__(self, knife: Knife, frier: Frier, boiler: Boiler) -> None:
        self.__knife = knife
        self.__frier = frier
        self.__boiler = boiler

    def cook_dishes(self):
        self.__knife.cut_vegitables()
        self.__frier.fry_vegetables()
        self.__boiler.boil_vegetables()


knife = Knife("My knife")
frier = Frier("My frier")
boiler = Boiler("My Boiler")
cook = Cook(knife, frier, boiler)
cook.cook_dishes()
