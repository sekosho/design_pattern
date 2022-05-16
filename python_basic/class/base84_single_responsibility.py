# single_responsibility
class UserInfo:
    # ユーザー情報を保持するという役割
    def __init__(self, name, age, number) -> None:
        self.name = name
        self.age = age
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}、{self.age}、{self.number}"

    # def write_str_to_file(self, filename):
    #     with open(filename, mode="w") as fh:
    #         fh.write(str(self))


class FileManager:
    @staticmethod
    def write_str_to_file(obj, filename):
        with open(filename, mode="w") as fh:
            fh.write(str(obj))


shogo = UserInfo("shogo", "32", "08069634405")
print(shogo)
# shogo.write_str_to_file("tmp.txt")
FileManager.write_str_to_file(shogo, "tmp.txt")
