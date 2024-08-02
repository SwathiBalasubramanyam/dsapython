class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        prefix_sum = []
        for ele in nums:
            prefix_sum.append(total_sum)
            total_sum += ele

        for idx, ele in enumerate(nums):
            before = prefix_sum[idx]
            after = total_sum-before-ele
            if before == after:
                return idx

        return -1