def armstrong_num(num):
    # You are given a 3-digit number n, Find whether it is an Armstrong number or not.An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 
    given_num = num
    total_sum = 0
    while num:
        remainder = num % 10
        num //= 10
        total_sum += (remainder**3)

    return total_sum == given_num

print(armstrong_num(153))