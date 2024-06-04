class Solution:
    def maxSubArray(self, nums=[1,2,-1,-2,2,1,-2,1,4,-5,4]):
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        
        print(max_sum)
        
Solution().maxSubArray()
    
