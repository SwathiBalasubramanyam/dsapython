a = [8,1,2,2,3]

sa = sorted(a)
d ={}
for i,v in enumerate(sa):
    if v not in d:
        d[v] = i

out = []
for num in a:
    out.append(d[num])

print (out)

n = 234
s= 0
p = 1

while n :
    d = n %10
    
    p *= d
    s += d
    n = n //10

l = [4,2,5,7]









        






