def prime(num):
    # your code here
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(prime(2))  # True
print(prime(5))  # True
print(prime(11)) # True
print(prime(4))  # False
print(prime(9))  # False
print(prime(-5)) # False

def pick_primes(number_list):
    # your code here
    return [ele for ele in number_list if prime(ele)]

print(pick_primes([2, 3, 4, 5, 6])) # [2, 3, 5]
print(pick_primes([101, 20, 103, 2017])) # [101, 103, 2017]