class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        right = left = 0
        while right < len(intervals):
                if start <= intervals[right].end:
                        if end < intervals[right].start:
                                break
                        start = min(start, intervals[right].start)
                        end = max(end, intervals[right].end)
                else:
                        left += 1
                right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]
                
intervals = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
newInterval = Interval(4,9)
intervals = insert(intervals, newInterval)
for inter in intervals:
    print [inter.start, inter.end]
