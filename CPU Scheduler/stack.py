from node import Node 

class Stack:
    def __init__(self):
        self.top = None 
        self.size = 0 

    def is_empty(self):
        return self.top == None
    
    def push(self, entry):
        new_node = Node(entry)
        if not(self.is_empty()):
            new_node.next = self.top 
        self.top = new_node
        self.size += 1
    
    def peek(self):
        return self.top.entry
    
    def pop(self):
        if not(self.is_empty()):
            result = self.top.entry
            self.top = self.top.next
            self.size -= 1
            return result
