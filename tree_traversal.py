class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    
class Tree:

    def insert(self, rnode, nnode):
        if not rnode:
            return nnode

        if rnode.val = nnode.val:
            return 

        if nnode.val > rnode.val:
            rnode.right = self.insert(rnode.right, nnode)
        else:
            rnode.left = self.insert(current_node.left, nnode)



