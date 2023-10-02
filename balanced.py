from stack import Stack

def main():
    sequence = input('enter sequence: ')
    seq_stack = Stack()

    for i in range(len(sequence)):
        seq_stack.push(sequence[i])

    def unbalanced(seq_stack):
        if seq_stack.is_empty():
            print('sequence unbalanced')
        else: 
            right = 0
            left = 0
            while not(seq_stack.is_empty()):
                if seq_stack.peek() == ')':
                    right += 1 
                    seq_stack.pop()
                else:
                    left += 1
                    seq_stack.pop()
                    if seq_stack.peek() == ')':
                        print('unbalanced')
                        return
        if left == right:
            print('balanced')
            return
        else:
            print('unbalanced')
            return
    unbalanced(seq_stack)

main()