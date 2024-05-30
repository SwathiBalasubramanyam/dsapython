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
            
        

#  leetcode 2148
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        res_cnt = 0
        for idx in range(len(nums)):
            found_low, found_high = False, False
            for jdx in range(len(nums)):
                if idx == jdx:
                    continue

                if nums[jdx] < nums[idx]:
                    found_low = True

                if nums[jdx] > nums[idx]:
                    found_high = True

                if found_low and found_high:
                    res_cnt += 1
                    break
                    
        return res_cnt

    def func(nums):
        smallest = min(nums)
        largest  = max(nums)

        return count([num for num in nums if smallest < num < largest])

#  leetcode 2006
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res_cnt = 0
        for idx in range(len(nums)):
            for jdx in range(idx, len(nums)):
                if abs(nums[idx] - nums[jdx]) == k:
                    res_cnt += 1

        return res_cnt


#  leetcode 2057
# https://leetcode.com/problems/smallest-index-with-equal-value/submissions/1167173627/
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        min_idx = float("inf")

        for idx in range(len(nums)):
            if idx % 10 == nums[idx]:
                min_idx = min(min_idx, idx)

        if min_idx == float("inf"):
            return -1
        return min_idx

# leetcode 2114
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_cnt = 0
        for sentence in sentences:
            max_cnt = max(max_cnt, len(sentence.split(" ")))
        return max_cnt

# leetcode 2119
# https://leetcode.com/problems/a-number-after-a-double-reversal/description/
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        def rev_num(num):
            res_num = 0
            while num > 0:
                res_num = (res_num * 10) + num % 10
                num //= 10

            return res_num

        return num == rev_num(rev_num(num))
        

# leetcode 2164
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_values = []
        even_values = []

        for idx in range(len(nums)):
            if idx%2 == 0:
                even_values.append(nums[idx])
            else:
                odd_values.append(nums[idx])

        odd_values.sort(reverse=True)
        even_values.sort()

        res_arr = [0 for _ in range(len(nums))]
        
        for idx in range(len(nums)):
            if idx%2 == 0:
                res_arr[idx] = even_values[0]
                even_values = even_values[1:]
            else:
                res_arr[idx] = odd_values[0]
                odd_values = odd_values[1:]

        return res_arr

#  leetcode 905
#  https://leetcode.com/problems/sort-array-by-parity/description/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i = 0
        sorted = False
        while not sorted:
            sorted = True
            for i in range(1, len(nums)):
                if nums[i-1]%2 != 0 and nums[i]%2 == 0:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    sorted = False
        return nums

        
# leetcode 1291
# https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        starting_digits = [1, 2, 3, 4, 5, 6, 7, 8]

        output = []

        for digit in starting_digits:

            while digit <= high:
                if low <= digit <= high:
                    output.append(digit)

                last_digit = (digit % 10) + 1
                if last_digit > 9:
                    break
                digit = (digit * 10) + (last_digit)

        return sorted(output)
    
#  leetcode 74
#  https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        matrix_len = len(matrix)

        mid = matrix_len // 2

        if target in matrix[mid]:
            return True
        elif target < matrix[mid][0]:
            return self.searchMatrix(matrix[:mid], target)
        else:
            return self.searchMatrix(matrix[mid+1:], target)

#  leetcode 
# https://leetcode.com/problems/koko-eating-bananas/
#  brute force
class Solution:
    def minEatingSpeed(self, piles, h):
        
        import math
        max_bananas = max(piles)
        
        completed = []
        for idx in range(1, max_bananas+1):
            hours_so_far = 0
            for pile in piles:
                hours_so_far += math.ceil(pile/idx)

            if hours_so_far <= h:
                completed.append(idx)

        return min(completed)

print(Solution().minEatingSpeed([3,6,7,11], 8))

#  binary search solution
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        import math

        rp = max(piles)
        lp = 1
        min_rate = float("inf")

        while lp <= rp:

            mid = (lp + rp) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
        
            if hours <= h:
                min_rate = min(min_rate, mid)
                rp = mid - 1
            else:
                lp = mid + 1

        return min_rate

# leetcode 1207
#  https://leetcode.com/problems/unique-number-of-occurrences/description/
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        from collections import defaultdict
        my_dict = defaultdict(int)
        for num in arr:
            my_dict[num] += 1

        return sorted(list(set(my_dict.values()))) == sorted(my_dict.values())
    
#  leetcode 1475
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        for i in range(len(prices)):
            min_index = None
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    min_index = j
                    break
            if min_index:
                prices[i] = prices[i] - prices[j]

        return prices
        
# leetcode 171
# https://leetcode.com/problems/excel-sheet-column-number/
def titleToNumber(self, columnTitle: str) -> int:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tlen = len(columnTitle)-1

        val = 0
        for idx, char in enumerate(columnTitle):
            val += 26**(tlen-idx) * (chars.index(char) + 1)
        return val

#  leetcode 
#  https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def format_str(my_string):
            my_stack = []
            for char in my_string:
                if char != "#":
                    my_stack.append(char)
                elif my_stack:
                    my_stack.pop()

            return my_stack

        return format_str(s) == format_str(t)
    
# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:


        def _dfs(node):
            if not node:
                return
            nonlocal curr
            _dfs(node.left)

            node.left = None
            curr.right = node
            curr = curr.right
            print("what is current", curr.val)
            _dfs(node.right)
            return

        dummy = TreeNode()
        curr = dummy
        _dfs(root)
        return dummy.right
    

    
resNode = Solution().increasingBST(TreeNode(5, TreeNode(1), TreeNode(7)))

while resNode:
    print(resNode.left, resNode.val, resNode.right)
    resNode = resNode.right


#  https://leetcode.com/problems/longest-nice-substring/
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        curr_max = ""
        for i in range(len(s)):
            for j in range(i+2, len(s)+1):
                sub_str = s[i:j]
                if set(sub_str) == set(sub_str.swapcase()) and len(sub_str) > len(curr_max):
                    curr_max = sub_str
        return curr_max

# this problem can have multiple solutions, one with stack and queue.
# but that is timing out as it is 2**n iterations
def longestNiceSubstring(self, s: str) -> str:
        from collections import Counter

        stack = [s]
        curr_max = ""
        while stack:

            last_ele = stack.pop()
            char_cnt = Counter(last_ele)

            for key in char_cnt.keys():
                if (key.islower() and not char_cnt.get(key.upper())) or (key.isupper() and not char_cnt.get(key.lower())):
                    if len(last_ele[1:]) > 1: 
                        stack.append(last_ele[1:])
                    if len(last_ele[:-1]):
                        stack.append(last_ele[:-1])

                    break
            else:
                if len(last_ele) > len(curr_max):
                    curr_max = last_ele
                
            
        return curr_max  

# https://leetcode.com/problems/design-an-ordered-stream/
class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.arr = [(i, None) for i in range(n)]
        self.next_id = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = (idKey-1, value)

        res = []
        while self.next_id-1 < self.n and self.arr[self.next_id-1][1]:
            res.append(self.arr[self.next_id-1][1])
            self.next_id += 1
        return res
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
    
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)

        def get_digit_sum(num):
            dsum = 0
            while num:
                dsum += num % 10
                num = num // 10
            return dsum

        digit_sum = 0
        for num in nums:
            digit_sum += get_digit_sum(num)
        
        return abs(digit_sum - element_sum)

# https://leetcode.com/problems/number-of-arithmetic-triplets/
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nlen = len(nums)
        triplets = []
        for i in range(nlen):
            for j in range(i+1, nlen):
                for k in range(j+1, nlen):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        triplets.append((i, j, k))

        return len(triplets)

# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/1201910808/
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        tsum = 0
        for i in range(0, len(arr), 2):
            for j in range(len(arr)):
                tsum += sum(arr[j: j+i+1])
                if (j+i+1) >= len(arr):
                    break

        return tsum

# https://leetcode.com/problems/design-browser-history/
class BrowserHistory:

    def __init__(self, homepage: str):
        self.backwards = []
        self.forwards = []
        self.backwards.append(homepage)
        

    def visit(self, url: str) -> None:
        self.backwards.append(url)
        self.forwards = []

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.backwards)-1)

        while steps > 0:
            curr = self.backwards.pop()
            self.forwards.append(curr)
            steps -= 1

        return self.backwards[-1]
        
    def forward(self, steps: int) -> str:
        # steps = min(steps, len(self.forwards)-1)

        while steps > 0 and self.forwards:
            curr = self.forwards.pop()
            self.backwards.append(curr)
            steps -= 1

        return self.backwards[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
    
# https://leetcode.com/problems/minimum-falling-path-sum/
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        min_sum = float("inf")
        memo = {}
        
        def _inbounds(col):
            return 0 <= col < COLS

        def _dfs(row_id, col_id):
            if not _inbounds(col_id):
                return float("inf")

            if row_id == ROWS-1:
                return matrix[row_id][col_id]

            if (row_id, col_id) in memo:
                return memo[(row_id, col_id)]

            left = _dfs(row_id + 1, col_id - 1)
            mid = _dfs(row_id + 1, col_id)
            right = _dfs(row_id + 1, col_id + 1)

            memo[(row_id, col_id)] = min(left, mid, right) + matrix[row_id][col_id]
            return memo[(row_id, col_id)]
        
        for col_id in range(COLS):
            min_sum = min(min_sum, _dfs(0, col_id))
        return min_sum

# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for idx in range(len(nums)):
        #     for jdx in range(idx+1, len(nums)):
        #         if nums[idx] + nums[jdx] == target:
        #             return [idx, jdx]

        # for idx, num in enumerate(nums):
        #     component = target - num
        #     if component in nums and nums.index(component) != idx:
        #         return [idx, nums.index(component)]

        nums_hash = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_hash:
                return [idx, nums_hash[compliment]]
            nums_hash[num] = idx

# https://leetcode.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.countNodes(root.left) + 1 + self.countNodes(root.right)
        
        
# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.queue = deque([])
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not bool(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
    

# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        if not root.left and not root.right:
            return root

        return TreeNode(val=root.val, left=self.invertTree(root.right), right=self.invertTree(root.left))
        

# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ranges = []
        lp = 0
        nums_len = len(nums)

        if nums_len == 1:
            return [str(nums[0])]

        for rp in range(1, nums_len):
            if nums[rp] != (nums[rp-1] + 1):
                ranges.append([nums[lp], nums[rp-1]])
                lp = rp

            if rp == (nums_len-1):
                ranges.append([nums[lp], nums[rp]])

        return [f'{ele[0]}' if ele[0] == ele[1] else f"{ele[0]}->{ele[1]}" for ele in ranges]
    
# https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        exp = 0
        base = 2

        while True:
            val = base**exp
            if val > n:
                return False
            if val == n:
                return True
            exp += 1
            
# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        my_stack = [(root, str(root.val))]
        while my_stack:
            curr_node, curr_paths = my_stack.pop()

            if not curr_node.left and not curr_node.right:
                res.append(curr_paths)

            if curr_node.left:
                my_stack.append((curr_node.left, curr_paths + f"->{curr_node.left.val}"))

            if curr_node.right:
                my_stack.append((curr_node.right, curr_paths + f"->{curr_node.right.val}"))

        return res

# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        
        new_num = 0
        while num:
            rem = num % 10
            num = num // 10
            new_num += rem

            if num == 0 and new_num > 9:
                num = new_num
                new_num = 0

        return new_num
    
# https://leetcode.com/problems/ugly-number/    
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        while num % 5 == 0:
            num /= 5

        while num % 3 == 0:
            num /= 3

        while num % 2 == 0:
            num /= 2

        return num == 1
    

# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lp, rp = 1, n

        while lp < rp:
            mid = (lp+rp) // 2

            if isBadVersion(mid):
                rp = mid
            else:
                lp = mid + 1

        return lp

# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_split = s.split(" ")
        seen_words = set()
        char_to_word = defaultdict(str)

        if len(str_split) != len(pattern):
            return False

        for idx, char in enumerate(pattern):
            if char in char_to_word and char_to_word[char] != str_split[idx]:
                return False

            if str_split[idx] in seen_words and char not in char_to_word:
                return False

            char_to_word[char] = str_split[idx]
            seen_words.add(str_split[idx])

        return True
