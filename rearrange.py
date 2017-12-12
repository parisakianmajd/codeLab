# PROBLEM 1. Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

# Solution:
#(x+y*z)/z=y provided x,y is less than z
#(x+y*z)%z=x provided x,y  is less than z

# increase each element arr[i] by (arr[arr[i]%n])*n)


def arrange(A):
    n = len(A)
    for i in xrange(len(A)):
        A[i] += (A[A[i]]%n) * n
    # use A[:] to maintain the reference to the orginial list
    A[:] = [a/n for a in A]
    return A


# PROBLEM 2.Rearrange an array such that 'arr[j]' becomes 'i' if 'arr[i]' is 'j'


 

def rearrange(arr):
    # To check whether an element is processed or not, we change the value of processed items arr[i] as -arr[i].
    # since zero cannot be negated, we increment all element by 1 in the begining and decrement them at the end
    arr[:] = [x+1 for x in arr]
    for i in xrange(len(arr)):
       if arr[i] > 0:
           val = -(i+1)
           i = arr[i] - 1

           while arr[i] > 0:
               new_i = arr[i] - 1
               arr[i] = val
               val = -(i + 1)
               i = new_i
    arr[:] = [-x-1 for x in arr]

arr = [2, 0, 1, 4, 5, 3]
rearrange(arr)
print arr
arrange(arr)
print arr
 
