class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        prefix_sum = []

        start = 0
        for ele in possible:
            if ele == 0:
                ele = -1
            start += ele
            prefix_sum.append(start)

        for idx, alice_score in enumerate(prefix_sum):
            level = idx+1
            bobs_score = prefix_sum[-1] - alice_score
            if alice_score > bobs_score:
                return level

        return -1