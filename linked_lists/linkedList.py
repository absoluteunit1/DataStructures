# What is __slots__?


# Single LinkedList Efficiency 

# Access an element: O(n)
# Add/remove element at an iterator position: O(1)
# Add/remove first element: O(1)
# Add last element: O(1)
# Remov last element: O(n)


# Double LinkedList Efficiency 

# Access an element: O(n)
# Add/remove element at an iterator position: O(1)
# Add/remove first element: O(1)
# Add last element: O(1)
# Remov last element: O(1)


# Difference between Arrays and LinkedLists

# Size: Arrays are fixed and their size is declared during declaration whereas liked lists grow and contract. Max size of linked lists depends on heap
# Storage Cap: Arrays storage is static; its location is allocated during compile time. Linked Lists: Dynamic: its node is located during runtime
# Order and Sorting: Data in arrays is stored consequtively (sequentially.). In Linked Lists, data is stored randomly (Does not have to be in order and order can be change. )
# Accessing elements: Arrays allow direct access. LinkedLists allow sequential access; traversing from the first node using pointers. 
# Searching: Arrays allow binary search and linear search. Linked Lists allow linear searching only. 

class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()          # Head node contains no data and is not accessible. It is used as a place holder which will allow us to point to the first node in the list

    def append(self, data):         # Adds a new data point to the end of the list. 
        new_node = Node(data)       # Creates a new node object and initialize the data
        cur = self.head             # A variable that stores the node that we are currently on. 
        while cur.next != None:     # Iterates through the list until the next element is not None (when it is None, we have reached the end of the list)
            cur = cur.next          # Sets the last node in the list to last item node in the list
        cur.next = new_node         # Once we are on the last element, we can set the next node to our new node!

    def length(self):
        count   = 0
        cur     = self.head
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
    
    def display(self):
        cur_node = self.head
        print("START-> ",end="")
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data, end=" ->END\n") if cur_node.next == None else print(cur_node.data, end="-")

    def get(self, index):
        try:
            cur_inx = 0
            cur_node = self.head
            while True:
                cur_node=cur_node.next
                if cur_inx == index:
                    return cur_node.data
                cur_inx += 1
        except AttributeError as error:
            print(f"The get() funcion encountered the following error: {error}")
            return None
    
    def erase(self, index):
        try:
            cur_inx = 0
            cur_node = self.head
            while True:
                last_node = cur_node
                cur_node=cur_node.next
                if cur_inx == index:
                    last_node.next = cur_node.next
                cur_inx += 1
        except AttributeError as error:
            print(f"The get() funcion encountered the following error: {error}")


myList = LinkedList()

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)

myList.display()
myList.erase(2)
myList.display()
myList.erase(0)
myList.display()

