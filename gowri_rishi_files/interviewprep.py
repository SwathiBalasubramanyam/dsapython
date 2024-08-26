
s = [7,1,2,39,3,7,4]

mn = float("inf")
cprof = mprof = 0
for stock in s:
    mn = min(stock,mn)
    cprof = stock - mn
    mprof = max(cprof,mprof)


print (mprof)


s = [-2,1,-3,4,-1,2,1,-5,4]

csum = msum = s[0]

for num in s[1:]:
    csum = max(num,csum+ num)
    msum = max(csum,msum)

print (msum)


s = [7,6,4,3,1]

profit = 0

for i in range(len(s)-1):

    if s[i] < s[i+1]:
        profit += s[i+1] -s[i]

print (profit)


s= "[]{}{}{}{{}}[[[]]]()"

m = { "}":"{", "]":"[", ")":"(" }

out = []
for bracket in s:   
    if bracket in m.values():
        out.append(bracket)
    else:
        if out and out[-1] == m.get(bracket):
            out.pop()
        else:
            print ("error")

if not out:
    print ("success")



class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def levelorder(root):

    s =[root]
    
    res = []

    while s:
        level = []
        for i in range(len(s)):
            temp = s.pop(0)

            level.append(temp.data)
            if temp.left:
                s.append(temp.left)
            if temp.right:
                s.append(temp.right)

        res.append(level)
    print (res)
        

def verticalorder(node,dist,d):


    if dist in d:
        d[dist].append(node.data)
    else:
        d[dist] = []
        d[dist].append(node.data)
    
    if node.left:
        verticalorder(node.left,dist-1,d)

    if node.right:
        verticalorder(node.right,dist+1,d)

    return d
    

def getverticalpath(node,path,res):

    if node is None:
        return []

    if node.left is None and node.right is None:
        res.append(path+str(node.data))

    if node.left:
        getverticalpath(node.left,path+str(node.data)+"-->" , res)

    if node.right:
        getverticalpath(node.right,path+str(node.data)+"-->" , res)

    return res

def hassum(node,csum,tsum,res):

    csum += node.data
    
    if node.left is None and node.right is None:
        if csum == tsum:           
            res = True            
    
    if not res and node.left:
        hassum(node.left,csum,tsum,res)

    if not res and node.right:
        hassum(node.right,csum,tsum,res)

    return res

    
def maxdepth(node):

    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    else:
        return 1 + max(maxdepth(node.left),maxdepth(node.right))
    

    
d = {}

for i in range(5):
    d[i] = i*i

import pdb;pdb.set_trace()
d= sorted(d.items() ,key = lambda x:x[1])










if __name__ == '__main__':

    """ 
    Construct below tree
              1
            /   \
           /     \
          2       3
                /   \
               /     \
              5       6
            /   \
           /     \
          7       8
                /   \
               /     \
              9      10
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.left.right.left = Node(9)
    root.right.left.right.right = Node(10)

    levelorder(root)
    d = {}
    dist = 0
    print (verticalorder(root,dist,d))
    print (getverticalpath(root,'',[]))
    res = False
    print (hassum(root,0,10,res))
    print (maxdepth(root))


