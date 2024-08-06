def gcd_nums(a, b):
    for i in range(min(a,b), -1, -1):
        if a%i == 0 and b%i == 0:
            return i
        
print(gcd_nums(98, 56))