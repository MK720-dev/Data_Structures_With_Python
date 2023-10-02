from node import Node 

class Stack():
    
    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, entry):
        temp = self._top
        self._top = Node(entry)
        self._top.next = temp
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError
        removed = self._top.entry
        self._top = self._top.next 
        self._size -= 1
        return removed
    
    def peek(self):
        if not(self.is_empty()):
            return self._top.entry
    


        
