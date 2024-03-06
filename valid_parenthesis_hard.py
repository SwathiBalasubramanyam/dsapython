class Solution:
    def checkValidString(self, s: str) -> bool:

        my_stack = []
        
        for jdx, char in enumerate(s):
            if char != ")":
                my_stack.append(char)
                continue

            my_stack.reverse()
            replaced_parenthesis = False

            for idx, charn in enumerate(my_stack):
                if charn != "(":
                    continue
                my_stack = my_stack[0:idx] + my_stack[idx+1:]
                my_stack.reverse()
                replaced_parenthesis = True
                break

            if replaced_parenthesis:
                continue

            if not my_stack:
                return False

            last_ele = my_stack.pop()
            if last_ele != "*":
                return False
            
        my_stack_str = "".join(my_stack)

        while "(*" in my_stack_str:
            my_stack_str = my_stack_str.replace("(*", "")

        my_stack = list(my_stack_str)

        return len(list(filter(lambda el: el not in ("", "*"), my_stack))) == 0
