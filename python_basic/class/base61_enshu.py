class CharacterAlreadyExistException(Exception):
    pass


class Character:
    def __init__(self, name, hp, offence, defence) -> None:
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence
        AllCharacters.set_character(self.name)

    def attack(self, other, is_critical=False):
        if self.hp <= 0:
            print("hpがないので攻撃できません。")
            return
        power = 1
        if is_critical:
            power = 2
        attack_point = self.offence - other.defence
        attack_point = 1 if attack_point < 0 else attack_point
        other.hp -= attack_point * power
        if other.hp <= 0:
            AllCharacters.delete_character(other.name)

    def critical_hit(self, other):
        self.attack(other, is_critical=True)


class AllCharacters:
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def set_character(cls, name):
        if name in cls.alive_characters:
            raise CharacterAlreadyExistException("同じ名前のキャラクターが存在するので作れません。名前を変えてください。")
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def delete_character(cls, name):
        cls.alive_characters.remove(name)
        cls.all_characters.remove(name)


my_character = Character("shogo", hp=100, offence=90, defence=60)
enemy1 = Character("takuya", hp=60, offence=40, defence=50)
enemy2 = Character("shogo2", hp=30, offence=49, defence=20)
print(AllCharacters.all_characters)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
# my_character.attack(enemy1)
# print(enemy1.hp)
my_character.critical_hit(enemy1)
print(enemy1.hp)
enemy1.attack(my_character)

print(AllCharacters.all_characters)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
