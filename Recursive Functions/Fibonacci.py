
def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
    

instruction = input('Enter mode and value: ')
mode = instruction.split()[0]
value = int(instruction.split()[1])
while not(mode in ['-i', '-v']):
    print('Mode you entred is inavlid')
    mode = input('Enter a valid mode: ')
if mode == '-i':
    while value < 0:
        print('Value you entred is inavlid')
        value = input('Enter a valid value: ')
    print(Fibonacci(value))
elif mode == '-v':
    if value < 0:
        print(f'{value} is not in the sequence')
    else:
        sequence = [0]
        i = 0
        while sequence[i] < value:
            i += 1
            sequence.append(Fibonacci(i))
        in_sequence = False
        for j in range(len(sequence)):
            if sequence[j] == value:
                in_sequence = True 
                break
        if in_sequence == True:
            print(f'{value} is in the sequence')
        else:
            print(f'{value} is not in the sequence')


    


    
