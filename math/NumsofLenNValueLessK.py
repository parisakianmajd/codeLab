#Given a set of digits (A) in sorted order,
#find how many numbers of length B are possible whose value is less than number C.
#e.g. Input:
#	  3 0 1 5  
#	  1  
#	  2  
#	Output:  
#	  2 (0 and 1 are possible)  


def get_count(A, B, base, index):
    if index >= len(base) or B==0:
        return 0
    current_max = int(base[index])
    rt = 0
    for x in A:
        if index == 0 and x ==0 and B!=1:
            continue
        if x > current_max:
            continue
        if x == current_max:
            rt += get_count(A, B-1, base, index+1)
        else:
            rt += len(A)**(B-1)
    return rt
    
def solve(A, B, C):
    base = str(C)
    if len(base) < B or C == 0 or len(A) == 0:
        return 0
    if len(base) == B:
        return get_count(A, B, base, 0)
    # if len(Base) > B
    if B == 1:
        return len(A)
    # the first digit can't be zero
    elif 0 in A:
        rt = len(A) - 1
    else:
        rt = len(A) 
    return rt *  len(A)**(B-1)



A = [4, 0, 1, 2, 5]  
B = 2  
C = 21




print solve(A, B, C)
