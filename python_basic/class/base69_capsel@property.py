# getter,setter
class Human:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print("getter nameが呼ばれました")
        return self.__name

    @property
    def age(self):
        print("getter ageが呼ばれました")
        return self.__age

    @name.setter
    def name(self, name):
        print("setter nameが呼ばれました")
        self.__name = name

    @age.setter
    def age(self, age):
        print("setter ageが呼ばれました")
        if age < 0:
            print("0以上の値を設定してください")
            return
        self.__age = age


human = Human("shogo", 32)
print(human.name)
human.name = "moriyama"
print(human.name)
