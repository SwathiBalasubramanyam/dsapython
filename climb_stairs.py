class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 
        if n == 2:
            return [(1,1), (2,)]

        total_combinations = set()

        for i in range(1, n):

            sub_combinations_1 = self.climbStairs(i)
            sub_combinations_2 = self.climbStairs(n-i)

            for comb_1 in sub_combinations_1:
                for comb_2 in sub_combinations_2:
                    total_combinations.add(comb_1 + comb_2)
                    total_combinations.add(comb_2 + comb_1)

        return total_combinations

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2
        x = 0

        for i in range(2, n):
            x = prev1 + prev2
            prev1 = prev2
            prev2 = x

        return x
