from node import Node 

class LinkedQueue():
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.front == None
    
    def enqueue(self, entry):
        temp = Node(entry)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp 
        self.rear = temp 

    def dequeue(self):
        if self.is_empty():
            return 
        temp = self.front 
        self.front = temp.next 
        if self.is_empty():
            self.rear = None 

    def peek_front(self):
        return self.front.entry


