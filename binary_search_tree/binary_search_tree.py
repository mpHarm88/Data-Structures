"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        cur_node = self

        while cur_node.value != target:
            if target > cur_node.value:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

            return True if cur_node.value == target else False

    # Return the maximum value found in the tree
    def get_max(self):
        
        cur_node = self

        while cur_node.right is not None:
            cur_node = cur_node.right
        
        return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)  
            if self.right:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        
        queue = []
        queue.append(self)

        while len(queue) > 0:
            val = queue.pop(0)
            print(val.value)
            if val.left:
                queue.append(val.left)
            if val.right:
                queue.append(val.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack
        stack = []

        # push some intial value(s) onto the stack
        stack.append(self)
        while len(stack) > 0:
            # pop Node off top of stack to traverse its L & R children
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
