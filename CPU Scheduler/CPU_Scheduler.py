from process import Process
from function import Function
from linkedqueue import LinkedQueue

class CPU_Scheduler():
    def __init__(self, file):
        self._processes_queue = LinkedQueue()
        self._command_list = []
        processes_list = []
        functions_list = []

        f = open(file, encoding='utf-8')

        for line in f: 
            self._command_list.append(line.strip(' \n').split())

        for command in self._command_list:
            if command[0] == 'START':
                process = Process(command[1])
                self._processes_queue.enqueue(process)
                process.START()
                processes_list.append(process.get_process_name())
                functions_list.append('main')
            elif command[0] == 'CALL':
                if not(self._processes_queue.is_empty()):
                    function = Function(command[1], command[2])
                    functions_list.append(function.get_name())
                    process_function = self.function_process_list(processes_list, functions_list)
                    for i in range(len(process_function)):
                        if process_function[i][1] == function.get_name():
                            process = Process(process_function[i][0])
                            process.CALL(function)
                            self._processes_queue.dequeue()
                            self._processes_queue.enqueue(process)
                            break
            elif command[0] == 'RETURN':
                 if not(self._processes_queue.is_empty()):
                     process = Process(self._processes_queue.peek_front().get_process_name())
                     process_function = self.function_process_list(processes_list, functions_list)    
                     exceptions = self.exceptions_list()
                     for i in range(len(process_function)):
                         if process_function[i][0] == process.get_process_name():
                             if process_function[i][1] == 'main':
                                 function = Function('main', None)
                                 process.RETURN(function)
                                 break
                             else:
                                 for j in range(len(exceptions)):
                                     if exceptions[j][0] == process_function[i][1]:
                                        function = Function(process_function[i][1], exceptions[j][0])
                                        break
                                 process.RETURN(function)
                                 print(f'{process.get_process_name()} returns from {function.get_name()}')
                     if process.get_function_stack().is_empty():
                         self._processes_queue.dequeue()
                         print(f'{process.get_process_name()} has ended')
                     else:
                         self._processes_queue.dequeue()
                         self._processes_queue.enqueue(process)

            elif command[0] == 'RAISE':
                if not(self._processes_queue.is_empty()):
                     process = Process(self._processes_queue.peek_front().get_process_name())
                     process_function = self.function_process_list(processes_list, functions_list)    
                     exceptions = self.exceptions_list()
                     for i in range(len(process_function)):
                         if process_function[len(process_function) - 1][0] == process.get_process_name():
                            process.RAISE(function)
                            if process_function[len(process_function) - 1][1]:
                                self._processes_queue.dequeue()
                            
                                       
    def function_process_list(self, processes, functions):
        function_process = []
        non_main_functions = []
        if not(self._processes_queue.is_empty()) and (len(functions) != 0):
            if self._processes_queue.size == 1:
                for i in range(len(functions)):
                    function_process.append([processes[0], functions[i]])
            else:
                j = 0
                for i in range(len(functions)):
                    if functions[i] == 'main':
                        function_process.append([processes[j], functions[i]])
                        j += 1
                for i in range(len(functions)):
                    if functions[i] != 'main':
                        non_main_functions.append(functions[i])
                k = 0      
                for i in range(len(processes)):
                    if k < len(non_main_functions):
                        function_process.append([processes[i], non_main_functions[k]])
                        k += 1
            return function_process
    
    def exceptions_list(self):
        exceptions = []
        for command in self._command_list:
            if len(command) == 3:
                exceptions.append([command[1], command[2]])
        return exceptions
                


file = 'C:/Users/kchao/OneDrive/Documents/Dossier_Malek/EECS_268/Lab2/input_file1.txt'      
CPU = CPU_Scheduler(file)

