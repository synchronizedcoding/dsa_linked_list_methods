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
        current_node = self.head #checks if current node is the head
        if not current_node:
            print("List is empty.") #if empty return none
            return
        print("Linked List:", end=" ")
        while current_node: #checks through the linked list
            print(current_node.get_data(), end=" -> ")
            current_node = current_node.get_next()
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

    def remove(self, d): #remove method
        current_node = self.head #starts at the head node, 
        prev_node = None
        while current_node: #loops through the linked list till current_node shows as None
            if current_node.get_data() == d: #checks if the value to be removed matches
                if prev_node:
                    prev_node.set_next(current_node.get_next()) #if not match, skip to the next node
                else:
                    self.head = current_node.get_next() # if matches the user input, remove the node and points the current to the next
                self.size -= 1 #decrement the size by 1 
                return True
            else:
                prev_node = current_node # the prev_node because current_node and the current_node moves to the next
                current_node = current_node.get_next()
        return False #if match is not found, returns false