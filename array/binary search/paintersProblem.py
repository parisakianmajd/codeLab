# You have to paint N boards of given lengths with k painters
# You know how much time a painter takes to paint 1 unit of board.
# You have to get this job done as soon as possible under the constraints
# that any painter will only paint contiguous sections of board.


# solution approach
    # min len a painer can paint is the max size of the boards 
    # because, like other boards, the max size board has to be pianted by one painter and cannot be share 
    # max len per painter is the sum of sizes of all of the boards, i.e. if one painter paints them all
    # use binary search to find an optimal approach in between



def paint(n, k, boards):

    low = max(boards)
    high = sum(boards)

    while low + 1 < high:
        mid = low + (high - low)/2
        painters = getPainters(boards, mid)
        if painters <= n:
            high = mid
        else:
            low = mid + 1
    if getPainters(boards, low) <= n:
        return k * low  % 10000003
    else:
        return k * high  % 10000003

def getPainters(boards, perPainter):
    painters = 1
    total = 0
    for a in boards:
        total += a
        if total > perPainter:
            total = a
            painters += 1
    return painters 




###
def paint2(n, k, boards):
    return binsearch(n, k, boards, max(boards), sum(boards))
    
def binsearch(n, k, boards, low, high):
    while low + 1 < high:
        mid = low + (high - low) / 2
        if isPossible(mid, n, k, boards):
            high = mid
        else:
            low = mid + 1 
    if isPossible(low, n, k, boards):
        return low * k % 10000003
    else:
        return high * k % 10000003
def isPossible(mid, n, k, boards):
    painters = 1
    total = 0
    for a in boards:
        total += a
        if total > mid:
            total = a
            painters += 1
    return painters <= n





A = 5
B = 10
C = [ 658, 786, 531, 47, 169, 397, 914 ]
print paint(A, B, C)
