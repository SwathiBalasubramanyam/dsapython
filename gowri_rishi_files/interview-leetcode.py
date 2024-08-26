# arr = [17,18,5,4,6,1]

# mx = -1

# for i in range(len(arr)-1,-1,-1):
#     cval    =   arr[i]
#     arr[i]  =   mx
#     mx      =   max(cval,mx)

# print (arr)

# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


# s = "Let's take LeetCode contest"
# s =s.split()
# o = []]
# for word in s:
#     o += word[::-1] + ' '

# print (o)

# ip = [4,2,5,7]
# out = [0]* len(ip)

# i = 0
# j = 1
# for num in ip:
#     if num % 2 == 0:
#         out[i] = num
#         i += 2
#     else:
#         out[j] = num
#         j += 2

# print (out)

# s = "abbaca"
# stack = []

# for alpha in s:
#     if stack and stack[-1] == alpha:
#         stack.pop()
    
#     else:
#         stack.append(alpha)

# print (''.join(stack))

# arr = [1,2,34,3,4,5,7,23,12]

# c = 0

# for num in arr:
#     if num % 2 != 0:
#         c += 1
#     else:
#         c =0

# arr.remove(2)
# print (arr)


# def two_sum():
#     nums = [2,7,11,15] 
#     target = 9


#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             return [buff_dict[nums[i]], i]
#         else:
#             buff_dict[target - nums[i]] = i

# two_sum()



# nums = [3,2,4]
# target = 6


# d = {}

# for i in range(len(nums)):
#     if nums[i] in d:
#         print (i,d[nums[i]])
#         break
#     else:
#         diff = target-nums[i]
#         d[diff] = i

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# csum = msum = nums[0]

# for num in nums[1:]:
#     csum = max(num,csum+num)
#     msum = max(csum,msum)

# print (msum)

nums = [2,1,-3,4,-1,2,1,-5,4]


print (nums.count(2))

print (nums.insert(20,400))

print (nums)
d ={}
for i in range(5):
    d[i] = i

print (d)

print (d.get(2,"two"))
print (d)


with open("inputfiles/text.txt",'r') as r , open("new" , 'a+') as K:

    out = r.read().splitlines()
    d ={}
    tc = 0
    cc = 0
    word = ''

    for line in out:
        word = line.split()
        for w in word:
            #import pdb;pdb.set_trace()
            d[w] = d.get(w,0) + 1
            if d[w] > tc:
                word = w
                tc = d[w]

    K.write(str(tc))
