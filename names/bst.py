class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode( value )
            else:
                self.left.insert( value )
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode( value )
            else:
                self.right.insert( value )

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains( target )
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains( target )

    # Return the maximum value found in the tree
    def get_max(self):
        next_node = self.right

        if next_node:
            curr = next_node.value

            while next_node:
                curr = next_node.value
                next_node = next_node.right
            return curr
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn( self.value )
        if self.left:
            self.left.for_each( fn )
        if self.right:
            self.right.for_each( fn )

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print( self.value )

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        que = Queue()
        que.enqueue( self )

        while len( que ) > 0:
            node = que.dequeue()

            print( node.value )

            if node.left:
                que.enqueue( node.left )
            if node.right:
                que.enqueue( node.right )
            


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push( self )

        while len( stack ) > 0:
            node = stack.pop()

            print( node.value )

            if node.right:
                stack.push( node.right )
            if node.left:
                stack.push( node.left )
