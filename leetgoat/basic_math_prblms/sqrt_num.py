def sqrt_num(num):
    i = 1
    while i <= num//2:
        if i * i == num:
            return i
        elif i * i > num:
            return i -1
        i += 1

print(sqrt_num(4))