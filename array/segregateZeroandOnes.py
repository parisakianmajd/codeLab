
# Segregate 0s and 1s in an array

def segregate(A):
    left = 0
    right = len(A) - 1
    while left < right:
        while A[left] == 0 and left < right:
            left += 1
        while A[right] == 1 and left < right:
            right -= 1
        if left < right:
            A[left] = 0
            A[right] = 1
            left += 1
            right -=1

A = [0,0,1,1,0,1, 0, 0, 1]
segregate(A)
print A
