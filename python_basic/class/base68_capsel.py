# getter,setter
class Human:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def get_name(self):
        print("getter __nameを呼び出しました")
        return self.__name

    def set_name(self, name):
        print("setter __nameをsetしました")
        self.__name = name

    def get_age(self):
        print("getter __ageを呼び出しました")
        return self.__age

    def set_age(self, age):
        print("setter __ageをsetしました")
        self.__age = age

    # name = property(get_name, set_name)  # nameを指定するとget_name, set_nameが呼び出されるようになる
    # age = property(get_age, set_age)

    def print_msg(self):
        print(f"{self.name},{self.age}")


human = Human("shogo", "32")
human.name = "moriyama"
print(human.name)
# print(human.__name)
