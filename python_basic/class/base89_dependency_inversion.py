# dependency invension


# class Book:
#     def __init__(self, content) -> None:
#         self.content = content


# class Formatter:
#     def format(self, book: Book):
#         return book.content


# class AFormatter:
#     def format(self, book: Book):
#         return book.content + "A"


# class Printer:
#     def print(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         print(formatted_book)


from abc import ABCMeta, abstractmethod, abstractproperty


class IBook(metaclass=ABCMeta):
    @abstractproperty
    def content(self):
        pass


class Book(IBook):
    def __init__(self, content) -> None:
        self._content = content

    @property
    def content(self):
        return self._content


class EBook(IBook):
    def __init__(self, content) -> None:
        self._content = content

    @property
    def content(self):
        return "E" + self._content


class IFormatter(metaclass=ABCMeta):
    @abstractmethod
    def format(self, i_book: IBook):
        pass


class HTMLFormatter(IFormatter):
    def format(self, i_book: IBook):
        return "<h1>" + i_book.content + "</h1>"


class XmlFormatter(IFormatter):
    def format(self, i_book: Book):
        return "<xml>" + i_book.content + "</xml>"


class Printer:
    def __init__(self, i_formatter: IFormatter) -> None:
        self._i_formatter = i_formatter

    def print(self, i_book: IBook):
        formatted_book = self._i_formatter.format(i_book)
        print(formatted_book)


book = Book("My book")
html_formatter = HTMLFormatter()
html_printer = Printer(html_formatter)
html_printer.print(book)

xml_formatter = XmlFormatter()
xml_printer = Printer(xml_formatter)
xml_printer.print(book)

ebook = EBook("My EBook")
html_printer.print(ebook)
xml_printer.print(ebook)
