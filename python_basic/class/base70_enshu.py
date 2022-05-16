from abc import abstractmethod, ABCMeta


class Animals(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animals):
    def speak(self):
        print("わん")


class Cat(Animals):
    def speak(self):
        print("にゃー")


class Sheep(Animals):
    def speak(self):
        print("めー")


class Other(Animals):
    def speak(self):
        print("そんな動物いない")


num = input("どの動物の鳴き声が聞きたいですか？1:犬、2:猫、3:羊\n")
if num == "1":
    animal = Dog()
elif num == "2":
    animal = Cat()
elif num == "3":
    animal = Sheep()
else:
    animal = Other()

animal.speak()  # ポリモーフィズム
