from collections import deque

class Solution:

    def generateParenthesis(self, n):
        queue = deque([""])
        while not all(map(lambda ele: len(ele) == n*2, queue)):
            ele = queue.popleft()

            if ele.count("(") < n:
                queue.append(ele + "(")

            if ele.count(")") < ele.count("("):
                queue.append(ele + ")")

        return list(queue)


print(Solution().generateParenthesis(3))