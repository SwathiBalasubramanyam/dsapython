# def valid_brackets():

#     m = { 
#         "]" : "[",
#         ")" : "(",
#         "}" : "{"
#         }

#     str1 = "AA{[({[()]})]]}AA"

#     s =[]

#     for bracket in str1:
#         if bracket in m.values():
#             s.append(bracket)
#         else:
#             if len(s) > 0 and s[-1] == m[bracket]:
#                 s.pop()
#             else:
#                 return False

#     return len(s) == 0

# print (valid_brackets())



m = { "]" : "[" , "}" : "{" , ")" : "("}

s = "()(){[]}}"

o = []
for bracket in s:
    if bracket in m.values():
        o.append(bracket)
    else:
        if len(o) > 0 and o[-1] == m[bracket]:
            o.pop()
        else:
            print ("error")

if not len(o) == 0:
    print ("error")




m = 10 
k = 11


print ("The val of m is {} and k is {} ".format(m,k))