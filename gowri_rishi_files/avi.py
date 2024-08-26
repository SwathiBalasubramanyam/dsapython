# # l1 = [1,2,3,4]

# # l1 = list(range(0,20,2))
# # print (l1)

# # l2 = list(range(20,40,5))
# # print (l2)

# # l1.extend(l2)

# # print (l1)
# # print (l2)

# # l1.insert(0,1000)
# # print (l1)

# # #print (l1.index(200))

# # l1.remove(1000)
# # print (l1)

# # print (l1.count(1000))

# # l1.reverse()

# # print (l1)
# # del l1[0]

# # print (l1)

# # l1.sort()

# # print (l1)

# ##################################################

# # def twosum():
# #     nums = [2,3,6,7,15]
# #     target = 9
# #     d ={}
# #     out =[]
# #     for i,v in enumerate(nums):
# #         if v in d:
# #             m = (d[v],i)
# #             out.append(m)
# #         else:
# #             diff = target - v
# #             d[diff] = i
# #     return out

# # print (twosum())

# # ##################################################
# # nums = [100,200,100,100,-200]
# # import heapq
# # res = heapq.nlargest(3,nums)
# # print (res)

# # m1 = m2 = m3 = float('-inf')

# # for num in nums:
# #     if num > m1:
# #         m3 = m2
# #         m2 = m1
# #         m1= num
# #     elif num > m2:
# #         m3 = m2
# #         m2 = num
# #     elif num > m3:
# #         m3 = num

# # print (m1,m2,m3)

# # k = set(nums)
# # print (k)

# # for num in k:
# #     print (num)



# # def parnt(s):
# #     out = []
    
# #     for c in s:
# #         if c in d.keys():
# #             if out and out[-1] == d[c]:
# #                 out.pop()
# #             else:
# #                 return False
# #         else:
# #             out.append(c)
    
# #     return out == []  

# # d = { ']':'[',
# #       ')':'(',
# #       '}':'{' }

# # slist =['{}','{{}}{}[]','{}{}{']
# # for s in slist:
# #     print (parnt(s))


def helper(s,l,r):

    while l >= 0 and r < len(s) and s[l] ==s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

s = 'gadadag'
res = ''
for i in range(len(s)):
    odd = helper(s,i,i)
    even = helper(s,i,i+1)
    res = max(res,odd,even,key=len)
print (res)


# s = "abbaca"

# o = []

# for c in s:
#     if o and o[-1] == c:
#         o.pop()
#     else:
#         o.append(c)
# print (o)


# ip = [1,2,3,4]
# op = [0]*len(ip)
# prev = 0
# for i,num in enumerate(ip):
#     op[i] = prev + num
#     prev = op[i] 

# print (op)

# #How Many Numbers Are Smaller Than the Current Number
# nums = [8,1,2,2,3]
# snums = sorted(nums)
# d = {}
# for i,num in enumerate(snums):
#     if num not in d:
#         d[num] = i
# #[1:0,2:1,2:2]

# print ([d[v] for v in nums])

# #Shuffle String
# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]

# o =[0]*len(s)

# for i,v in enumerate(indices):
#     o[v] = s[i]
# print (o)

# #Subtract the Product and Sum of Digits of an Integer

# n = 234

# p = 1
# s = 0

# while n:
#     d = n % 10
#     p *= d
#     s += d
#     n = n //10
# print (p,s)

# #insert num
# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
# o = []

# for i,v in enumerate(nums):
#     o.insert(index[i],v)

# print (o)


# s = "RLLLLRRRLR"
# count = 0
# tc = 0
# for c in s:
#     if c == 'R':
#         count += 1
#     elif c == 'L':
#         count -= 1
#     if count == 0:
#         tc += 1
# print (tc)

# #even numbers

# nums = [12,345,2,6,7896]
# c = 0
# for num in nums:
#     nc = 0
#     while num:
#         num = num // 10
#         nc += 1
#     if nc % 2 == 0:
#         c +=1 

# print (c)

# #max product

# m1 = m2 = float('-inf')

# nums = [3,4,5,2]

# for num in nums:
#     if num > m1:
#         m2 = m1
#         m1 = num
#     elif num > m2:
#         m2 = num

# print (m1,m2)

# #odd count
# n = 4

# if n % 2 == 0:
#     print ('a'*(n-1)+'b')
# else:
#     print ('a'*n)



# #adding upot zeroes
# n = 5
# print (list(range(1-n,n,2)))


# s = 'aaabbccaabbcc'
# o = ''
# c =1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         o +=  s[i] + str(c)
#         c =1
# o +=  s[i] + str(c)
# print (o)

# oo = ''
# for c in o:
#     if c.isalpha():
#         cc = c
#     else:
#         oo += cc*int(c)
# print (oo)

# print (set(oo))

# #(re.split('[/.]', UBUNTU_TENANT_TEMPLATE))

# oo = ''
# i = 0
# while i < len(o):
#     oo += o[i]*int(o[i+1])
#     i += 2
# print (oo)


# s = 'a-)()*BNBNfg'

# import re
# m=re.split('[-)(*)]',s)
# print (m)

# #Input: 
# s = "Let's take LeetCode contest"
# #Output: "s'teL ekat edoCteeL tsetnoc"

# slist = s.split()
# o = []
# for w in slist:
#     o.append(w[::-1])

# print (' '.join(o))


# s = "abcdef"
# k = 2

# flag = False
# o =''
# i = 0

# while i < len(s)-1:
#     flag  = not flag
#     c1 = s[i]
#     c2 = s[i+1]
#     if flag:
#         o += c1 + c2
#     else:
#         o += c2 + c1
#     i += 2

# if not len(s) % 2 == 0:
#     o += s[-1]

# print (o)

# arr = [1,2,34,3,4,5,7,23,12]
# c = 0
# out = []
# l =[]
# for num in arr:
#     if num % 2 != 0:
#         c += 1
#         l.append(num)
#     else:
#         c = 0
#         l = []
#     if c == 3:
#         print ('found')
#         out.append(l)
# print (out)

# d ={} 
# maxv = 0 
# arr = [2,2,3,3,3,4]
# for num in arr:
#     d[num] = d.get(num,0)+1
# print (d)
# for k,v in d.items():
#     if k == v:
#         maxv = max(maxv,k)
# print (maxv)



# s ='abbbb'
# c = 1
# mx = 1

# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         c += 1
#     else:
#         c =1
#     mx = max(mx,c)

# print (mx)

# s = "a-bC_dEf+ghIj"
# s=list(s)
# i = 0
# j = len(s)-1

# while i < j:
#     if s[i].isalpha():
#         i += 1
#     elif s[j].isalpha():
#         j -= 1
#     else:
#         s[i],s[j]=s[j],s[i]
#         i += 1
#         j -= 1
# print (''.join(s))



# num =38
# digit_sum = 0

# while num:
#     digit =  num %10
#     digit_sum += digit
#     num = num //10

# print (digit_sum)


# nums = [1,1,2,2,3,4]
# incr = False
# decr = False

# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         incr = True
#     if nums[i] > nums[i+1]:
#         decr = True
#     if incr and decr:
#         print ('Fail')

# p = 0
# prices = [7,1,5,3,6,4]
# for i in range(len(prices)-1):
#     if prices[i] < prices[i+1]:
#         p = p + prices[i+1] - prices[i]

# print (p)


# prices = [7,1,5,3,6,4]

# p1 = sorted(prices)
# d ={}
# for i,v in enumerate(p1):
#     if v not in d:
#         d[v] = i

# print ([d[x] for x in prices])



# pat = '^(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])$'


# ip = '10.40.50.20'

# import re
# m = re.search(pat,ip)
# if m:
#     print (m)
#     print (m.group())
#     print (m.group(2))
    
    

# s ='abcd'
# print (len('abc'))
# print ((s[0]))


# s1 = list(s)
# print (s1)


# strs = ["eat","tea","tan","ate","nat","bat"]
# d ={}
# for w in strs:
#     k = tuple(sorted(w))
#     d[k] = d.get(k,[])+[w]
# print (d)

# s = "anagram" 
# t = "nagaram"

# d1 ={}
# d2 ={}
# for c in s:
#     d1[c] = d1.get(c,0)+1

# for c in t:
#     d2[c] = d2.get(c,0)+1

# print (d1==d2) 

# import heapq

# prices = [7,1,5,3,6,4]
# print (heapq.nsmallest(3, prices))



# l1 = list(range(-10,0))

# print (l1)

# nlargest = heapq.nlargest(3,l1)
# smallest = heapq.nsmallest(2, l1)


# res = max((nlargest[-1]* nlargest[-2] * nlargest[-3]),(smallest[0]*smallest[1]*nlargest[-1]))
# print (res)


# def check_parentheses():

#     op = []
#     for c in s1:
#         if c in paranthese_map.keys():
#             if op and op[-1] == paranthese_map[c]:
#                 op.pop()
#             else:
#                 return False    
#         else:
#             op.append(c)
    
#     return op == []

# paranthese_map = { ']':'[','}':'{',')':'('}

# ip = ['((((()()[[]]{}{}{{}}))))','{}{}}','']


# for s1 in ip:
#     if s1:
#         print (check_parentheses())
#     else:
#         print ('string is empty')


# import json
# with open('test1.json','r') as file_handle:
#     content = json.load(file_handle)
# print (content)



# import json
# with open('test1.json','r') as f:
#     contents = json.load(f)

# print (contents)

# with open('o1.txt','a') as f_handle:
#     out = f_handle.write("XVZ")
# print (out)


# pattern = '^(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])$'

# import re

# # m = re.search(pattern,'300.200.1.1')
# # print (m.group())


# print (prices)

# prices.sort()
# print (prices)


# nums = [-2,1,-3,4,-1,2,1,-5,4]

# csum = msum = nums[0]

# for num in nums[1:]:
#     csum = max(csum+num,num)
#     msum = max(csum,msum)

# print (msum)


# prices = [7,1,5,3,6,4]
# minprice = float('inf')
# maxprofit =0

# for price in prices:
#     minprice = min(price,minprice)
#     profit = price-minprice
#     maxprofit = max(maxprofit,profit)

# print ((maxprofit))



# startip = '10.1.1.1,90/10+20'
# mask = '255.255.0.0'

# import re
# iplist = re.split('[./+,]',startip)
# print (iplist)


# iplist = startip.split('.')
# i,j =0,0
# c = 0

# prefix = (iplist[0]) +'.' + (iplist[1])
# while i < 256:
#     while j < 256:
#         print ('{}.{}.{}'.format(prefix,str(i),str(j)))
#         c += 1
#         j += 1
#     i += 1
#     j = 0
# print (c)




# mgmt_gw = '10.1.0.0/16'
# import ipaddress
# network = ipaddress.IPv4Network(mgmt_gw)

# for each in network:
#     print (each)
# import random
# for i in range(10):
#     print ('.'.join([str(random.randint(0,3)) for _ in range(4)]))



# import ipaddress
# nw = '30.1.1.0/30'
# nw_range = ipaddress.IPv4Network(nw)

# for ip in nw_range:
#     print (ip)



# def fibo(list1):
    
#     if len(list1) < 10:
#         list1.append(list1[-1] + list1[-2])
#         fibo(list1)
#     return list1

# print (fibo([0,1]))
