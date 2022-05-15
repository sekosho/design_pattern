# # 高階関数
# def print_hello():
#     print("hello")


# def print_goodbye():
#     print("goodbye")


def print_message(msg):
    print(f"{msg} world")


def print_konnichiwa():
    print("こんにちは")


def print_hello(func):
    func("hello")
    return print_konnichiwa


var = print_hello(print_message)
var()
