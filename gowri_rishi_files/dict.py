#d = {}


# for i in range(10):
#     d[i] = i**2

# print (d)

# print (d.get(30))




# # print (d.items())

# # print (d.keys())

# poped = d.popitem()

# import pdb;pdb.set_trace()
# print (poped)
# print (d)


# m = d.update({0:100})

# print (d)

# d = {}

# for i in range(10):
#     d[i]= {}
#     d[i][i] = i+10

#print (d)


# for each,v1 in d.items():
#     import pdb;pdb.set_trace()
#     for k,v in v1.items():
#         print (k,v)

#     for k,v in d: 
#         print (k,v)


#sorted dictionary

#d = {'one':1,'three':3,'five':5,'two':2,'four':4}
# a = sorted(d.items(), key=lambda x: x[0])    
# print(a)

# a = sorted(d.items(),key= lambda x:x[1])
# print (a)

# a = sorted(d.items(),key = lambda x:x[1])
# m ={}
# for k,v in a:
#     m[k] = v
# print (m)

# d = {}
# for i in [10,-4,2,-7,8]:
#     d[i] = i + 10
# print (d)
# for i in sorted(d.values()):
#     print (i)


# # for i in sorted(d.items()):
# #     print (i)

# m = sorted(d.items(),key = lambda x:x[1])
# print (m)

# ip = "tree"


# d = {}

# for alpha in ip:
#     d[alpha] = d.get(alpha,0) + 1


# m = sorted(d.items(),key = lambda x : -x[1])

# print (m)
# out = ''

# for k,v in m:
#     o1 = k * v
#     out += o1

# print (out)



# ip = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2

# d ={}

# for w in ip:
#     d[w] = d.get(w,0) + 1

# print (d)

# m = sorted(d.items() , key=lambda x :-x[1])

# print (m)

# import collections


# def flatten(d, parent_key='', sep='_'):
#     items = []
#     import pdb;pdb.set_trace()
#     for k, v in d.items():
#         new_key = parent_key + sep + k if parent_key else k
#         if isinstance(v, collections.MutableMapping):
#             items.extend(flatten(v, new_key, sep=sep).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)

# ad = {'a': 1,'c': {'a1': 2,'b1': {'x1': 5,'y1' : 10}},'d': [1, 2, 3]}
# print (flatten(ad))



# row = [1,2,3]

# #row=row[::-1]
# row.reverse()

# print (row)


d = {}
key = "abc"
d[key] = d.get(key)
print (d)