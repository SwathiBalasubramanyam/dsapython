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

#  Leetcode 9
def isPalindrome(x):
    start_num = x
    end_num = 0
    while x > 0:
        rem = x % 10
        x //= 10
        end_num = (end_num * 10) + rem
    
    return start_num == end_num

#  Leetcode 13
def romanToInt(s):

    # https://leetcode.com/problems/roman-to-integer/description/

    symbol_val = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    i = 0
    total_value = 0
    while i < len(s):
        char = s[i]
        curr_val = symbol_val[char]
        sub_total = curr_val
        
        while (i+1) < len(s) and symbol_val[s[i+1]] > curr_val:
            sub_total = symbol_val[s[i+1]] - sub_total
            i += 1
        total_value += sub_total
        i += 1

    return total_value

#  Leetcode 14
def longestCommonPrefix(strs):
    # prefix = strs[0]

    # prefix_in_all = False

    # while prefix and not prefix_in_all:
    #     prefix_in_all = True
    #     for ele in strs[1:]:
    #         if prefix not in ele:
    #             prefix_in_all = False
    #             prefix = prefix[:-1]
    #             break


    # return prefix

    strs.sort()
    prefix = ""
    i = 0
    while i < len(strs[0]):
        prefix += strs[0][i]
        for word in strs:
            if not word.startswith(prefix):
                return prefix[0:-1]
        i += 1
    return prefix

#  Leetcode 20
def isValidParenthesis(s):
        
    close_to_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    my_stack = []
    for char in s:
        if char in close_to_open:
            if not my_stack or close_to_open[char] != my_stack[-1]:
                return False
            my_stack.pop()
        else:
            my_stack.append(char)

    return not my_stack 

def isValidParenthesis(s):
    possible_combos = ["()", "{}", "[]"]
    replaceable = True

    while replaceable and s:
        replaceable = False
        for combo in possible_combos:
            if combo in s:
                replaceable = True
                s = s.replace(combo, "")

    return not s

#  Leetcode 21
# https://leetcode.com/problems/merge-two-sorted-lists/description/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

#  Leetcode 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(self, nums: List[int]) -> int:
    seen_nums = set()

    for idx, num in enumerate(nums):
        if num in seen_nums:
            nums[idx] = "_"
        else:
            seen_nums.add(num)

    nums = list(seen_nums) + ["_" for i in range(len(nums) - len(seen_nums))]

    return len(seen_nums)

# Leetcode 27
# https://leetcode.com/problems/remove-element/
def removeElement(self, nums: List[int], val: int) -> int:
    replaced_val = 0
    for idx, num in enumerate(nums):
        if nums[idx] == val:
            replaced_val += 1
            nums = nums[:idx] + nums[idx+1:] + ['_']
            print(nums)
    return len(nums) - replaced_val

#  Leetcode 1089
# https://leetcode.com/problems/duplicate-zeros/description/
def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        while i < len(arr):

            if arr[i] != 0:
                i += 1
                continue
            
            last_num = 0
            for j in range(i+1, len(arr)):
                arr[j], last_num = last_num, arr[j]

            i += 2


# Leetcode 59
# https://leetcode.com/problems/spiral-matrix-ii/description/
def generateMatrix(self, n: int) -> List[List[int]]:
        DIRECTIONS = [(0,1), (1,0), (0, -1), (-1, 0)]
        sub_arr_cnt = [n]
        for i in range(n-1, 0, -1):
            sub_arr_cnt += [i, i]

        value = 1
        r, c = 0, 0
        d = 0

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        while value <= n * n:

            matrix[r][c] = value
            value += 1
            sub_arr_cnt[0] -= 1

            if sub_arr_cnt[0] == 0:
                sub_arr_cnt = sub_arr_cnt[1:]
                d = (d+1) % 4

            dr, dc = DIRECTIONS[d]
            r += dr
            c += dc

        return matrix

# Leetcode 79
# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import Counter, defaultdict, deque

        ROWS = len(board) 
        COLS  = len(board[0])
        DIRECTIONS = [(0,1), (1,0), (-1, 0), (0, -1)]

        word_char_count = Counter(word)
        board_char_count = defaultdict(int)

        for r in range(ROWS):
            for c in range(COLS):
                board_char_count[board[r][c]] += 1

        for char, cnt in word_char_count.items():
            if board_char_count[char] < cnt:
                return False

        def _get_neighbors(cell, my_queue):
            for dir in DIRECTIONS:
                new_row, new_col = cell[0] + dir[0], cell[1] + dir[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    my_queue.append((new_row, new_col))

        for r in range(ROWS):
            for c in range(COLS):
                if not word.startswith(board[r][c]):
                    continue

                visited = set()
                res_word = board[r][c]
                my_stack = [(r,c)]

                while my_stack:
                    last_ele = my_stack.pop()

#  leetcode 43
# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        total = 0
        len_num1 = len(num1) - 1
        len_num2 = len(num2) - 1

        for idx, digit1 in enumerate(num1):
            int_digit1 = int(digit1)
            for jdx, digit2 in enumerate(num2):
                int_digit2 = int(digit2)
                total += (int_digit1 * (10 ** (len_num1 - idx))) * (int_digit2 * (10 ** (len_num2 - jdx)))
        
        return str(total)


