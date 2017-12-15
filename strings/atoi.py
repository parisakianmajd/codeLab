#The atoi() function takes a string
#(which represents an integer) as an argument and returns its value.
#e.g.Input : "9 2704"
# Output : 9 

def atoi(A):
    if len(A) < 1:
        return 0
    i = 0
    num =0
    sign = 1
    if A[0] in ["+", "-"]:
        i = 1
        if A[0] == "-":
            sign = -1
    while i < len(A):
        if A[i].isdigit():
            num = num*10 + (ord(A[i]) - ord('0'))
        else:
            break
        i += 1
    return max(-2**31, min(sign * num,2**31-1))
