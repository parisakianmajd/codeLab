
#Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#Sample Input :
#(1, 1)
#(2, 2)
#Sample Output : 2
# You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])



def maxPoints(x, y):
        hashMap = {}
        maxPoints = 0
        for i in xrange(len(x)):
            duplicates = 1
            vertical = 0
            for j in xrange(i +1 , len(x)):
                if x[i] == x[j]:
                    if y[i] == y[j]:
                        duplicates += 1
                    else:
                        vertical += 1
                else:
                    slope = 0.0 if y[i] == y[j] else 1.0*(y[j] - y[i])/(x[j] - x[i])
                    if slope in hashMap:
                        hashMap[slope] += 1
                    else:
                        hashMap[slope] = 1
            for count in hashMap.values():
                if count + duplicates > maxPoints:
                    maxPoints = count + duplicates
            maxPoints = max(vertical + duplicates, maxPoints)
            hashMap.clear()
        return maxPoints


x = [0, 0, 1]
y = [1, -1, -1]
print maxPoints(x, y)
