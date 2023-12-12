def all_else_equal(num_list):
    # your code here
    half = sum(num_list) // 2

    return half if half in num_list else None


print(all_else_equal([2, 4, 3, 10, 1])) # 10
print(all_else_equal([6, 3, 5, -9, 1])) # 3
print(all_else_equal([1, 2, 3, 4]))     # None