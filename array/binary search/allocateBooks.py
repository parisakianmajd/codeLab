
# Solution Approach
# do a binary search for max of X pages per student and check if it's feasible
# to check if it's feasible, keep allocating books to the first student until it gets more than max then add another student,.. if you ran out of books, it's feasible
#  O(NlogM) where N is the number of books and M is the total number of pages
def isPossible(books, n, mid):
    if mid < max(books):
        return False
    students = 0
    currentSum = 0
    for b in books:
        if b > mid:
            return False
        if currentSum + b <= mid:
            currentSum += b
        else:
            students += 1
            currentSum = b
            if students >= n:
                return False
    return True
    
def books(books, n):
    if len(books) < n:
        return -1
    low = min(books)
    high = sum(books)
    result = -1
    while low <= high:
        mid = (low+high)/2
        if isPossible(books, n, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B = 5
print books(A, B)

