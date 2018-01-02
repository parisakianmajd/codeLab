# return the square root of x.



def sqrt(A):
    if A == 0 or A == 1:
        return A
    start = 1
    end = A
    while start <= end:
        mid = (start + end) / 2
        if mid * mid == A:
            return mid
        elif mid * mid < A:
            # since we only need the floor, we update the ans everytime our search lands in tt
            # the smaller half
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
