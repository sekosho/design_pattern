# ポリモーフィズム

from abc import ABCMeta, abstractmethod


class Human(metaclass=ABCMeta):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(f"私の名前は{self.name}")


class Woman(Human):
    def say_something(self):
        print(f"女性：私の名前は{self.name}です")


class Man(Human):
    def say_something(self):
        print(f"男性：私の名前は{self.name}です")


# ポリモーフィズム
num = input("0か1を入力してください")
if num == "0":
    human = Man("Taro")
elif num == "1":
    human = Woman("Hanako")
else:
    print("入力が間違っています")

human.say_something()
