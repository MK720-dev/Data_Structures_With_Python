from node import Node 

class LinkedQueue():

    def __init__(self):
        self._front = None 
        self._rear = None
        self._size = 0
    
    def is_empty(self):
        return self._front == None
    
    def enqueue(self, entry):
        temp = Node(entry)
        if self._front == None:
            self._front = self._rear = temp
            self._size += 1 
            return 
        self._rear.next = temp
        self._rear = temp 
        self._size += 1 

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError
        temp = self._front
        removed = self._front.entry
        self._front = temp.next 
        self._size -= 1
        if self._front == None:
            self._rear == None
        return removed 

    def peek_front(self):
        return self._front.entry
    
    def get_size(self):
        return self._size
    
    def __str__(self):
        temp = self._front
        self.dequeue()
        return str(temp.entry)
    

    

