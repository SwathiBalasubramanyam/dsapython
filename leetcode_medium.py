# https://leetcode.com/problems/asteroid-collision/submissions/1176341915/
class Solution:
    def asteroidCollision(self, asteroids):
        
        my_stack = []

        for el in asteroids:
            my_stack.append(el)
            

            while len(my_stack) > 1 and my_stack[-2] > 0 and my_stack[-1] < 0:
                last_ele = my_stack.pop()
                before_last_ele = my_stack.pop()

                if abs(last_ele) > before_last_ele:
                    my_stack.append(last_ele)
                elif abs(last_ele) < before_last_ele:
                    my_stack.append(before_last_ele)
                elif abs(last_ele) == before_last_ele:
                    continue
            
                
        return my_stack


# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1176376151/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lp = rp = 0
        curr_max = 0

        while rp < len(s):
            rp += 1

            if len(s[lp:rp]) != len(set(s[lp:rp])):
                curr_max = max(curr_max, len(s[lp:rp-1]))
                lp += 1
                
        if len(s[lp:rp]) == len(set(s[lp:rp])):
                curr_max = max(curr_max, len(s[lp:rp]))

        return curr_max
    
# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_occur = {}
        for idx, char in enumerate(s):
            last_occur[char] = idx

        rp = 0
        start = 0
        substrs = []

        for lp, char in enumerate(s):
            rp = max(rp, last_occur[char])

            if lp == rp:
                substrs.append(len(s[start: rp+1]))
                start = lp+1

        return substrs

# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(-1,0), (1, 0), (0, -1), (0, 1)]

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def get_neighbors(r, c):
            neighbors = []
            for dr, dc in DIRS:
                if inbound(r+dr, c+dc):
                    neighbors.append((r+dr, c+dc))
            return neighbors

        def dfs(r, c):
            stack = [(r,c)]
            while stack:
                ele_r, ele_c = stack.pop()
                if grid[ele_r][ele_c] == "1":
                    grid[ele_r][ele_c] = "0"
                    stack += get_neighbors(ele_r, ele_c)

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                ele = grid[r][c]
                if ele != "1":
                    continue
                dfs(r, c)
                num_islands += 1

        return num_islands   
        
# https://leetcode.com/problems/odd-even-linked-list/submissions/1210414837/
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd_root = ListNode()
        odd_tail = odd_root

        even_root = ListNode()
        even_tail = even_root

        idx = 1
        while head:
            if idx % 2 == 0:
                even_tail.next = head
                even_tail = even_tail.next
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next

            head = head.next
            idx += 1

        odd_tail.next = even_root.next
        even_tail.next = None
        return odd_root.next
        

# https://leetcode.com/problems/sort-the-matrix-diagonally/
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        def get_diagonal_idxs_and_vals(row, col):
            diagonal_idxs = []
            diagonal_vals = []
            while row < rows and col < cols:
                diagonal_idxs.append((row, col))
                diagonal_vals.append(mat[row][col])
                row += 1
                col += 1
            return diagonal_idxs, sorted(diagonal_vals)

        def put_vals_in_place(dig_idxs, dig_data):
            for i in range(len(dig_idxs)):
                r, c = dig_idxs[i]
                mat[r][c] = dig_data[i]


        for i in range(rows):
            for j in range(cols):
                dig_idxs, dig_data = get_diagonal_idxs_and_vals(i, j)
                put_vals_in_place(dig_idxs, dig_data)

        return mat
    
# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        from collections import defaultdict
        rows = len(mat)
        cols = len(mat[0])
        mat_dict = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                mat_dict[r-c].append(mat[r][c])

        for k, v in mat_dict.items():
            mat_dict[k] = sorted(v, reverse=True)

        for r in range(rows):
            for c in range(cols):
                mat[r][c] = mat_dict[r-c].pop()
        return mat


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
from collections import defaultdict, deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        adj_list = defaultdict(list)
        # nodes = [(root, None)]
        # while nodes:
        #     curr_node, node_parent = nodes.pop()
        #     if node_parent:
        #         adj_list[curr_node.val].append(node_parent.val)
        #     if curr_node.left:
        #         adj_list[curr_node.val].append(curr_node.left.val)
        #         nodes.append((curr_node.left, curr_node))
        #     if curr_node.right:
        #         adj_list[curr_node.val].append(curr_node.right.val)
        #         nodes.append((curr_node.right, curr_node))


        def _tree_to_graph(node, parent):
            if not node:
                return

            if parent:
                adj_list[node.val].append(parent.val)
                adj_list[parent.val].append(node.val)

            _tree_to_graph(node.left, node)
            _tree_to_graph(node.right, node)

        _tree_to_graph(root, None)

        minutes = 0
        queue = deque([(start, minutes)])
        visited_set = set()

        while queue:
            node_val, minutes = queue.popleft()
            
            visited_set.add(node_val)

            for adj_node in adj_list[node_val]:
                if adj_node not in visited_set:
                    queue.append((adj_node, minutes+1))

        return minutes


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        from queue import deque

        adjacency_list = defaultdict(list)
        for edge in edges:
            adjacency_list[edge[1]].append(edge[0])

        res = []
        for i in range(n):
            all_ancestors = set()
            node_ancestors = deque(adjacency_list[i])
            while node_ancestors:
                ancestor = node_ancestors.popleft()
                if ancestor in all_ancestors:
                    continue
                all_ancestors.add(ancestor)
                node_ancestors += adjacency_list[ancestor]
            res.append(sorted(all_ancestors))

        return res

# https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEndOfWord = False

    def __str__(self):
        return f"{self.val}, {self.isEndOfWord}"

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]

        current_node.isEndOfWord = True

    def traverse(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node

    def search(self, word: str) -> bool:
        res = self.traverse(word)
        return res if type(res) is bool else res.isEndOfWord


    def startsWith(self, prefix: str) -> bool:
        return bool(self.traverse(prefix))


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
    
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
    class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def _binary_search(spell):
            print("starting")
            left, right = 0, len(potions)-1
            while left <= right:
                print("before", left, right)
                mid = (left+right)//2

                if spell*potions[mid] >= success:
                    right = mid - 1
                else :
                    left = mid + 1
                print("after", left, right)
                
            return left

        res = []
        potions.sort()
        for spell in spells:
            idx = _binary_search(spell)
            res.append(len(potions)-idx)
        return res
    
# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        word_dict = defaultdict(list)
        for word in strs:
            word_dict["".join(sorted(list(word)))].append(word)
        return word_dict.values()
    
# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for idx in range(len(nums)):
            res.append(prod)
            prod *= nums[idx]

        prod = 1
        for idx in range(len(nums)-1, -1, -1):
            res[idx] *= prod
            prod *= nums[idx]

        return res

# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_set = set()
        cols_set = set()

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows_set.add(r)
                    cols_set.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in rows_set or c in cols_set :
                    matrix[r][c] = 0

        return matrix
        
# https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        char_cnt = sorted(Counter(s).items(), key=lambda item: item[-1], reverse=True)
        
        return "".join([tup[1]* tup[0] for tup in char_cnt])

# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 00 01 02 --> 20 10 00
        # 10 11 12 --> 01 11 21
        # 20 21 22 --> 22 12 02

        l = 0
        r = len(matrix) -1
        while l < r:
	        matrix[l], matrix[r] = matrix[r], matrix[l]
	        l += 1
	        r -= 1
        # transpose 
        for i in range(len(matrix)):
	        for j in range(i):
		        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

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

# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res_arr = set()
        len_str = len(s)

        def _backtrack(idx, curr_str):
            if idx == len_str:
                res_arr.add(curr_str)
                return

            if not s[idx].isnumeric():
                _backtrack(idx+1, curr_str + s[idx].upper())
            _backtrack(idx+1, curr_str + s[idx].lower())

        _backtrack(0, "")
        return list(res_arr)
        

# https://leetcode.com/problems/rank-teams-by-votes/submissions/1276773752/
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        votes_by_char = {}

        for vote in votes:
            for idx, char in enumerate(vote):
                if char not in votes_by_char:
                    votes_by_char[char] = [0 for _ in range(len(vote))]
                votes_by_char[char][idx] += 1

        sorted_vals = sorted(votes_by_char.items(), key=lambda item: (item[1], -ord(item[0])), reverse=True)

        return "".join([fv for fv, sv in sorted_vals])
                
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operations:
                my_stack.append(int(token))
                continue
            sn, fn = my_stack.pop(), my_stack.pop()
            if token == '+':
                my_stack.append(fn+sn)
            elif token == '-':
                my_stack.append(fn-sn)
            elif token == '*':
                my_stack.append(fn*sn)
            else:
                
                my_stack.append(int(fn/sn))


        return my_stack[0]

        
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float("inf")
        
        while nums:
            if nums[0] <= nums[-1]:
                min_val = min(min_val, nums[0])
                break

            mid = len(nums)//2
            min_val = min(min_val, nums[mid])

            left_nums = nums[:mid]
            right_nums = nums[mid+1:]

            if left_nums and nums[mid] >= left_nums[0]:
                nums = right_nums
            else:
                nums = left_nums
        return min_val

# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0,1), (0, -1), (1,0), (-1,0)]
        
        max_minutes = 0
        my_queue = deque([])

        def find_max_mins():
            nonlocal max_minutes, my_queue
            processed = set()
            
            while my_queue:
                (row, col, minutes) = my_queue.popleft()
                max_minutes = max(max_minutes, minutes)  

                processed.add((row, col))

                for dir in DIRS:
                    dr, dc = row+dir[0], col+dir[1]
                    if 0<=dr<ROWS and 0<=dc<COLS and grid[dr][dc] == 1 and (dr,dc) not in processed:
                        grid[dr][dc] = 2
                        my_queue.append((dr,dc,minutes+1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 2:
                    continue
                my_queue.append((row, col,0))

        find_max_mins()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return max_minutes
                

# https://leetcode.com/problems/zigzag-conversion/      
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = ["" for _ in range(numRows)]
        row = 0
        dir = 1
        for char in s:
            mat[row]+= char
            if (row+dir)%numRows == 0:
                dir = -1
            elif row == 0:
                dir = 1
            row += dir

        return "".join(mat)
        
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_chart = defaultdict(list)

        for idx, group_size in enumerate(groupSizes):
            gci = group_chart[group_size]
            if not gci:
                gci.append([idx])
            elif len(gci[-1]) < group_size:
                gci[-1].append(idx)
            elif len(gci[-1]) >= group_size:
                gci.append([idx])

        res_array = []
        for sub_list in group_chart.values():
            res_array += sub_list
        return res_array

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         lp = 0
#         pairs = 0

#         for idx in range(len(time)):
#             for jdx in range(idx+1, len(time)):
#                 if (time[idx] + time[jdx]) % 60 == 0:
#                     pairs += 1

#         return pairs

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res  , count  = 0,  [0] * 60
        for one in range(len(time)):
            index = time[one] % 60
            res += count[(60 - index)%60] # %60 is for index==0
            count[index] += 1
        return res


# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for the first element

            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate values for the second element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate values for the third element
                    left += 1
                    right -= 1

        return res

# https://leetcode.com/problems/01-matrix/  
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from queue import deque

        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS = len(mat)
        COLS = len(mat[0])

        res_arr = []

        queue = deque()

        for row in range(ROWS):
            new_row = []
            for col in range(COLS):
                if mat[row][col] == 0:
                    new_row.append(0)
                    queue.append((row,col))
                else:
                    new_row.append(float("inf"))

            res_arr.append(new_row)

        while queue:
            row, col = queue.popleft()
            for dr, dc in DIRS:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS:
                    if res_arr[r][c] > res_arr[row][col] + 1:
                        res_arr[r][c] = res_arr[row][col] + 1
                        queue.append((r, c))

        return res_arr    
    
# https://leetcode.com/problems/flower-planting-with-no-adjacent/
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Initialize a result array with all gardens having 1 as flower
        res = [1] * n

        adj_list = defaultdict(list)
        flower_choices = set([1,2,3,4])

        for path in paths:
            adj_list[path[0]].append(path[1])
            adj_list[path[1]].append(path[0])

        garden_to_flower = defaultdict(int)

        def get_adj_flowers(adj_gardens):
            res = set()
            for adj_garden in adj_gardens:
                if not garden_to_flower[adj_garden]:
                    continue
                res.add(garden_to_flower[adj_garden])
            return res

        for garden, adj_gardens in adj_list.items():

            adj_flowers = get_adj_flowers(adj_gardens)
            choices = flower_choices - adj_flowers
            garden_to_flower[garden] = list(choices)[0]
            res[garden-1] = garden_to_flower[garden]

        return res

# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        num_map =  [(1000, 'M'), (900,'CM'), (500, 'D'), (400,'CD'), (100, 'C'),
           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), 
           (5, 'V'), (4, 'IV'), (1, 'I')]

        res_str = ""

        for k,v in num_map:

            if k > num:
                continue

            quotient = num // k
            res_str += (v * quotient)
            num = num % k

        return res_str
    
# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1287536479/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:

            mid = left + (right-left) // 2

            if nums[mid] == target:
                return mid

            # left portion of array
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid-1

            # right portion of array
            else:
                if target < nums[mid]:
                    right = mid-1
                elif target > nums[right]:
                    right = mid-1
                else:
                    left = mid+1
                

        return -1
    
# https://leetcode.com/problems/time-based-key-value-store/submissions/1288355301/
class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.myDict[key]
        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]
            if values[m][1] < timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res

# https://neetcode.io/problems/longest-repeating-substring-with-replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        max_cnt = 0
        char_cnt = {}

        for r in range(len(s)):
            char_cnt[s[r]] = 1 + char_cnt.get(s[r], 0)

            while (r-l+1) - max(char_cnt.values()) > k:
                char_cnt[s[l]] -=1
                l += 1

            max_cnt = max(max_cnt, r-l+1)

        return max_cnt
        
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize a left, right pointer at 0, len(s1)
        # while r <= len(s2)
        # get the substring[l:r] --> "lec"
        # sort the substring and see if it matches S1
        #  if true, then return true else at the end return false

        l, r = 0, len(s1)
        sorted_s1 = sorted(s1)
        while r <= len(s2):
            sub_str = s2[l:r]
            if sorted_s1 == sorted(sub_str):
                return True
            l += 1
            r += 1
        return False

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        can_len = len(candidates)
        def dfs(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return 

            if total > target or i >= can_len:
                return

            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])

            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums[:]]

        res = []

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res += perms

            nums.append(n)

        return res
        

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return 

            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, curr)

        dfs(0, [])
        return res
        
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def dfs(r,c,idx):
            # that means we have already searched all the chars 
            # and we reached last idx+1 so we can return true
            if idx == len(word):
                return True

            # outofbounds errors so false
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            # in traced path
            if (r,c) in visited:
                return False

            # char not in place, so false
            if board[r][c] != word[idx]:
                return False


            visited.add((r,c))
            res = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)
            visited.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev= second
            second = nxt

        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        node_len = 0
        while tmp:
            node_len += 1
            tmp = tmp.next

        node_to_delete = node_len - n

        dummyNode = ListNode()
        tail = dummyNode
        while node_to_delete:
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = None
            node_to_delete -= 1

        if head.next:
            tail.next = head.next
        return dummyNode.next

class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


            