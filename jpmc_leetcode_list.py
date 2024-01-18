
def get_sum(num):
    num_sum = 0
    while num > 9:
        num_sum += (num % 10) ** 2
        num = num // 10
    num_sum += num**2
    return num_sum


def happy_number(num):

    while len(str(num)) > 1:
        num = get_sum(num)
    return num == 1 or n == 7

print(happy_number(19))

class Solution:
    def isValid(self, s: str) -> bool:
        
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        my_stack = []
        for char in s:
            if char in close_to_open:
                if not my_stack or close_to_open[char] != my_stack[-1]:
                    return False
                my_stack.pop()
            else:
                my_stack.append(char)

        return not my_stack

print(Solution().isValid("()"))
