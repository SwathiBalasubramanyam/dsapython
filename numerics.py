print("*"*100)
def find_digit_amount(num1):
    return len(str(num1))

print(find_digit_amount(123))           #> 3
print(find_digit_amount(-56))           #> 2
print(find_digit_amount(7154))          #> 4
print(find_digit_amount(61217311514))   #> 11
print(find_digit_amount(0))             #> 1

print("*"*100)
def perfect_square(num1, num2):
    return num2 * num2 == num1

print(perfect_square(15, 5)) #> False
print(perfect_square(25, 5)) #> True
print(perfect_square(81, 9)) #> True
print(perfect_square(9, 2))  #> False

print("*"*100)

def recursive_fib(nth):
    if nth == 1 or nth == 2:
        return 1
    return recursive_fib(nth-1) + recursive_fib(nth-2)

print(recursive_fib(1))     #> 1
print(recursive_fib(2))     #> 1
print(recursive_fib(4))     #> 3
print(recursive_fib(6))     #> 8
print(recursive_fib(12))    #> 144

print("*"*100)
def recursive_countdown(num):
    if num <= 0:
        return
    print(num)
    recursive_countdown(num-1)    

recursive_countdown(5) #> 5 4 3 2 1

print("*"*100)

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(1))  #> False
print(is_prime(2))  #> True
print(is_prime(3))  #> True
print(is_prime(5))  #> True
print(is_prime(9))  #> False
print(is_prime(15)) #> False

print("*"*100)
def divisible_by_five(num):
    return num % 5 == 0

print(divisible_by_five(5))    #> True
print(divisible_by_five(-55))  #> True
print(divisible_by_five(37))   #> False

print("*"*100)

def calculate_exponent(base, exp):
    return base ** exp

print(calculate_exponent(5, 5))     #> 3125
print(calculate_exponent(10, 10))   #> 10000000000
print(calculate_exponent(3, 3))     #> 27

print("*"*100)

def remainder(num1, num2):
    return num1 % num2

print(remainder(1, 3))  #> 1
print(remainder(3, 4))  #> 3
print(remainder(5, 5))  #> 0
print(remainder(7, 2))  #> 1


# Write your function, here.

print("*"*100)
def first_before_second(sent, char1, char2):
    index_of_char2 = sent.index(char2)

    for i in range(len(sent)):
        if sent[i] == char1 and i > index_of_char2:
            return False

    return True

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

print("*"*100)

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]
list3 = [2, 3]

# Use "==" to compare these values and see what gets printed! How does this
# compare with JavaScripts "==="?

# Compare "x" with itself
print(x == x)
# Compare "x" with "y"
print(x == y)

# Compare "list1" with "list2"
print(list1 == list2)
# Compare "list1" with "list3"
print(list1 == list3)

print("*"*100)

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]

print(x == x) # True
print(x is x) # True
print(x != y) # True
print(x is not y) # True
print(list1 == list2) # True
print(list1 is list2) # False
print(list1 != list2) # False
print(list1 is not list2) # True

def largestPerimeter(nums):
    nums.sort(reverse=True)

    for i in range(len(nums)-2):
        a = nums[i]
        b = nums[i+1]
        c = nums[i+2]

        if a < b+c:
            return a+b+c
    return 0    

print(largestPerimeter([2,1,2]))
print(largestPerimeter([1,2,1,10]))