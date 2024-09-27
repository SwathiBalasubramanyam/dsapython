class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2

        num_cnt = defaultdict(int)

        for num in nums:
            num_cnt[num] += 1

            if num_cnt[num] > majority:
                return num
        