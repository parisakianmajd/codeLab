def mergeIntervals(intervals):
    # sort the intervals according to the start time
    sorted_by_start = sorted(intervals, key = lambda tup: tup[0])
    merged = []

    for higher in sorted_by_start:
        if not merged:
            # push the first interval into the stack
            merged.append(higher)
        else:
            lower = merged[-1]
            # if it overlaps with top of stack 
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  
            else:
                # if it doesn't overlap with top of the stack push it
                merged.append(higher)
    return merged


intervals = [(6,8), (1,9), (2,4), (4,7)]
intervals2 = [[1,3],[2,6],[8,10],[15,18]]
print mergeIntervals(intervals2)
