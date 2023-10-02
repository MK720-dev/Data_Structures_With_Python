
def RecursivePower(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base 
    else:
        return base*RecursivePower(base, exponent-1)
    

base = int(input('Enter a base: '))
exponent = int(input('Enter a power: '))
while exponent < 0:
    print('Sorry, your exponent must be zero or larger.')
    exponent = int(input('Enter a power: '))
print(RecursivePower(base, exponent))
