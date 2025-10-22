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

    def display(self):
        this_node = self.head #checks if current node is the head
        if not this_node:
            print("List is empty.") #if empty return none
            return
        print("Linked List:", end=" ")
        while this_node: #checks through the linked list
            print(this_node.get_data(), end=" -> ")
            this_node = this_node.get_next()
        print("None") #prints None at the very end of the linked list after the last node

    def find(self, d):
        first_node = self.head #points the head to the first node of the linked list
        index = 0 #tracks the position of the node
        while first_node: #loops till the next node is null
            if first_node.get_data() == d: #returns the node user is looking for
                return index
            else:
                first_node = first_node.get_next() #moves through the next node if not what is looking for
                index += 1