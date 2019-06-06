# Pre-order traversal with recursion
# Use recursion and perform pre_order traversal.

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

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# define post_order traversal
def post_order(tree):
    visit_order = post_order_recursion(tree.get_root())
    print(visit_order)

def post_order_recursion(node):
    if node is None:
        return []
    visit_order = list()
    visit_order.extend(post_order_recursion(node.get_left_child()))
    visit_order.extend(post_order_recursion(node.get_right_child()))
    visit_order.append(node.get_value())
    return visit_order

# check solution: should get: ['dates', 'banana', 'cherry', 'apple']
post_order(tree)

