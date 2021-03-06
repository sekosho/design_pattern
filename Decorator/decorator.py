from abc import ABC, abstractmethod
from operator import mod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ShowCharComponent(Component):
    def __init__(self, char) -> None:
        self.__char = char

    def operation(self):
        print(self.__char * 20)


class ShowDecorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component


class ShowMessage(ShowDecorator):
    def __init__(self, component: Component, msg) -> None:
        super().__init__(component)
        self.__msg = msg

    def operation(self):
        self._component.operation()  # Componentのメソッド
        print(self.__msg)  # ShowMessageクラスのプロパティ
        self._component.operation()


class WriteDecorator(Component):
    def __init__(self, component: Component, file_name, msg) -> None:
        self._component = component
        self._file_name = file_name
        self._msg = msg


class WriteMessage(WriteDecorator):
    def operation(self):
        self._component.operation()
        with open(self._file_name, mode="w") as fh:
            fh.write(self._msg)


show_component = ShowCharComponent("-")
# show_component.operation()
show_message = ShowMessage(show_component, "Hello")
# show_message.operation()
write_message = WriteMessage(show_message, "tmp.txt", "Write Message")
write_message.operation()
