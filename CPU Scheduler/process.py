from function import Function
from stack import Stack 

class Process:
    def __init__(self, process_name):
        self._process_name = process_name 
        self._function_stack = Stack()

    def START(self):
        function = Function('main', None)
        self._function_stack.push(function)
        return print(f'{self._process_name} added to queue')
    
    def CALL(self, function):
        self._function_stack.push(function)
        return print(f'{self._process_name} calls {function.get_name()}')

    def RETURN(self, function):
        self._function_stack.pop()
        return print(f'{self._process_name} returned from {function.get_name()}')

    def RAISE(self, function):
        if function == 'main':
            self._function_stack.pop()
            return print(f'{self._process_name} has ended')
        elif function.get_exceptions() == 'no':
            self._function_stack.pop()
            return
        else:
            return print(f'{function} handled the exception')

    def get_process_name(self):
        return self._process_name
    
    def get_function_stack(self):
        return self._function_stack
