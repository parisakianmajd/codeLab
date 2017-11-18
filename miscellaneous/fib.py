#Generators vs Functions

def fibonacci(n):
    '''Fibonacci numbers generator'''
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(5)

for x in f:
    print x,
print
