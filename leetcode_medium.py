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
                