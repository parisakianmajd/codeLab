
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


def mergeIntervals(intervals):
    sorted_by_start = sorted(intervals, key = lambda x: x.start)
    merged = []

    for higher in sorted_by_start:
        if not merged:
            # push the first interval into the stack
            merged.append(higher)
        else:
            lower = merged[-1]
            # if it overlaps with top of stack 
            if higher.start <= lower.end:
                upper_bound = max(lower.end, higher.end)
                merged[-1] = Interval(lower.start, upper_bound)  
            else:
                # if it doesn't overlap with top of the stack push it
                merged.append(higher)
    return merged



times = [(6,8), (1,9), (2,4), (4,7)]
intervals = []
for t in times:
    intervals.append(Interval(t[0],t[1]))
merged= mergeIntervals(intervals)
for  m in merged:
    print (m.start, m.end),
