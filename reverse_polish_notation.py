class Solution:
    def evalRPN(self, tokens) -> int:

        stack = []
        valid_operators = ["+", "-", "*", "/"]

        for ele in tokens:
            if ele not in valid_operators:
                stack.append(int(ele))
                continue

            last_ele = stack.pop()
            prev_last_ele = stack[-1]

            if ele == "+":
                stack[-1] = prev_last_ele + last_ele 
            elif ele == "-":
                stack[-1] = prev_last_ele - last_ele 
            elif ele == "*":
                stack[-1] = prev_last_ele * last_ele 
            else:
                stack[-1] = prev_last_ele // last_ele 

            print(stack)

        return stack[-1]

print(Solution().evalRPN(["10","-1","*","17","+","5","+"]))