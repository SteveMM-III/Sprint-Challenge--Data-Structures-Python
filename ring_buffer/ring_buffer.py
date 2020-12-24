class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.que  = []
        self.curr = 0

    def append(self, item):
        # if not at capacity
        if len( self.que ) < self.capacity:
            self.que.append( item )
        # capacity reached
        else:
            self.que[ self.curr ] = item
        
        # increase current
        self.curr += 1

        # verify current not out of bounds
        if self.curr is self.capacity:
            self.curr = 0

    def get(self):
        return self.que
