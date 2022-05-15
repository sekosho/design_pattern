# 特殊メソッド


class Human:
    def __init__(self, name, age, phone_number) -> None:
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"{self.name},{self.age},{self.phone_number}"

    def __eq__(self, other):
        return (self.name == other.name) and (self.phone_number == other.phone_number)

    def __hash__(self) -> int:
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if int(self.age) >= 20 else False

    def __len__(self):
        return len(self.name)


man = Human("shogo", "32", "08-8273912")
man2 = Human("shogo", "18", "08-8273912")
man3 = Human("takuya", "18", "09-8273912")
# __str_が呼ばれる
# str_human = str(man)
print(man)
print(man2)

# __eq__が呼ばれる
print(man == man2)

# setは内部的にhashをしているので__hash__が呼ばれる
set_men = {man, man2, man3}
for m in set_men:
    print(m)

# if利用で__bool__が呼ばれる
if man:
    print(f"{man.name}は{man.age}なので成人です")
if man2:
    print(f"{man2.name}は{man2.age}なので成人です")
if man3:
    print(f"{man3.name}は{man3.age}なので成人です")

# __len__が呼ばれる
print(len(man))
print(len(man3))
