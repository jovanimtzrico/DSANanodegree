# Traverse a tree (breadth first search)
# Think through the algorithm
# We are walking down the tree one level at a time. So we start with apple at the root, and next are banana and cherry, and next is dates.

# 1) start at the root node
# 2) visit the root node's left child (banana), then right child (cherry)
# 3) visit the left and right children of (banana) and (cherry).

# Queue
# Notice that we're waiting until we visit "cherry" before visiting "dates". It's like they're waiting in line. We can use a queue to keep track of the order.

from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# BFS algorithm
def bfs(tree):
    visit_order = list()
    q = Queue()
    node = tree.get_root()
    
    while node:
        visit_order.append(node)
        if node.has_left_child() and node is not visit_order:
            q.enq(node.get_left_child())
        if node.has_right_child() and node is not visit_order:
            q.enq(node.get_right_child())
        node = q.deq()
    return visit_order

# check solution: should be: apple, banana, cherry, dates
print(bfs(tree))




