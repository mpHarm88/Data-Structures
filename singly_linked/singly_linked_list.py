class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node 
        self.length += 1
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.set_next(new_node)
        self.tail=new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            return None
        # list with 1 node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # list with +2 Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        pass


    def contains(self, value):

        cur_node = self.head

        while cur_node is not None:
            if cur_node.value == value:
                return True
            else:
                cur_node = cur_node.next_node
        return False

                      
    def get_max(self):
        # iterate through all elements

        cur_node = self.head
        max = 0
        
        if self.length == 0:
            return None
        
        while cur_node is not None:
            if cur_node.value > max:
                max = cur_node.value
            cur_node = cur_node.next_node

        return max

        


        