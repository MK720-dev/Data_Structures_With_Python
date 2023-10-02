
class Function:
    def __init__(self, name, exceptions):
        self._name = name
        self._exceptions = exceptions

    def get_name(self):
        return self._name
    
    def get_exceptions(self):
        return self._exceptions
    
    def __str__(self):
        return(f'{self._name}, {self._exceptions}')