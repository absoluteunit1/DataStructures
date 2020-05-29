# Regular queue
# Uses circular arrays
# Allows for removal from the front and insertion at the back


class Empty(Exception):
    pass

# FIFO Queue implementation using a Python list as storage

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        # returns the number of elements in the queue
        return self._size
    
    def is_empty(self):
        # returns true if the queue is empty
        return self._size == 0

    def first(self):
        # returns (doesn't remove) the first element in the queue
        # Raises exception if the queue is empty
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        # Removes and return the first element of the queue
        # Raises exception if queue is empty
        if self.is_empty():
            raise Empty('Queue is empty')
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return result

    def enqueue(self, e):
        # Adds an element to the back of queue
        if self._size == len(self._data):
            self._resize(2*len(self.data)) # doubles the array size if we are at the cap of the current array
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def resize(self, cap):
        old = self._data
        self. data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self. front = 0
        