# https://www.geeksforgeeks.org/problems/count-digits5716/1

def cnt_digits(num):
    digit_cnt = 0
    while num:
        num = num // 10
        digit_cnt += 1

    return digit_cnt

print(cnt_digits(23))