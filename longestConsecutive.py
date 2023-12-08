from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        max_length, curr_length = 0, 1
        lp, rp = 0, 1

        while rp < len(nums):

            if nums[rp] == (nums[rp-1] + 1):
                curr_length += 1
            else:
                max_length = max(max_length, curr_length)
                curr_length = 1
                lp = rp
                
            rp += 1
            
        return max(max_length, curr_length)


print(Solution().longestConsecutive([1,2,0,1]))