def is_palindrome(num):
    return num == reverse(num)

def reverse(num):
    rev = 0
    while num:
        rem = num % 10
        num //= 10
        rev = rev*10 + rem
    return rev

print(is_palindrome(152))
print(is_palindrome(343))