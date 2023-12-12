def fibonacci(length):
    # your code here

    if length == 0:
        return []

    if length == 1:
        return [1]

    res = [1, 1]

    for i in range(2, length):
        res.append(res[i-1] + res[i-2])

    return res

print(fibonacci(0)) # []
print(fibonacci(1)) # [1]
print(fibonacci(6))  # [1, 1, 2, 3, 5, 8]
print(fibonacci(8))  # [1, 1, 2, 3, 5, 8, 13, 21]