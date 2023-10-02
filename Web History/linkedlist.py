from node import Node

class LinkedList():
    def __init__(self):
        self._front = None
        self._length = 0 

    def insert(self, index, entry):
        if index < 0 or index > self._length:
            raise IndexError
        else:
            if index == 0:
                new_node = Node(entry)
                new_node.next = self._front
                self._front = new_node
                self._length += 1 
            else:
                new_node = Node(entry)
                previous = self._front 
                for i in range(index-1):
                    previous = previous.next
                target = previous.next 
                previous.next = new_node
                new_node.next = target
                self._length += 1 
    
    def remove(self, index):
        if index < 0 or index > self._length:
            raise IndexError
        else:
            if self._front is None:
                return
            position = 0
            current = self._front
            while current.next and position < index:
                previous = current
                current = current.next
                position += 1
            if position < index:
                return
            elif position == 0:
                removed_data = self._front.entry
                self._front = self._front.next
                self._length -= 1
                return removed_data
            else:
                removed_data = previous.next.entry
                previous.next = current.next
                current = None #Optional statement
                self._length -= 1
                return removed_data
           
    def length(self):
        return self._length
    
    def get_entry(self, index):
        if index < 0 or index > self._length:
            raise IndexError
        else:
            if self._front:
                if index == 0:
                    return self._front.entry
                else:
                    previous = self._front
                    for i in range(index-1):
                        previous = previous.next 
                    target = previous.next 
                    return target.entry
            else:
                return None
         
    def set_entry(self, index, entry):
        if index < 0 or index > self._length:
            raise IndexError
        else:
            if index == 0:
                if self._front != None:
                    self._front.entry = entry
                else:
                    self._front = Node(entry)
            else:
                previous = self._front
                for i in range(index-1):
                    previous = previous.next 
                target = previous.next
                target.entry = entry 
        
    def clear(self):
        for i in range(self._length):
            self._front = self._front.next
            self._length -= 1

        


