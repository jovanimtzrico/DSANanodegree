# Build a queue using a linked list
# By now, you may be noticing a pattern. Earlier, we had you implement a stack using an array and a linked list. Here, we're doing the same thing with queues: In the previous notebook, you implemented a queue using an array, and in this notebook we'll implement one using a linked list.

# It's good to try implementing the same data structures in multiple ways. This helps you to better understand the abstract concepts behind the data structure, separate from the details of their implementation—and it also helps you develop a habit of comparing pros and cons of different implementations.

# With both stack and queues, we saw that trying to use arrays introduced some concerns regarding the time complexity, particularly when the initial array size isn't large enough and we need to expand the array in order to add more items.

# With our stack implementation, we saw that linked lists provided a way around this issue—and exactly the same thing is true with queues.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    # Add the dequeue method
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")

                