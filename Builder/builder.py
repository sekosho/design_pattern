# Builderパターン
from abc import ABC, abstractclassmethod, abstractproperty


# Product
class SetMeal:
    @property
    def main_dish(self):
        return self.__main_dish
