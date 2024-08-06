
from typing import List
def printDivisors(n: int) -> List[int]:
    # Write your code here
    res = []

    for i in range(1, n+1):
        if n%i == 0:
            res.append(i)
    return res

def factors(n):

    i = 1
    res = set()
    while i*i <= n:
        if n%i == 0:
            res.append(i)
            res.append(n//i)
        i += 1

    return res

print(factors(100))