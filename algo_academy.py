# Day 1 - set of problems :-
#  Topics - Arrays, stacks, sliding window concepts, two pointers

# https://leetcode.com/problems/contains-duplicate-ii/description/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            
        lp = 0
        window = []
        
        for rp in range(len(nums)):
            if nums[rp] in window:
                return True

            window.append(nums[rp])

            if len(window) >= k+1:
                window = window[1:]
                lp += 1


        return False
        
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = ""
        max_size = 0

        for rp in range(len(s)):
            if s[rp] in window:
                max_size = max(max_size, len(window))
                while s[rp] in window:
                    window = window[1:]
            window += s[rp]
        max_size = max(max_size, len(window))

        return max_size

# https://leetcode.com/problems/minimum-size-subarray-sum/description/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp, total = 0, 0
        min_size = float('inf')

        for rp in range(len(nums)):
            total += nums[rp]
            while total >= target:
                min_size = min(min_size, rp-lp+1)
                total -= nums[lp]
                lp += 1

        return min_size if min_size != float('inf') else 0
    
# https://leetcode.com/problems/asteroid-collision/description/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        my_stack = [asteroids[0]]

        for astr2 in asteroids[1:]:
            my_stack.append(astr2)

            while len(my_stack) >= 2 and (my_stack[-2] > 0 and my_stack[-1] < 0):

                ast1, ast2 = my_stack.pop(), my_stack.pop()
                if abs(ast1) == abs(ast2):
                    continue
                elif abs(ast1) > abs(ast2):
                    my_stack.append(ast1)
                else:
                    my_stack.append(ast2)
        return my_stack
    
# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height)-1

        def get_max_water(lp_idx, rp_idx):
            return min(height[lp_idx], height[rp_idx]) * (rp_idx-lp_idx)

        max_water = get_max_water(lp, rp)

        while lp < rp:
            if (height[lp] < height[rp]):
                lp += 1
            else:
                rp -= 1

            max_water = max(max_water, get_max_water(lp, rp))

        return max_water

# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        my_stack = [intervals[0]]

        for curr in intervals[1:]:
            prev = my_stack[-1]

            if prev[0] <= curr[0] and prev[-1] >= curr[1]:
                my_stack[-1] = prev
            elif prev[0] >= curr[0] and prev[1] <= curr[1]:
                my_stack[-1] = curr
            elif prev[0]<=curr[0]<=prev[1] and curr[0]<=prev[1]<=curr[1]:
                my_stack[-1] = [prev[0], curr[1]]
            elif curr[0]<=prev[0]<=curr[1] and prev[0]<=curr[1]<=prev[1]:
                my_stack[-1] = [curr[0], prev[1]]
            else:
                my_stack.append(curr)


        return my_stack

# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        my_stack = []

        for char in s:
            if char not in close_to_open:
                my_stack.append(char)
                continue
                
            if not my_stack or my_stack[-1] != close_to_open[char]:
                return False

            if my_stack[-1] == close_to_open[char]:
                my_stack.pop()

        return not my_stack
