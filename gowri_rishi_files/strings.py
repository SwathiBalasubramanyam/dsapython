# print (chr(97))

# ip = "a4k3z2"
# out = ''

# for c in ip:
#     if c.isalpha():
#         alpha = c
#     else:
#         o = ord(alpha)
#         o = o + int(c)
#         out = out + alpha + chr(o)

# print (out)

        
# ip = "aaacccdddbbb"

# o  = ''
# for c in ip:
#     if c not in o:
#         o = o + c

# print (o)


# s = "ABAACDDDBBA"
# mc =0
# c =1

# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         if c > mc:
#             mc = c
#             a = s[i]
#             c =1

# print (mc,a)

# s ="a4b3c2"
# out =''
# i = 0
# while i < len(s):
#     out += s[i]*int(s[i+1])
#     i += 2

# print (out)

# c =1
# out = ''
# s = "aaaabbbccz"

# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         out = out + str(c) + s[i]
#         c =1
# out = out + str(c) + s[i+1]
# print (out)


######################################################################################################
######################################################################################################
#Function to check if X can be derived from Y by rotating it
# X = "ABCD"
# Y = "DABC"

# for i in range(len(X)):


#     X = X[1:] + X[0]

#     if X == Y:
#         print ("True")
#         break

# print ("False")


######################################################################################################
######################################################################################################
# Function to check if X and Y are anagrams or not


X = "tommarvoloriddle"  # Tom Marvolo Riddle
Y = "iamlordvoldemort"  # I am Lord Voldemort

d ={}
for i in X:
    d[i] = d.get(i,0) +1

for i in Y:
    d[i] = d.get(i)
    d[i] = d[i] -1
    if d[i] ==0:
        del d[i]

if d:
    print ("fail")
else:
    print ("pass")


######################################################################################################
######################################################################################################
# check palindrome


s ="xxxxx"

i = 0
j = len(s)-1

while i < j:
    print (s[i],s[j])
    if s[i] != s[j]:
        print ("Fail")
        break
    i +=1
    j -=1


######################################################################################################
######################################################################################################
# Function to remove adjacent duplicates characters from a string

s = "AAABBCDDD"
prev = None
out = ''
for i in s:
    if i != prev:
        out = out + i
    prev = i

print (out)











    
