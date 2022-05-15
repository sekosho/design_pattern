# 再帰
def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a - 1)


# sample(10)

# フィボナッチ
def fib(n):
    """
    1,2のとき：1
    3以上のとき；直前の二つの数値の和
    """
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


for x in range(1, 10):
    print(fib(x))
