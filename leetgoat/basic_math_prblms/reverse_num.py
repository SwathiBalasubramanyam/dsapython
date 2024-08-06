# https://www.geeksforgeeks.org/problems/reverse-digit0316/1

def rev_num(num):
    # 2345 --> 5
    num_reversed = 0

    while num:
        remainder = num % 10
        num = num // 10
        num_reversed = num_reversed * 10 + remainder
        
    return num_reversed

print(rev_num(23456))