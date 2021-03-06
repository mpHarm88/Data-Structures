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
   - The linked list is a class instance and the array is a data type.
"""
import sys
sys.path.insert(1, "/Users/mph/Lambda/cspt-9/Data-Structures/singly_linked")

from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
        
#         if len(self.storage) == 0:
#             return None
#         else:  
#             data = self.storage[-1]
#             del self.storage[-1]
#             return data

# --------- Using Node & Linked List Storage ------------

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
    
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
    
    def pop(self):

        if self.size == 0:
            return None

        else:
            data = self.storage.head.value
            self.storage.remove_head()
            self.size -= 1
            return data

        

