#Write a program to validate if the input string has redundant braces?
# e.g. ((a + b))  and (a) have redundant braces


def braces(A):
    braces = 0
    for char in A :
        if char == '(' :
            braces += 1
        elif char in "*/+-" :
            braces -= 1
        if braces < 0 :
            braces = 0
    if braces == 0 :
        return 0
    else :
        return 1    


A = "(a+(a+b))"
print braces(A)
