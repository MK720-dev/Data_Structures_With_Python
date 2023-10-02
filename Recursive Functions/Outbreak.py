def PeopleWithFlu(day):
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75
    else:
        return PeopleWithFlu(day-1) + PeopleWithFlu(day-2) + PeopleWithFlu(day-3)
    
print('OUTBREAK!')
day = int(input('What day do you want a sick count for?: '))
while day <= 0:
    print('Invalid day')
    day = int(input('What day do you want a sick count for?: '))
    
print(PeopleWithFlu(day))