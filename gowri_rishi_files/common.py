#import pdb
# def two_sum2(numbers, target):
#     m = set()
#     for num in numbers:
#         if (target - num) in m:
#             print ("hello")
#             return True
#         m.add(num)
#     return False

# print(two_sum2([1, 3, 7], 8) == True)
# print(two_sum2([1, 3, 7], 6) == False)
# print(two_sum2([], 1) == False)
# print(two_sum2([1, 1], 2) == True)
# print(two_sum2([1], 1) == False)


# #stock max profit

# def maxProfit(prices):
#     max_profit, min_price = 0, float('inf')
#     for price in prices:
#         min_price = min(min_price, price)
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#     return max_profit

# print (maxProfit([7,1,5,3,6,4]))


# #Given an integer n, return any array containing n unique integers such that they add up to 0.

# def sum2zero(n):
#     return list(range(1-n,n,2))

# print (sum2zero(2))

# # 1374. Generate a String With Characters That Have Odd Counts
# def oddcount(n):
#     if n%2!=0: 
#         return 'a'*n 
#     else: 
#         return "a"*(n-1)+'b'

# print (oddcount(3))


# # s = "Generate a String With Characters"
# # n = ["1","2","3"]
# # print ("".join(x[:-1] for x in (s.split())))

# # s = "123"
# # print (s[::-1])



# # m = "reverse the sentence"
# # m1 = m.split()

# # print (" " .join([x[::-1] for x in (m.split()[::-1])]))

# from collections import Counter

# s = []

# print (s[-1])
# # l = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
# # m = Counter(l)
# # for k,v in m.items():
# #     print (k,v)

# def removeDuplicates(S):
#     stack = []
#     for c in S:
#         if stack and stack[-1] == c:
#             stack.pop()
#         else:
#             stack.append(c)
#     return ''.join(stack)


# print (removeDuplicates("abbaca"))

# mat =   [[1,2,3,4,5],
#         [11,12,13,14,15],
#         [21,22,23,24,25]]

# out = []

# for i in range(len(mat)):
#     s = 0
#     for j in range(len(mat[i])):
#         s += (mat[i][j])
#     out.append(s)

# print (out)

# def commonChars(A):
#     res = []
#     try:
#         key_set = set(A[0])
#     except IndexError:
#         return res
    
#     for ch in key_set:
#         l1 = [w.count(ch) for w in A]
#         n = min(l1)
#         if n:
#             res.extend([ch]*n)

#     return res
    
#print (commonChars(["bella","label","roller"]))


# words = ["cat","bt","hat","tree"] 
# chars = "atach"
# setofchars = set(chars)
# for word in words:
#     for alpha in word:
#         if alpha in setofchars:
#             print (alpha)


# def fib(N):
#     a, b = 0, 1
#     for i in range(N): 
#         b = a + b
#         a = b
#     return a

# print(fib(4))

# def oddnum(l1):

#     c =0
#     for i in l1:
#         if i%2 !=0 :
#             c +=1
#             if c ==3:
#                 return True
#         else:
#             c = 0
#     return False

# print (oddnum([1,3,3,4,5]))


# def diagmat():
# a = ("John", "Charles", "Mike","hi")
# b = ("Jenny", "Christy", "Monica","hello")

# x = zip(a, b)

# print (list(x))

# m = [[1,2,3,4],
#      [5,1,2,3],
#      [9,5,11,2]]

# for i in range(len(m)-1):
#     for j in range(len(m[0])-1):
#         if m[i][j]  != m[i+1][j+1]:
#             print ("False")
# print  ("True")



# def findWords(words):
#     line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
#     ret = []
#     for word in words:
#       w = set(word.lower())
#       if w <= line1 or w <= line2 or w <= line3:
#         ret.append(word)
#     return ret

# print (findWords(["Hello", "Alaska", "Dad", "Peace"]))

# m = [2,2,3,4]
# from collections import Counter

# f = Counter(m)

# import pdb;pdb.set_trace()
# m = -1
# for a in f:
#     if a == f[a]:
#         m = max(m,f[a])
# print (m)

# nums = [0,1,0,3,12]
# zero = 0  # records the position of "0"
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i], nums[zero] = nums[zero], nums[i]
#         zero += 1


# S = "ABCD"
# S, i, j = list(S), 0, len(S) - 1
# while i < j:
#     # if not S[i].isalpha():
#     #     i += 1
#     # elif not S[j].isalpha():
#     #     j -= 1
#     # else:
#         S[i], S[j] = S[j], S[i]
#         i, j = i + 1, j - 1
# print  ("".join(S))


# m = [1,2,1,3]

# incr = False
# decr = False

# for i in range(len(m)-1):


#     if m[i] < m[i+1]:
#         incr = True
#     if m[i] > m[i+1]:
#         decr = True
#     if decr and incr:
#         print ("False")
    
# print ("True")

# d = {"1": "a","2" : "b"}
# d1 = {"2": "b","1" : "a","3":"c"}

# if d == d1:
#     print ("equal")
# else:
#     print ("ne")


# 


# m = 5 

# for i in range(m+1):
#     for j in range(i):
#         print (m,end=" ")
#     print()


# def triangle(n): 
    
#     k = 2*n-2
#     for i in range(n):

#         # for j in range(0,k):
#         #     print (end = " ")

#         for j in range(i+1):
#             print ("*",end= " ")

#         k = k-1

#         print () 
  
# # Driver Code 
# n = 5
# triangle(n) 

# l =[1,2,3,1]

# s = set(l)
# print (len(s))

# s ="abcd"
# t = "abcde"

# d = {}
# for i in s:
#     d[i] = 1

# for i in t:
#     if d.get(i,0) == 0:
#         print (i)

# all(a.isupper() for a in word) or 
# all(a.islower() for a in word) or 
# (word[0].isupper()and all(word[a].islower() for a in range(1,len(word)))))

# s ="lllleetcode"
# d ={}

# for i,a in enumerate(s):
#     if a not in d:
#         d[a] = 1
        
#     else:
#         d[a]+= 1

# print (d)

# m =sorted(d)
# print (m)

# from collections import Counter
# c = Counter(s)
# print (c)

# #import pdb;pdb.set_trace()
# l1n=[1,2,3,1,1,1,1,1]

# m = list(range(9))

# m.reverse()
# for i in m:
#     print (i)


# print (set(l1n))

# from collections import Counter

# m = (Counter(l1n))

# for k,v in m.items():
#     print (k,v)

# s = "aaabbbcc"
# c = 1
# o = ''
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         o = o + s[i] + str(c)
#         c = 1

# o = o + s[i] + str(c)
# print (o)

# s = "abcdefg"
# k = 2

# pdb.set_trace()       
# if len(s) < k:
#     print  (s[::-1])
# m = s[:k:-1] + s[k:]
# print("".join(m))
        
# nums = [88,1,2,2,3]
# dic = {}
# sorted_list = sorted(nums)

# for i,n in enumerate(sorted_list):
#     if n not in dic:
#         dic[n] = i
# print  ([dic[n] for n in nums])

# i = 2222
# m = ((len(str(i))) % 2 == 0)
# print (m)

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]

# pdb.set_trace()
# n = len(mat)
# mid = n//2
# su = 0
# for i in range(n):
    
#     su += mat[i][i]
#     print ([n-1-i])
#     su += mat[n-1-i][i]

# if n % 2 != 0:
#     su -=  mat[mid][mid]

# print (su)


# nums = [88,1,2,89,2,3,90]

# f = s  = m = 0


# for num in nums:
#     if num > f:
#         s = f
#         f = num
#     elif num > s:
#         s= num

# print (f,s)
    

# m = [[1,1,0],[1,0,1],[0,0,0]]

# t = []
# for row in m:
    
#     row =row[::-1]
#     print (row)
#     for bit in row:
#         bit = 1-bit
#     t.append(row)
# print (t)


# grid = [[4,3,2,-1],
#         [3,2,1,-1],
#         [1,1,-1,-2],
#         [-1,-1,-2,-3]]


# row_len = len(grid[0])
# col_len = len(grid)

# i = 0 
# j = row_len - 1
# total = 0

# while i < col_len and j >= 0:
#     val = grid[i][j]
#     if val < 0:
#         total +=     - i
#         j -= 1
#     else:
#         i += 1
# print (total)

# prices = [8,4,6,2,3]

# res, stack = prices[:], []
# for i, price in enumerate(prices):
#     while stack and prices[stack[-1]] >= price:
#         res[stack.pop()] -= price
#     stack.append(i)
# print (res)


# A = [17,18,5,4,6,1]
# mx = -1
# for i in range(len(A) - 1, -1, -1):
#     A[i], mx = mx, max(mx, A[i])
# print (A)


# A = [17,18,5,4,6,1]
# mx = 1

# for i in range(len(A)-1,-1,-1):
#     cval = A[i]
#     A[i] = mx
#     mx = min(cval,mx)

# print (A)

    
# A = [17,18,5,4,6,1,33,2,43,7,6,5,4]

# mi = A[0]
# for i in range(len(A)-1):
#     vcal = A[i]
#     A[i] = mi
#     mi = min(mi,vcal)

# print (A)

# s = "cc"
# c = 1
# fc = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         fc = max(fc,c)
#         c = 1

# print (fc)



# l1 = [1,1,1,1,2,2,2,3,3,3,3,5,6,7,7,7]

# from collections import Counter

# m =Counter(l1)

# print (m)
# for k in m:
#     if m[k] > 1:
#         print (m[k])


# listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']

# d ={}
# for i,v in enumerate(listOfElems):
#     if v not in d:
#         d[v] = [1 ,[i]]        
#     else:
#         d[v][0] += 1
#         d[v][1].append(i)

# import pprint
# pprint.pprint (d)


# A = [-2,-3,-4,-1,-3,-4,-5,-6]


# fm =0 
# fm =cm = m[0]
# for num in m[1:]:
#     cm = max(num+cm,num)
#     fm = max(fm,cm)
# print (fm)


# curSum = maxSum = A[0]
# for num in A[1:]:
#     curSum = max(num, curSum + num)
#     maxSum = max(maxSum, curSum)

# print (maxSum)


# s1 = "{}[]{}[]0{}{}"


# m = { "]" : "[" , "}" : "{" , ")" : "("}

# s = []

# for bracket in s1:
#     if bracket in m.values():
#         s.append(bracket)
#     else:
#         if len(s) > 0 and s[-1] == m[bracket]:
#             s.pop()
#         else:
#             print ("error")
    

# if len(s) != 0:
#     print ("error")
# else:
#     print ("pass")



# Explanation:
# opened count the number of opened parenthesis.
# Add every char to the result,
# unless the first left parenthesis,
# and the last right parenthesis.

# S= "(()())(())"

# res, opened = [], 0
# for c in S:
#     if c == '(' and opened > 0: 
#         res.append(c)
#     if c == ')' and opened > 1: 
#         res.append(c)
#     if c == '(':
#         opened += 1 
#     else:
#         opened += -1
# print ("".join(res))


# l = [10,5,6,7,12,56,0,90]

# f,s = 0,0

# for num in l:
#     if num > f:
#         s = f
#         f = num
#     elif num >s:
#         s = num

# print (f,s)



# s = "Let's take LeetCode contest"


# m = s.split(" ")
# o = []
# for i in m:
#     o.append(i[::-1])

# print (' '.join(o))


# ip ="abbaca"

# s = []

# for i in ip:
#     if s and s[-1] == i:
#         s.pop()
#     else:
#         s.append(i)

# print (s)


# salary = [4000,3000,1000,2000]

# m = float("inf")
# M = float("-inf")
# s = 0
# for sal in salary:
#     s += sal
#     m = min(m,sal)
#     M = max(M,sal)

# avg = (s-M-m)/(len(salary)-1)
# print (avg)


# a =0
# b = 1
# N = 5
# for i in range(N):
#     a,b = b,a+b


# arr = [1,2,34,3,4,5,7,23,12]
# c =0

# for num in arr:
#     if num%2 != 0:
#         c+=1
#         if c ==3 :
#             print ("True") 
#     else:
#         c = 0
# print ("False")


# matrix = [
#   [1,2,3,4],
#   [15,11,12,13],
#   [29,25,21,22],
#   [35,31,32,33],
#   [49,45,41,42]
# ]



# r = len(matrix)-1
# c = len(matrix[0])-1



# for i in range (r):
#     for j in range(c):
#         print (matrix[i][j])


# print (arr[:4])
# #import pdb;pdb.set_trace()
# arr = [1,2,2,3,3,3]
# n = len(arr)
# cnt = [0] * (n + 1)
# for a in arr:
#     if a <= n:
#         cnt[a] += 1
# for i in range(n, 0, -1):
#     if cnt[i] == i:
#         print (i)
# print  ("-1")



# s = "abbcccddddeeeeedcba"

# c =1
# fc = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         c =1
# from collections import Counter


# c = Counter(arr)
# print (c)


# s = "a-bC-dEf-ghIj"

# i= 0
# j = len(s)-1

# s = list(s)

# while i < j:
#     if not s[i].isalpha():
#         i += 1
#     if not s[j].isalpha():
#         j -= 1
#     else:
#         s[i],s[j] = s[j],s[i]
#         i += 1
#         j -= 1

# print ("".join(s))

# nums = [0,1,0,3,12]
# j = 0

# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[i],nums[j] = nums[j],nums[i]
#         j += 1


# ip = [1,100,9]

# inc = False
# dec = False


# for i in range(len(ip)-1):

#     if ip[i] < ip[i+1]:
#         inc = True
#     if ip[i] > ip[i+1]:
#         dec = True
#     if inc and dec:
#         print ("Fail")

# print ("pass")

# p = [7,1,5,3,6,4]
# profit =0

# for i in range(len(p)-1):
#     if p[i] < p[i+1]:
#         profit = profit + p[i+1] - p[i]

# print (profit)


# s = "anagram"
# t = "nagaram"


# d1 ={}
# d2 ={}

# for a in s:
#     d1[a] = d1.get(a,0)+1
# for b in t:
#     d2[b] = d2.get(b,0)+1
# if d1 == d2:    
#     print ("True")
# else:
#     print ("false")


# ones = [1,1,0,1,1,1]
# c =0
# fc = 0
# for num in ones:
#     if num ==1:
#         c += 1
#         fc = max(fc,c)
#     else:    
#         c = 0

# print (fc)


dup =[1,0,2,3,0,4,5,0]


i = 0
while i < len(dup):
    if dup[i] == 0:
        dup.insert(i+1,0)
        dup.pop()
        i +=1 
    i += 1

print (dup)


stock = [7,1,5,3,6,4]

minv = float("inf")
cp = 0
mp = 0

for i in stock:
    minv = min(i,minv)
    cp = i - minv
    mp = max(mp,cp)


s = "abc"
t = "zzz"


# for i in range(len(s)-1):
#     try:
#         ind = t.index(s[i])
#     except ValueError:
#         print ("False")
#     t =t[ind+1:]
# print ("True")


# s = "aabbbbccccc"

# c =1
# mc = 1
# l = ''

# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         if c > mc:
#             mc = c
#             l = s[i]
#         c =1
# if c > mc:
#     mc = c
#     l = s[i]
# print (mc,l)

# l1 =[10,12,1,4,2,9]



# print (sorted(l1))
# print (l1)



a= 0
b =1
v = 0
N = 10

for i in range(N):
    a,b = a + b,a
    b = a
    a = v
    print (v)



print (v)