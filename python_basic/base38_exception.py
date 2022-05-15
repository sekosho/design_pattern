# raise 例外自作
class MyException(Exception):
    pass


def divide(a, b):
    if b == 0:
        raise MyException("0入れているんじゃねぇ")
    else:
        return a / b

try:
    c = divide(3,0)
except Exception as e:
    print(e,type(e))