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
