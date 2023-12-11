def prime_factors(n):
    # your code here
    prime_fac = []
    for i in range(2, n):
        if n % i == 0 and prime(i):
            prime_fac.append(i)

    return prime_fac

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(prime_factors(24)) # [2, 3]
print(prime_factors(60)) # [2, 3, 5]