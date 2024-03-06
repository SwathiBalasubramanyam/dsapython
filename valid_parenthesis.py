class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ele in s:
            if ele not in close_to_open:
                stack.append(ele)
                continue

            last_ele = stack.pop()
            if close_to_open[ele] != last_ele:
                return False

        return len(stack) == 0

print(Solution().isValid("{[]}"))