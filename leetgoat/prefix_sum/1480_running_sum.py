class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # o(n) time and o(1) space
        sum_so_far = 0
        for idx, ele in enumerate(nums):
            sum_so_far += ele 
            nums[idx] = sum_so_far
        return nums
    
    def runningSum(self, nums: List[int]) -> List[int]:
        # with extra space
        # o(n) time and space
        sum_so_far = 0
        prefix_sum = []
        for ele in nums:
            sum_so_far += ele 
            prefix_sum.append(sum_so_far)
        return nums