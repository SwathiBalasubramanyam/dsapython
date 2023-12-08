# DO NOT EDIT - Example of a multiline string
print('''
Here is a whole bunch of instruction that you'd better follow if you know what's good for you!

It even includes blank lines. :)
''')

# STEP 1: Write your own print statement on multiple lines

print(''' thi sis my multiline statement.
the beauty of this is you can just continue on the sam eline or 
enter new line

''')


# DO NOT EDIT
print('***BEFORE***')

# STEP 2: Copy the original multiline print and make it show
# without blank lines at the beginning and the end
print('''
Here is a whole bunch of instruction that you'd better follow if you know what's good for you!

It even includes blank lines. :)
''')

# DO NOT EDIT
print('***AFTER***')
print()

# STEP 3: Uncomment the following print command and fix the error
print('What\'s up, doc?')

# STEP 4: Uncomment the following print command and fix the error
print("The poet used \"day\" to mean \"life\".")

# STEP 5: Uncomment the following print command and fix the error
print('''The bunny said, "Let's go to the library."''')

# DO NOT EDIT - Sample debug for an equality operation
num = 5
str = "5"
print('num {0}, str {1}, equal? {2}'.format(num, str, num==str))

# STEP 6: Rewrite the print above in an alternate way using f' on the string

print(f'num {num}, str {str}, equal? {num==str}')


print ('*'*100)

def compare(str1, str2):
    return len(str1) == len(str2)


print(compare("AB", "CD"))              #> True
print(compare("ABC", "DE"))             #> False
print(compare("hello", "App Academy"))  #> False

# Write your function, here.

def format_name(fn, ln):

    return f"Hi, my name is {fn} {ln}"

print(format_name("Alex", "Ambrose"))  #> Hi, my name is Alex Ambrose
print(format_name("Amy", "Mayer"))     #> Hi, my name is Amy Mayer
print(format_name("Rick", "Morty"))    #> Hi, my name is Rick Morty

def index_string(str):
    return str[3:-1]

print(index_string("Alchemy"))     #> hem
print(index_string("Ridiculous"))  #> iculou
print(index_string("Serendipity")) #> endipit

def index_of(str, char):
    return str.lower().index(char) or None

print(index_of("Arm", "a"))  #> 0
print(index_of("Pie", "e"))  #> 2
print(index_of("Lucid", "i"))  #> 3
print(index_of("Obvious","u"))  #> 5

def long_burp(num):
    return "Bu" + "r"*num + "p"

print(long_burp(3))  #> "Burrrp"
print(long_burp(5))  #> "Burrrrrp"
print(long_burp(9))  #> "Burrrrrrrrrp"

def last_three(str, comp_str):

    return str.lower()[-3:] == comp_str.lower()

print(last_three("Power", "wer"))  #> True
print(last_three("Application", "App"))   #> False
print(last_three("Raw", "raw"))   #> True
print(last_three("Bonjour", "OUR"))   #> True

def is_palindrome_1(str):
    return str == str[::-1]

def reverse_str(str):
    if not str:
        return ""
    return str[-1] + reverse_str(str[0:-1])

def is_palindrome(str):
    return str == reverse_str(str)

print("*"*100)
print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False

print("*"*100)
def is_same_num(num1, num2):
    return num1 == num2


print(is_same_num(4, 8))   #>  False
print(is_same_num(2, 2))   #>  True
print(is_same_num(2, "2")) #>  False

print("*"*100)
def not_equal(num1, num2):
    return num1 != num2

print(not_equal(0, 2))   #>  True
print(not_equal(2, 2))   #>  False
print(not_equal(2, "2")) #>  True

print("*"*100)
def And(bool1, bool2):
    return bool1 and bool2

print(And(True, False))    #> False
print(And(True, True))     #> True
print(And(False, True))    #> False
print(And(False, False))   #> False

print("*"*100)

def not_or(bool1, bool2):
    return not bool1 or bool2

print(not_or(True, False))    #> False
print(not_or(True, True))     #> True
print(not_or(False, True))    #> True
print(not_or(False, False))   #> True

print("*"*100)
def length_list(list, list_len):
    return len(list) == list_len

print(length_list([], 1))   #>  False
print(length_list([], 0))   #>  True
print(length_list([5, 2], 2))   #>  True
print(length_list([1, 4, 3], 4))   #>  False
print(length_list([0, 2, "i", 0.9], 4))   #>  True

print("*"*100)
def has_remainder(num1, num2):
    return bool(num1%num2)

print(has_remainder(4, 2))   #>  False
print(has_remainder(57, 4))  #>  True
print(has_remainder(6, 3))   #>  False
print(has_remainder(81, 7))  #>  True

print("*"*100)
def xor(arg1, arg2):
    return arg1 ^ arg2

print(xor(False, False))   #>  False
print(xor(True, False))   #>  True
print(xor(True, True)) #>  False
print(xor(5, 3))  #> 6
print(xor(8, 4))  #> 12
print(xor(2, 2))  #> 0
print(xor(1, 2))  #> 3
print(xor(4, 4))  #> 0

print("*"*100)

def de_morgans_law(x, y):
    return not(x and y)


print(de_morgans_law(True, True)) # False
print(de_morgans_law(True, False)) # True
print(de_morgans_law(False, False)) # True
print(de_morgans_law("", [])) # True
print(de_morgans_law(2, 2)) # False
print(de_morgans_law(2, 0)) # True


print("*"*100)

def addition(num1, num2):
    return num1 + num2

print(addition(2, 3))   #> 5
print(addition(-3, -6)) #> -9
print(addition(7, 3))   #> 10


# DO NOT EDIT - Setup for exploration
# tiny number
int1 = 5
float1 = 5.0
# small number
int2 = 135
float2 = 135.246
# huge number known as `googol`
int3 = 10**100
float3 = 10.0**100

# STEP 1: Print and compare tiny numbers
print('** FIVE **')
# 1A: Print int1
print(int1)
# 1B: Print float1
print(float1)
# 1C: Print equality comparison (==) between int1 and float1
print(int1 == float1)

# STEP 2: Print and compare huge numbers
print('\n** GOOGOL **')
# 2A: Print int3
print(int3)
# 2B: Print float3
print(float3)
# 2C: Print equality comparison (==) between int1 and float3
print(int3 == float3)

# STEP 3: Compare results of integer division in all 4 possible combinations
print('\n** INTEGER DIVISION **')
# 3A: Print int2 divided by int1 (//)
# 3B: Print float2 divided by float1 (//)
# 3C: Print float2 divided by int1
# 3D: Print int2 divided by float1
print(int2 // int1)
print(float2 // float1)
print(float2 // int1)
print(int2 // float1)

# STEP 4: Compare results of mod in all 4 possible combinations
print('\n** MOD **')
# Copy/paste 4 statements from STEP 3 and switch operator to mod (from // to %)
print(int2 % int1)
print(float2 % float1)
print(float2 % int1)
print(int2 % float1)

print("*"*100)

def increment(num):
    return num+1

print(increment(0))   #> 1
print(increment(9))   #> 10
print(increment(-3))  #> -2

print("*"*100)

def min2sec(min):
    return min * 60
print(min2sec(5)) #> 300
print(min2sec(3)) #> 180
print(min2sec(2)) #> 120

print("*"*100)
def how_many_legs(chick, cow, pig):
    return chick * 2 + cow * 4 + pig * 4

print(how_many_legs(2, 3, 5))    #> 36
print(how_many_legs(1, 2, 3))    #> 22
print(how_many_legs(5, 2, 8))    #> 50

print("*"*100)
def integer_division(n1, n2):
    return n1 // n2

print(integer_division(5.0, 2))     #> 2.0
print(integer_division(10, 10))     #> 1
print(integer_division(60, 8.0))    #> 7.0
print(integer_division(5.0, 1.0))   #> 5.0
print(integer_division(8, 2))       #> 4

