# Problem Statement
# Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

# Example:

# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    current_node = head
    odd_node = None
    if current_node.data % 2 != 0:
        odd_node = current_node
    
    previus_node = current_node
    current_node = current_node.next
    while current_node:
        if current_node.data % 2 != 0:
            if odd_node is None:
                odd_node = current_node
            else:
                temp_node = current_node.next
                previus_node.next = current_node.next
                current_node.next = odd_node.next
                odd_node.next = current_node
                odd_node = odd_node.next
                current_node = odd_node

        previus_node =  current_node    
        current_node = current_node.next
    
    return head

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")

#Test 1
arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

#Test 2
arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)


#Test 3
arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

