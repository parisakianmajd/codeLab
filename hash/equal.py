#Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array


def equal(A):
    table = {}
    result = []
    for i in xrange(len(A)):
        for j in xrange(i+1, len(A)):
            currentSum = A[i] + A[j]
            if currentSum in table:
                a, b, c, d = table[currentSum] + [i,j]
                if a < c and b != c and b != d:
                    result.append([a, b, c, d])   
            else:
                table[currentSum] = [i, j]
    if len(result) == 0:
        return []
    return min(result)
            
        

A = [ 1, 1, 1, 1, 1 ]
print equal(A)

