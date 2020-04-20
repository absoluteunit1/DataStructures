# A node cannot have more than two children
# Strict/Proper binary tree: when each node has either 2 or 0 children nodes.
# Complete Binary Tree: All levels except the last are completely filled and all nodes are as left as possbile

# Max number of trees possbile at a level i = 2**i

# Another Lesson:

# Full Tree: All leaf nodes are at the same level
# Complete: All levels but the last are filled. The last level, the leaf nodes are all left most 
# Height Balanced Trees: todo

class Node:

    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
    
class binary_search_tree:
    
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):

        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child=Node(value)
            else:
                self._insert(value, cur_node.right_child)

        else:
            print("Value already in tree!")

    def print