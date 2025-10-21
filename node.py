class Node: #defines class node for new nodes
    def init(self, d, n= None): #intializes data and the address
        self.data = d
        self.next = n

    def get_next(self): #get the next node method
        return self.next

    def set_next(self, n): #set the pointer to the next node
        self.next = n

    def get_data(self): #returns the node's value
        return self.data

    def set_data(self, d): #changes the node's data
        self.data = d