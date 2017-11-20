
class Job():
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self. profit = profit



def findweightedJobSchedulingMaximumProfit(jobs):
    jobs.sort(key = lambda j : j.end)
    temp = [j.profit for j in jobs]
    for i in xrange(1,len(jobs)):
        for j in xrange(i-1,-1, -1):
            if jobs[j].end <= jobs[i].start:
                # no overlap
                temp[i] = max(temp[i], temp[j] + jobs[i].profit)
    return max(temp)






jobs = []
jobs.append(Job(1,3,5))
jobs.append(Job(7,9,2))
jobs.append(Job(6,7,4))
jobs.append(Job(2,5,6))
jobs.append(Job(4,6,5))
jobs.append(Job(5,8,11))

print findweightedJobSchedulingMaximumProfit(jobs)
