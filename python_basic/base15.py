fruit = """apple
grape
orange
キウイ
"""
print(fruit)


# encode , decode => bytes[]
byte_fruit = fruit.encode("utf-8")
print(byte_fruit)
print(type(byte_fruit))


str_fruit = byte_fruit.decode("utf-8")
print(str_fruit)
print(type(str_fruit))
