"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        if self.length == 0:
            self.head = ListNode(value, None, None)
            temp = self.head
            self.tail = temp
            self.head.next = temp
            self.length += 1

        elif self.length == 1:
            temp = self.head
            self.head = ListNode(value, None, temp)
            temp = self.tail
            self.length += 1
        else:
            temp = self.head
            self.head = ListNode(value, None, temp)
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        
        if self.length == 0:
            return None
        
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        else:
            temp = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return temp
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        if self.length == 0:
            self.head = ListNode(value, None, None)
            self.tail = self.head
            self.length += 1

        elif self.length == 1:
            temp = ListNode(value, self.head, None)
            self.head.next = temp
            self.tail = temp
            self.length += 1

        else:
            temp = ListNode(value, self.tail, None)
            self.tail.next = temp
            self.tail = temp
            self.length += 1
            
        
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        
        if self.length == 0:
            return None
        
        elif self.length == 1:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            self.tail.prev = self.tail
            self.tail.next = None
            self.length -= 1
            return value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        if self.length == 2:
            temp = self.head
            self.tail.next = temp
            self.head = self.tail
            self.head.prev = None
            temp.next = None
        
        elif node == self.tail:
            temp = self.tail
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            self.tail = temp.prev
      
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.prev = node
            node.prev = None
            node.next = self.head
            self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        if self.length == 2:
            temp = self.head
            self.head = temp.next
            self.tail = temp

            self.head.prev = None
            self.head.next = self.tail

            self.tail.prev = self.head
            self.tail.next = None
        
        elif node == self.head:
            temp = self.head
            self.head.next = self.head
            self.head.prev = None

            self.tail.next = temp
            temp = self.tail
            self.tail.next = None
      
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 1:
            del node
            self.head = None
            self.tail = None
            self.length -= 1

        elif node == self.tail:
            node.prev = self.tail
            self.tail.next = None
            self.length -= 1
        
        elif node == self.head:
            temp = self.head.next 
            temp.prev = None
            self.head = temp
            self.length -= 1

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        if self.length == 0:
            return None

        max = 0
        temp = self.head
        while temp is not None:
            if temp.value > max:
                max = temp.value
                temp = temp.next
            else:
                temp = temp.next
        
        return max