

class Solution:
    def carFleet(self, target, position, speed):
        final_lst = sorted(zip(position, speed))

        stack = []

        for eles in final_lst:
            pos, sp = eles
            time_to_dest = (target - pos) / sp
            if not stack or time_to_dest < stack[-1]:
                stack.append(time_to_dest)
            else:
                while stack and time_to_dest > stack[-1]:
                    stack.pop()
                stack.append(time_to_dest)
            
        return len(stack)
        

print(Solution().carFleet(10, [0,4,2], [2,1,3]))