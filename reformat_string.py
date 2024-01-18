class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        alphas = []

        for ele in s:
            if ele.isdecimal():
                nums.append(ele)
            else:
                alphas.append(ele)

        if len(alphas) == 1 and len(nums) == 0:
            return alphas[0]

        if len(nums) == 1 and len(alphas) == 0:
            return nums[0]

        if not nums or not alphas:
            return ""

        if len(nums) == len(alphas):
            new_str = ""
            for ele in zip(nums, alphas):
                new_str += ele[0]
                new_str += ele[1]
            return new_str

        if max(len(nums), len(alphas)) - min(len(nums), len(alphas)) != 1:
            return ""

        if len(nums) > len(alphas):
            new_str = ""
            for ele in zip(nums, alphas):
                new_str += ele[0]
                new_str += ele[1]
            new_str += nums[-1]
            return new_str
        else:
            new_str = ""
            for ele in zip(alphas, nums):
                new_str += ele[0]
                new_str += ele[1]
            new_str += alphas[-1]
            return new_str

        
            