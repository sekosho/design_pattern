class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greeting(self):
        print(f"{self.name}といいます。よろしくお願いいたします。")

    def say_age(self):
        print(f"{self.age}歳です。")


class Employee(Person):
    def __init__(self, name, age, number) -> None:
        super().__init__(name, age)
        self.number = number

    def say_number(self):
        print(f"電話番号は{self.number}です")

    def greeting(self):  # オーバーライド
        super().greeting()
        print(f"私は従業員です。電話番号:{self.number}")

    # def greeting(self, age): #pythonでオーバーロードはできない。オーバーライドしたメソッドに引数を追加して対応する
    #     print(f"私は{self.name}です。年齢は{self.age}です")


man = Employee("shogo", "32", "080726348")
man.greeting()
man.say_age()
man.say_number()
