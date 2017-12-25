#There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.


#Solution:
#string :  .x..x..x.
#positions where x are present {1, 4, 7}
#Median is 4. So we will move all x near our median. 1st person would need to jump 2 steps and 3rd person would also need to jump 2 steps. Total answer = 4. 

def seats(A):
   n = len(A)
    sitting = [i for i in xrange(n) if A[i]=='x']
    ns = len(sitting)
    if ns <= 1:
        return 0
    median = 0
    if ns % 2 == 1:
        median = sitting[ns/2]
    else:
        median = (sitting[ns/2] + sitting[ns/2-1] +1) / 2
    step, target = 0, median - 1
    for i in xrange((ns-2)/2,-1,-1):
        step += target - sitting[i]
        target -= 1
    target = median
    for i in xrange(ns/2,ns):
        step += sitting[i] - target
        target += 1
    return step % 10000003
