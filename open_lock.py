from collections import deque

class Solution:
    def openLock(self, deadends, target) -> int:

        def _children(lock):
            res = []
            for idx, digit in enumerate(lock):
                clockwise = (int(digit) + 1) % 10
                counterclockwise = (int(digit)-1 + 10) % 10

                res.append(lock[:idx] + str(clockwise) + lock[idx+1:])
                res.append(lock[:idx] + str(counterclockwise) + lock[idx+1:])

            return res

        queue = deque([("0000", 0)])
        visited = set(deadends)

        while queue:
            lock, level = queue.popleft()

            if lock == target:
                return level

            children = _children(lock)

            for child in children:
                if child in visited:
                    continue
                visited.add(child)
                queue.append((child, level+1))

        return -1
        
print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))