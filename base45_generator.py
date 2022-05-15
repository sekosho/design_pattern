# list, generator memory

import sys

list_a = [i for i in range(100000)]


def num(max):
    n = 0
    while n < max:
        yield n
        n += 1


gen = num(100000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))


list_b = []
for i in num(100000):
    list_b.append(i)
print(sys.getsizeof(list_b))
