#Given a list of non negative integers, arrange them such that they form the largest number.

# Solution: write a custom comparision for the sort
# If XY is larger, then, in the output, X should come before Y, else Y should come before X.


def compare(a, b):
    ab, ba = a + b, b + a
    if ab == ba:
        return 0
    if ab < ba:
        return -1
    return 1


def largestNumber(A):
    A = list(map(str,A))
    A.sort(cmp=self.compare, reverse=True)
    return int(''.join(A))


A = [3, 30, 34, 5, 9]
print largestNumber(A)
