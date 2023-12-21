class Solution:
    def dailyTemperatures(self, temperatures):

        res = [0 for i in range(len(temperatures))]

        i = 0
        stack = [[temperatures[0], i]]

        while i < len(temperatures)-1:
            next_temp = temperatures[i+1]
        
            while stack and next_temp > stack[-1][0]:
                last_ele, last_idx = stack.pop()
                res[last_idx] = (i+1) - last_idx

            i += 1
            stack.append([next_temp, i])

        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))