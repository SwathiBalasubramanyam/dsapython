def twosum():
    nums = [0,8,1,7,2]
    target = 9
    d = {}
    l = []
    for i,num in enumerate(nums):
        if num in d:
            l.append((i,d[num]))
        else:
            diff = target - num
            d[diff] = i
    return l
print (twosum())



def par1(d,s):

    op = []
    for ch in s:
        if ch in d.keys():
            if op and op[-1] == d[ch]:
                op.pop()
            else:
                return False
        else:
            op.append(ch)
    return op == []

d = {']':'[',')':'(','}':'{'}

print (par1(d,'{}{{}}{}'))

s = "abbaca"

op = []

for ch in s:
    if op and op[-1] == ch:
        op.pop()
    else:
        op.append(ch)

print (''.join(op))



ip = [1,2,3,4]
op = [0] * len(ip)

prev = 0

for i,v in enumerate((ip)):
    op[i] = v + prev
    prev = op[i]

print (op)



nums = [8,1,2,2,3]
snums = sorted(nums)
d = {}
for i,num in enumerate(snums):
    if num not in d:
        d[num] = i




print ([d[num] for num in nums])



s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
op = [0]*len(indices)

for i,v in enumerate(indices):

    op[i] = s[v]

print (op)


def sumprod():
    n = 1
    s = 0
    p = 1
    if n != 0:
        while n:
            d = n % 10
            s += d
            p *= d
            n = n //10
        return (s,p)
    else:
        return (s,0)


print (sumprod())



s = "RLLLLRRRLR"
c = 0
tc = 0
for ch in s:
    if ch == 'R':
        c += 1
    elif ch == 'L':
        c -= 1
    if c == 0:
        tc += 1

print (tc)


n = 4

print (list(range(1-n,n,2)))


s = 'aaabbccaabbcc'
c = 1
o = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        o += s[i] + str(c)
        c = 1
o += s[i] + str(c)

print (o)


s = 'abs&&()()lll'
import re
m =re.split('[&()]',s)
print (m)


s = 'ahdhd-)()*BNBNfg'

import re
m=re.split('[-)(*)]',s)
print (m)


s = "a-bC_dEf+ghIj"
s = list(s)
i = 0
j = len(s)-1

while i < j:
    if not s[i].isalpha():
        i += 1
    elif not s[j].isalpha():
        j -= 1
    else:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1


print (s)

strs = ["eat","tea","tan","ate","nat","bat"]
d ={}
for s in strs:
    k = tuple(sorted(s))
    d[k] = d.get(k,[]) + [s]

print ([v for k,v in d.items()])


nums = [-2,1,-3,4,-1,2,1,-5,4]

csum = msum = nums[0]

for num in nums[1:]:
    csum = max(csum+num,num)
    msum = max(csum,msum)



def twosum(arr,target):

    d ={}
    for i,v in enumerate(arr):
        if v in d:
            return (i,d[v])
        else:
            diff = target - v
            d[diff] = i

print (twosum([2,3,6,7,15],9))



def max2num(arr):
    m1 = m2 = m3 = float('-inf')

    for num in arr:
        if num > m1:
            m2 = m1
            m1 = num
        elif num >m2:
            m2 =num
    return (m1,m2)

print (max2num([2,3,6,7,15]))



def check_parent(parenth):

    d = {')':'(',']':'[','}':'{'}
    o = []
    for s in parenth:
        if s in d.keys():
            if o and o[-1] == d[s]:
                o.pop()
            else:
                return False
        else:
            o.append(s)
    
    return o == []

print (check_parent('{}{}()()'))


def helper(s,l,r):
    while l >=0 and r < len(s) and s[l]==s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

s = 'abba'
maxv = ''

for i in range(len(s)):
    odd = helper(s,i,i)
    even = helper(s,i,i+1)
    maxv = max(odd,even,maxv,key=len)

print (maxv)

s = "abbaca"
o = []
for c in s:
    if o and o[-1] == c:
        o.pop()
    else:
        o.append(c)
print (o)


ip = [1,2,3,4]
op = [0]*len(ip)
prev =0

for i,num in enumerate(ip):
    op[i] = prev + num
    prev = op[i]

print (op)

nums = [8,1,2,2,3]

snums = sorted(nums)

d ={}

for i,v in enumerate(snums):
    if v not in d:
        d[v] = i

print ([d[v] for v in nums ])

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
o =['']*len(indices)

for i,v in enumerate(indices):
    o[v] = s[i]

print (o)


n = 234

p = 1
s = 0


while n:
    d = n % 10
    p *= d
    s += d
    n = n //10

print (p,s)


s = "RLLLLRRRLR"

c = 0
tc = 0

for ch in s:
    if ch == 'R':
        c += 1
    elif ch == 'L':
        c -= 1

    if c ==0:
        tc += 1

print (tc)

nums = [12,345,20,6,7896]

tc = 0
for num in nums:
    nc = 0
    while num:
        num = num //10
        nc += 1

    if nc % 2 == 0:
        tc += 1

print (tc)


s = 'aaabbccaabbcc'
c = 1
o = ''

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c += 1
    else:
        o += s[i] + str(c)
        c = 1
o += s[i] + str(c)

print (o)

o1 = ''
for c in o:
    if c.isalpha():
        cc = c
    else:
        o1 += cc * int(c)
print (s)
print (o1)


s ='asd89*(!!<>kk<>,.dddjdjd,.hdjsk'

import re
s1 = re.split('[!<>,.]',s)
print (s1)


s = "Let's take LeetCode contest"

import re
o = []
s = re.split(' ',s)
print (s)
for w in s:
    o.append(w[::-1])
print (' '.join(o))



s1 = "a-bC_dEf+ghIj"
s =list(s1)
i = 0
j = len(s)-1

while i < j:
    if s[i].isalpha():
        i += 1
    elif s[j].isalpha():
        j -= 1
    else:
        s[i],s[j]=s[j],s[i]
        i += 1
        j -= 1

print (s)


pat = '^(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])\.(25[0-4]|2[0-4][0-9]|[10]?[0-9]?[0-9])$'

ip = '1.1.1.1000'

import re
m = re.search(pat,ip)
print (m)

s = "anagram" 
t = "nagaram"

d1 ={}
d2 ={}

for ch in s:
    d1[ch] = d1.get(ch,0)+1
for ch in t:
    d2[ch] = d2.get(ch,0)+1

print  (d1==d2)


strs = ["eat","tea","tan","ate","nat","bat"]
d ={}
for w in strs:
    key = tuple(sorted(w))
    d[key] = d.get(key,[]) + [w]
print (d)


with open('abc.txt','r') as f:
    contects= json.load(f)

with open('o1.txt','r') as f:
    c =f.read().splitlines()
print (c)

nums = [-2,1,-3,4,-1,2,1,-5,4]
msum = csum = nums[0]

for num in nums[1:]:
    csum = max(csum+num,num)
    msum = max(csum,msum)


prices = [7,1,5,3,6,4]
minprice = float('inf')
maxprofit = 0

for num in prices:
    minprice = min(minprice,num)
    cprofit = num - minprice
    maxp = max(maxp,cprofit)
print (maxp)