#Given a non-negative number represented as an array of digits,
#add 1 to the number ( increment the number represented by the digits ).


# e.g.  [1, 2, 3] ->  [1, 2, 4]

def inc(A):
        i = len(A) - 1
        if A[i] < 9:
            A[i] += 1
        else:
            digits = 0
            while A[i] == 9 and i > 0:
                digits += 1
                A[i] = 0
                i -= 1
            if i == 0:
                if A[i] == 9:
                    A = [1] + (digits + 1) * [0]
                else:
                    A[i] += 1
            else:
                A[i] += 1
        i = 0
        while A[i] == 0:
            i += 1
        A = A[i:]
        return A                
    
print inc([ 6, 4, 7, 7, 8, 9 ])
