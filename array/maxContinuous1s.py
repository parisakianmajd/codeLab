
# Given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.
# Return the indices of maximum continuous series of 1s in ordpointer i and j 

# Solution:
# use two pointers initialized at 0 to keep track of the left and right of the window


def maxOnes(arr, flips):
    wl = wr = 0
    bestWindow = 0
    count = 0
    while wr < len(arr):
        if count <= flips:
            if arr[wr] == 0:
                count += 1
            wr += 1
        if count > flips:
            if arr[wl] == 0:
                count -= 1
            wl += 1

        if count <= flips and wr - wl + 1 > bestWindow:
             bestWindow = wr - wl + 1
             bestwl = wl
    return range(bestwl, bestwl + bestWindow - 1)


arr = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
f = 1
print maxOnes(arr, f)
