def zero(operation=None): 
    if operation:
        return operation(0)
    else: 
        return 0
    
def one(operation=None): 
    if operation:
        return operation(1)
    else:
        return 1
    
def two(operation=None): 
    if operation:
        return operation(2)
    else:
        return 2
    
def three(operation=None):
    if operation:
        return operation(3)
    else:
        return 3
    
def four(operation=None): 
    if operation:
        return operation(4)
    else:
        return 4
    
def five(operation=None):
    if operation:
        return operation(5)
    else:
        return 5
    
def six(operation=None):
    if operation:
        return operation(6)
    else:
        return 6
    
def seven(operation=None): 
    if operation:
        return operation(7)
    else:
        return 7
    
def eight(operation=None): 
    if operation:
        return operation(8)
    else:
        return 8
    
def nine(operation=None): 
    if operation:
        return operation(9)
    else:
        return 9

def plus(y): 
    return lambda x: x + y

def minus(y): 
    return lambda x: x - y

def times(y): 
    return lambda x: x * y

def divided_by(y): 
    return lambda x: x // y


output = (seven(plus(five())))
print(output)  # Output should be 12

output2 = (four(minus(two())))
print(output2)  # Output should be 2

output3 = (eight(times(three())))
print(output3)  # Output should be 24

output4 = (nine(divided_by(three())))
print(output4)  # Output should be 3

output5 = (six(divided_by(two())))
print(output5)  # Output should be 3

