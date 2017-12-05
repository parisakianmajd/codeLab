#Given a binary array and an integer m, find the position of zeroes flipping which creates maximum number of consecutive 1's in array.

# Use sliding window
# Whenever you encounter a 0, increment the counter of zeros.
# window size is m

def zerosToFlip(arr, m):
        if m == 0:
            return
        # wL and wR: sides of the current window
        wL, wR = 0, 0
        # bestL, bestWindow: left side and size of the widest window
        bestL, bestWindow = 0, 0
        zeroCounts = 0
        while wR < len(arr):
            if zeroCounts <= m:
                if arr[wR] == 0:
                    zeroCounts += 1
                wR += 1
            if zeroCounts > m:
                if arr[wL] == 0:
                    zeroCounts -= 1
                wL += 1
            if wR - wL > bestWindow:
                bestWindow = wR - wL
                bestL = wL
        # print the index of zeros in the widest window
        zeroIndexes = []
        for i in xrange(bestWindow):
            if arr[bestL + i] == 0:
                zeroIndexes.append(bestL + i)
        return zeroIndexes

arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
m = 2
print zerosToFlip(arr, m)
