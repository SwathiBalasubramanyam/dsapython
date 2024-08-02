class NumArray:
    #  this implementation creates an extra variable called prefix_sum and computes the sum once nd can be retrieved in o(1) time for rest of the queries
    def __init__(self, nums: List[int]):
        self.nums = nums
        sum_so_far = 0
        self.prefix_sum = []
        for ele in self.nums:
            sum_so_far += ele
            self.prefix_sum.append(sum_so_far)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left-1]
    

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    #  here it is always going to be o(n) as we are slicing 
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left: right+1])