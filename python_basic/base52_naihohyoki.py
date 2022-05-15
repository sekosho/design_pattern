def is_sosu(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


sosu_l = [x for x in range(100) if is_sosu(x) == True]  # list
sosu_t = tuple(x for x in range(100) if is_sosu(x) == True)  # tuple
sosu_g = (x for x in range(100) if is_sosu(x) == True)  # generator
sosu_s = {x for x in range(100) if is_sosu(x) == True}  # set
print(sosu_l)
print(sosu_t)
print(f"ジェネレータ：{next(sosu_g)}")
print("ジェネレータ展開")
for i in sosu_g:
    print(i)

print(sosu_s)
t = (11, 11, 22, 33, 33)
print(t)
print(set(t))
