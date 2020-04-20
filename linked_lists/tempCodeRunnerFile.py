cur_node = self.head
        cur_index = 0
        previous_node_a = self.head
        previous_node_b = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if index_a == cur_index: