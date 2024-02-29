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
