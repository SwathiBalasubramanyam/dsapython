"""A simple file for Leetcode Easy Problems"""

# LeetCode 645
def findErrorNums(nums):
    #  return [dup, missing_num]
    possible_nums = set(range(1, len(nums)+1))
    dup_num = None

    for num in nums:
        if nums.count(num) == 2:
            dup_num = num

        possible_nums.discard(num)

    return [dup_num, list(possible_nums)[0]]

# Leetcode 645 different way of solving 
def findErrorNums(nums):
    n = len(nums)

    expected_sum = n * (n+1) // 2

    seen = set()
    dup = None
    actual_sum = 0

    for num in nums:
        if num in seen:
            dup = num
        else:
            seen.add(num)
            actual_sum += num

    return [dup, expected_sum - actual_sum]


#  Leetcode 66
def plusOne(digits):

    new_digits = []
    carry = 1

    for idx, num in enumerate(digits[::-1]):
        if carry:
            num += carry
            carry = 0

        if num > 9:
            new_digits.append(num % 10)
            carry = num // 10
        else:
            new_digits.append(num)


    if carry:
        new_digits.append(carry)

    return new_digits[::-1]


# Leetcode 168

def convertToTitle(columnNumber):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res_str = ""

    while columnNumber > 26:
        remainder = columnNumber % 26
        res_str = chars[remainder-1] + res_str
        columnNumber //= 26
        if remainder == 0:
            columnNumber -= 1

    res_str = chars[columnNumber-1] + res_str

    return res_str

# Leetcode 500
def findWords(words):

    first_row = "qwertyuipo"
    sec_row = "asdfghjkl"
    third_row = "zxcvbnm"

    selected_words = []

    for word in words:
        if len([char for char in word if char.lower() in first_row]) == len(word):
            selected_words.append(word)

        elif len([char for char in word if char.lower() in sec_row]) == len(word):
            selected_words.append(word)

        elif len([char for char in word if char.lower() in third_row]) == len(word):
            selected_words.append(word)

    return selected_words