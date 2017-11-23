# Decorators
# from https://www.python-course.eu/python3_decorators.php
import math

#Polynomial Factory
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    





#Polynomial Factory, generalized case
def polynomial_creator(*coefficients):
    """ coefficients are in the form a_0, a_1, ... a_n 
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients):
            res += coeff * x** index
        return res
    return polynomial
  
p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(2, 3, -1, 8, 1)
#p3= x^4 + 8 * x^3 - x^2 + 3 * x + 2





p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))



def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        print func(x)
        print("After calling " + func.__name__)
    return function_wrapper


# a generalized version that accept functions with any number of parameters
def our_decorator2(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        print func(*args, **kwargs)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def succ(n):
    return n + 1




succ(10)
sin = our_decorator(math.sin)
cos = our_decorator(math.cos)
for f in [sin, cos]:
    f(3.14)
