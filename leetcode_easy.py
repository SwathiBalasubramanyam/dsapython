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

        def _get_neighbors(cell, visited):
            valid_dirs = []
            for dir in DIRECTIONS:
                new_row, new_col = cell[0] + dir[0], cell[1] + dir[1]
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited:
                    valid_dirs.append((new_row, new_col))

            return valid_dirs

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                my_stack = [(r,c)]
                word_sofar = ""
                while my_stack:
                    last_ele = my_stack.pop()
                    new_word = word_sofar + board[last_ele[0]][last_ele[1]]
                    if not word.startswith(new_word):
                        continue
                    word_sofar += board[last_ele[0]][last_ele[1]]

                    if word_sofar == word:
                        return True
                        
                    visited.add((r,c))
                    my_stack += _get_neighbors(last_ele, visited)
        return False

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


# Leetcode 704
# https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        mid = len(nums) // 2
        
        if target > nums[mid]:
            idx = self.search(nums[mid+1:], target)

            if idx == -1:
                return -1
            return mid + idx + 1

        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        else:
            return mid
        
#  Leetcode 1909
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        for idx in range(len(nums)):

            all_increasing = True
            new_nums = nums[:idx] + nums[idx+1:]

            for jdx in range(1, len(new_nums)):
                if new_nums[jdx-1] >= new_nums[jdx]:
                    all_increasing = False
                    break

            if all_increasing:
                return True

        return False

# Leetcode 1446
# https://leetcode.com/problems/consecutive-characters/description/
class Solution:
    def maxPower(self, s: str) -> int:
        
        prev_char = s[0]
        max_pwr = 1
        currnt_char_cnt = 1

        for char in s[1:]:
            if char == prev_char:
                currnt_char_cnt += 1
            else:
                max_pwr = max(max_pwr, currnt_char_cnt)
                currnt_char_cnt = 1
                prev_char = char

        return max(max_pwr, currnt_char_cnt)

# leetcode 1389
# https://leetcode.com/problems/create-target-array-in-the-given-order/description/
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res_arr = [0 for i in range(len(nums))]

        for idx in range(len(nums)):
            jdx = index[idx]
            res_arr[jdx:] = [nums[idx]] + res_arr[jdx:]

        return res_arr[:len(nums)]

# leetcode 1556
# https://leetcode.com/problems/thousand-separator/description/
class Solution:
    def thousandSeparator(self, n: int) -> str:
        str_int = str(n)[::-1]
        new_str = ""

        for idx in range(0, len(str_int), 3):
            new_str += str_int[idx:idx+3]
            new_str += "."

        new_str = new_str[::-1]
        if new_str[0] == ".":
            return new_str[1:]
        return new_str
        
# Leetcode 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen_nums = set()
        idx = 0
        while idx < len(nums):

            if nums[idx] == "_":
                break
        
            if nums[idx] in seen_nums:
                nums.remove(nums[idx])
                nums.append("_")
            else:
                seen_nums.add(nums[idx])
                idx += 1

        return len(seen_nums)

#  Leetcode 2016
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        maxDiff = -1
        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                if i < j and nums[i] < nums[j]:
                    maxDiff = max(nums[j] - nums[i], maxDiff)

        return maxDiff
        
#  Leetcode 35
# https://leetcode.com/problems/search-insert-position/submissions/1163381179/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        mid = len(nums) // 2

        if target < nums[mid]:
            return self.searchInsert(nums[:mid], target)

        elif target > nums[mid]:
            return mid + self.searchInsert(nums[mid+1:], target) + 1

        else:
            return mid

#  Leetcode 88
# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not m:
            nums1[:] = nums2[:]
            return

        if not n:
            return

        for idx in range(m, len(nums1)):
            nums1[idx] = "_"
        
        nums1_idx, nums2_idx = 0, 0

        while nums2_idx < n:
            if nums1[nums1_idx] == "_":
                nums1[nums1_idx] = nums2[nums2_idx]
                nums2_idx +=1
            elif nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[:] = nums1[:nums1_idx] + [nums2[nums2_idx]] + nums1[nums1_idx:-1]
                nums2_idx +=1
                
            nums1_idx += 1
            
# Leetcode 100
# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# LeetCode 101
# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(left, right):

            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)

# leetcode 104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        my_stack = [(root, 1)]
        max_depth = 0
        while my_stack:
            curr_node, curr_depth = my_stack.pop()
            max_depth = max(curr_depth, max_depth)
            if curr_node.left:
                my_stack.append((curr_node.left, curr_depth+1))
            if curr_node.right:
                my_stack.append((curr_node.right, curr_depth+1))

        return max_depth
            
        