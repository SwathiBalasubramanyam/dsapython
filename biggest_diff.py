# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.


def biggest_diff(nums):
    maxn, minn = float("-inf"), float("inf")
    for num in nums:
        if num > maxn:
            maxn = num
        if num < minn:
            minn = num
    print(maxn-minn)

biggest_diff([10, 3, 5, 6]) #→ 7
biggest_diff([7, 2, 10, 9]) #→ 8
biggest_diff([2, 10, 7, 2]) #→ 8
