# name = input("あなたの名前は何ですか？：")
# age = 32
# print("私の名前は={},年齢は{}".format(name, age))

# a = b = "Hello"
# print(a, b)


# LEGAL_AGE = 20
# age = 18

# if age < LEGAL_AGE:
#     print("未成年")
# else:
#     print("成人")

# print(f"{age=}")

# # 数値型
# value = -2
# value = value + 4
# print(value)
# print(value // 3)
# print(value % 3)
# print(value**3)

# シフト演算
value = 8  # 1000 => 0010
print(value >> 2)
print(value << 3)  # 1000 => 1000000

print(12 & 21)  # 01100 and 10101 = 00100 => 4
print(12 | 21)  # 01100 or 10101 = 11101 => 29

value = 12
value &= 21  # value = value & 21
print(value)
