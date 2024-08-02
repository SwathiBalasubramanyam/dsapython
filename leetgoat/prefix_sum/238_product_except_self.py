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