class Node:

    def __init__ (self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data  

class LinkedList:

    # Initializes the list; with head of the list that contains no data and its next variable points to None
    def __init__(self):
        self.head = Node()

    # Adds a node to the beginning of the list
    def push(self, data):
        # Initialize the new node
        new_node = Node(data)
        # Create a buffer that points to the node that the head is currently pointing to
        temp_node = self.head.next
        # Make the head of the list point to the new_node
        self.head.next = new_node
        # And make the new_node point to the temp_node (what the head was pointing to originally)
        new_node.next = temp_node

    # Adds a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    # Returns the length of the list
    def length(self):
        cur_node = self.head
        count = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            count += 1
        return count
    
    # Prints the list
    def display(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node, end="->") if cur_node.next != None else print(cur_node)

    # Returns a the data of the node of which the index was specified
    def get(self, index):
        try:
            cur_node = self.head
            cur_index = 0
            while True:
                cur_node = cur_node.next
                if cur_index == index:
                    return cur_node.data
                cur_index += 1
        except AttributeError as error:
            print(f"The get() function call encountered the following error: {error}")
            return None
    
    # Returns the data of the last node in the listvor the data at the index of the specified node and removes that node from the list
    def pop(self, index=None):
        cur_node = self.head
        previous_node = self.head

        # If the index is not specified, remove the last item from the list
        if index == None:
            while cur_node.next != None:
                previous_node = cur_node
                cur_node = cur_node.next
            data = cur_node.data
            previous_node.next = None
            return data
        
        # If the index is specified, remove that node from the list
        else:
            try:
                cur_index = 0
                while True:
                    # Previous node is the node prior to the node whose index was specified. 
                    previous_node = cur_node
                    cur_node = cur_node.next
                    if cur_index == index:
                        data = cur_node.data
                        previous_node.next = cur_node.next  # If the index matches, we set the previous_node's pointer to the node the current node is pointing to.
                        return data
                    cur_index += 1
            except AttributeError as error:
                print(f"The pop({index}) function call experienced the following error: {error}")
                return None
    



    
names = LinkedList()
names.push('Anton')
names.push('Vlad')
names.push('John')
names.append("Nick")
names.display()
names.pop(2)
names.display()
names.pop(5)
names.pop(0)
names.display()
