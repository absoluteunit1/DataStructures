class LinkedList:

    class Node:
        def __init__(self, data=None, nextNode=None):
            self.data = data
            self.next = nextNode

    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        result = ""
        if not self.is_empty():
            while self.head:
                if self.head.next == None:
                    result += self.head.data
                else:
                    result += f"{self.head.data} -> "
                self.head = self.head.next
            return result
        return "Stack is empty"

    def is_empty(self):
        return self.length == 0
    
    def push(self, data):
        self.head = self.Node(data, self.head)
        self.length += 1

    def top(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Stack is empty")

    def pop(self):
        if not self.is_empty():
            result = self.head.data
            self.head = self.head.next
            self.length -= 1
            return result
        else:
            print("Stack is empty")


