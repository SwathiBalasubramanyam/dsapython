# https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1

def last_digit_in_num(base, exp):

    remainder = (base**exp) % 10
    return remainder

print(last_digit_in_num(3, 10))