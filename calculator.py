# https://github.com/FALLENx4NGEL/LAB11-JK-ET
import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    if a < 0 or b < 0:
        raise ValueError
    else:
        return math.hypot(a,b)

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

def logarithm(a,b):
    if b <= 0 or b == 1:
        raise ValueError
    else:
        return math.log(a,b)

def exp(a,b):
    return a ** b
