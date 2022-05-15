# ジェネレーター関数
def generator(max):
    print("generator作成")
    n = 0
    for n in range(max):
        try:
            x = yield n
            print(f"{x=}")
            print("yield実行")
        except ValueError as e:
            print("throw 実行しました")


gen = generator(10)
print(type(gen))
# for x in gen:
#     print(f"{x=}")
next(gen)
gen.send(100)
# gen.throw(ValueError("Invalid Value"))
gen.close()
next(gen)
