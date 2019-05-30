class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_node = list1.head
    list2_node = list2.head
    
    while list1_node or list2_node:
        if list1_node is None:
            merged.append(list2_node.value)
            list2_node = list2_node.next
        elif list2_node is None:
            merged.append(list1_node.value)
            list1_node = list1_node.next
        elif list1_node.value <= list2_node.value:
            merged.append(list1_node.value)
            list1_node = list1_node.next
        else:
            merged.append(list2_node.value)
            list2_node = list2_node.next
        
    return merged

class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        return self.do_flatten(self.head)
        pass
    def do_flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self.do_flatten(node.next))


# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

nested_linked_list = NestedLinkedList(Node(linked_list))
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
nested_linked_list.append(second_linked_list)   

presolution = nested_linked_list.flatten()
solution = []
node = presolution.head
print("This will print 1 2 3 4 5")
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    solution.append(node.value)
    node = node.next

assert solution == [1,2,3,4,5]        


# Second Test Scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
print("\nThis will print 1 2 3 4 5")
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
print("\nThis will print 1 3 5")
while node is not None:
    #This will print 1 3 5
    print(node.value)
    node = node.next

