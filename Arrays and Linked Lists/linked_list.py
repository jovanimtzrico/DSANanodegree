class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list_nodes(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    current = None
    for value in input_list:
        if head is None:
            head = Node(value)
            current = head
        else:
            current.next = Node(value)
            current = current.next
    
    return head



class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        
        # TODO: Write function to turn Linked List into Python List
        list_nodes = []
        current_node = self.head
        while current_node:
            list_nodes.append(current_node.value)
            current_node = current_node.next
        return list_nodes


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
