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
        while cur_node.next != None:
            cur_node = cur_node.next
            print(cur_node.data, end="")

list1 = LinkedList()
list1.append("Hello")
list1.append(" ")
list1.append("World!")
list1.append("\n")
list1.display()