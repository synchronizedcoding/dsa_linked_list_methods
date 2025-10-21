from node import Node

class LinkedList:
    def init(self, n = None):
        self.head = n
        self.size = 0

    def get_list_size(self): #returns the size of the linked list
        return self.size

    def add_new_node(self, d): #adds a new node in linked list
        new_node = Node(d, self.head)
        self.head = new_node
        self.size += 1