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


