# Map関数
list_a = list(range(1, 6))
map_a = map(lambda x: x * 2, list_a)
for x in map_a:
    print(x)

# サンプル
man = {"name": "shogo", "age": "32", "height": "164"}
# for key in man:
#     print(key)


map_b = map(lambda x: f"{x},{man[x]}", man)
for x in map_b:
    print(x)


# サンプル（引数ありの関数）
def calc(x, y, z):
    if z == "plus":
        return x + y
    elif z == "minus":
        return x - y


map_sample = map(
    calc, range(5), [3, 3, 3, 3, 3], ["plus", "minus", "plus", "minus", "plus"]
)
for i in map_sample:
    print(i)
