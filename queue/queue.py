import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?    A list appends and pops in linear time while a linked list can do it at constant time
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

         You would need 2 stacks 
         example code line 52-73
 
"""


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:

#             return self.storage.pop(0)

class Queue(LinkedList):
    def enqueue(self, value):
        self.add_to_tail(value)

    def dequeue(self):
        return self.remove_head()



# Stretch
class Queue_with_Stacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

# the enqueue function should add elements to teh enqueue stack when called
    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        # should check if the dequeue stack is empty
        if not bool(self.dequeue_stack):
            # check if there is a value in enqueue stack
            if bool(self.enqueue_stack):
                # check if only one item is in the enqueue stack, if so return it
                if len(self.enqueue_stack) == 1:
                    return self.enqueue_stack.pop()
                # loop through all items in the enqueue stack and push them to the dequeue stack, this should reverse the order
                while len(self.enqueue_stack):
                    self.dequeue_stack.append(self.enqueue_stack.pop())
        # return the last item in the dequeue stack, which should be the older item in the  queue
        return self.dequeue_stack.pop()


my_stack_queue = Queue_with_Stacks()
my_stack_queue.enqueue(1)
my_stack_queue.enqueue(2)
my_stack_queue.enqueue(3)
my_stack_queue.enqueue(4)
my_stack_queue.enqueue(5)
print(my_stack_queue.dequeue())
print(my_stack_queue.dequeue())
print(my_stack_queue.dequeue())
print(my_stack_queue.dequeue())
print(my_stack_queue.dequeue())
