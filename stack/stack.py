
import sys
sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.data = []
#         # self.storage = ?

#     def __len__(self):
#         return len(self.data)

#     def push(self, value):
#         self.data.append(value)

#     def pop(self):
#         if len(self.data):
#             return self.data.pop()


class Stack(LinkedList):
    def push(self, value):
        self.add_to_tail(value)

    def pop(self):
        return self.remove_tail()


my_stack = Stack()
my_stack.push(1)


print(my_stack)
print(f'length is {len(my_stack)}')
