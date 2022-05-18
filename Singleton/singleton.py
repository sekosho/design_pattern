class DataBase:
    _instance = None

    def __init__(self) -> None:
        self.__database_url = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def database_url(self):
        return self.__database_url

    @database_url.setter
    def database_url(self, database_url):
        self.__database_url = database_url

    def connect(self):
        # DBに接続します
        pass


a = DataBase()
b = DataBase()
print(a == b)

print(id(a), id(b))
database_url = "128.1.1.1.1:5678"
a.database_url = database_url
print(a.database_url)
print(b.database_url)
