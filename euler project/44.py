import sys
pantagons = []
minDiff = sys.maxint
for i in xrange(1,3000):
    pantagons.append(i * (3 * i - 1) / 2)
for i in xrange(len(pantagons)):
    print i
    for j in xrange(i+1, len(pantagons)):
        if (pantagons[i] + pantagons[j]) > pantagons[-1]:
            break
        elif (pantagons[i] + pantagons[j]) in pantagons:
            if (pantagons[j] - pantagons[i]) in pantagons:
                if (pantagons[j] - pantagons[i]) < minDiff:
                    minDiff = pantagons[j] - pantagons[i]
                    print pantagons[j],
                    print '   ',
                    print pantagons[i]
print minDiff
