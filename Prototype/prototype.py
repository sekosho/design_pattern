from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def use(self, msg):
        pass

    @abstractmethod
    def _clone(self):
        pass


class MessageBox(Prototype):
    def __init__(self, decoration_char) -> None:
        self.__decoration_char = decoration_char

    def use(self, msg):
        str_msg = str(msg)
        print(self.__decoration_char * (len(str_msg) + 4))
        print(self.__decoration_char + " " + str_msg + " " + self.__decoration_char)
        print(self.__decoration_char * (len(str_msg) + 4))

    def _clone(self):
        print("MessageBoxのクローンを作成します")
        return deepcopy(self)

    @property
    def decoration_char(self):
        return self.__decoration_char

    @decoration_char.setter
    def decoration_char(self, decoration_char):
        self.__decoration_char = decoration_char


class UnderlinePen(Prototype):
    def __init__(self, underline_char) -> None:
        self.__underline_char = underline_char

    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)
        print(self.__underline_char * (len(str_msg) + 4))

    def _clone(self):
        print("UnderlinePenのコピーを作成します")
        return deepcopy(self)

    @property
    def underline_char(self):
        return self.__underline_char

    @underline_char.setter
    def underline_char(self, underline_char):
        self.__underline_char = underline_char


class Manager:
    def __init__(self) -> None:
        self.__products = {}

    def register(self, name, proto_type: Prototype):
        self.__products[name] = deepcopy(proto_type)

    def create_product(self, name):
        product = self.__products.get(name)
        return product._clone()


manager = Manager()
m_box = MessageBox("*")
m_box.use("Yahoo")
manager.register("m_box", m_box)
new_box = manager.create_product("m_box")

m_box.decoration_char = "="
m_box.use("Yahoo")

new_box.use("New Yahoo")
