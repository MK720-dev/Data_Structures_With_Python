from node import Node 

class LinkedList():

    def __init__(self):
        self._front = None
        self._length = 0

    def insert(self, index, entry):
        if index < 0 or index > self._length:
            raise IndexError
        elif index == 0:
            new_node = Node(entry)
            new_node.next =  self._front
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
        elif index == 0:
            removed = self._front.entry
            self._front = self._front.next 
            self._length -= 1
            return removed
        else:
            previous = self._front
            for i in range(index-1):
                previous = previous.next 
            target = previous.next 
            removed = target.entry
            previous.next = target.next 
            target = None
            self._length -= 1
            return removed

    def get_entry(self, index):
        if index < 0 or index > self._length:
            raise IndexError
        elif index == 0:
            return self._front.entry
        else:
            previous = self._front
            for i in range(index-1):
                previous = previous.next
            target = previous.next 
            return target.entry

    def set_entry(self, index, entry):
        if index < 0 or index > self._length:
            raise IndexError
        elif index == 0:
            if self._front == None:
                return
            else:
                self._front.entry = entry
        else:
            previous = self._front
            for i in range(index-1):
                previous = previous.next
            target = previous.next 
            target.entry = entry
        
        
