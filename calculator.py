import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypotenuse(a,b)

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

def log(a,b):
    if b < 0 and b == 1:
        raise ValueError
    else:
        return math.log(a,b)

def exp(a,b):
    return a ** b

print(log(5,1))