#Find out the maximum sub-array of non negative numbers from an array.
#NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
#NOTE 2: If there is still a tie, then return the segment with minimum starting index
def maxset(A):
        maxSub = []
        start = end = 0
        for i in xrange(len(A)+1):
            if i < len(A) and A[i] >= 0:
                end = i
            else:
                if start < i:
                    currentSub = A[start:end+1]
                    if sum(currentSub) > sum(maxSub) or \
                       sum(currentSub)== sum(maxSub) and\
                       (len(currentSub) > len(maxSub) or currentSub[0] < maxSub[0]):
                        maxSub = currentSub
                start = i + 1
                end = start    
        return maxSub

print maxset([ 1, 2, 5, -7, 2, 5 ])
print maxset([-1, -1])
