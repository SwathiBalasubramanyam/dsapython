# https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1

def pwr_nums(num, pwr):
    # time is o(n), where n is the pwr

    res = 1
    for i in range(pwr):
        res *= num

    return res

def pwr_nums_2(num, pwr):
    # time and space is o(n)
    if pwr == 0:
        return 1
    
    if pwr == 1:
        return num
    
    return num * pwr_nums_2(num, pwr-1)

def pwr_divide_and_conquer(num, pwr):
    #  o(logn complexity)
    if pwr == 0:
        return 1
    
    temp = pwr_divide_and_conquer(num, pwr//2)
    if pwr%2 == 0:
        return temp * temp
    return num * temp * temp

print(pwr_divide_and_conquer(2,4))