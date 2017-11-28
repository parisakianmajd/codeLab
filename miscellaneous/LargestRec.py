#Largest rectangular area in a histogram

def largestRecArea(hist):
    heights = []
    positions = []
    maxArea = -1
    for i in xrange(len(hist)):
        # if stack is empty or the the current value is larger that the top value
        # we might be at the begining of the largest rec area
        if len(heights) == 0 or hist[i] > heights[-1]:
            heights.append(hist[i])
            positions.append(i)
        # if the current value is less that the top value
        # we are at the end of the area
        elif hist[i] < heights[-1]:
            while len(heights) > 0 and hist[i] < heights[-1]: 
                h = heights.pop()
                p = positions.pop()
                area = h * (i-p)
                if area > maxArea:
                    maxArea = area
            if len(heights) == 0:
                heights.append(hist[i])
                # if the stack becomes empty, add the last position back because that's the start of the current rec
                positions.append(p)
    while len(heights):
        h = heights.pop()
        index = positions.pop()
        area = (len(hist)- index) * h
        if area > maxArea:
            maxArea = area
    return maxArea

h = [1, 3, 2, 1, 2]
print largestRecArea(h)
h = [2, 1, 2, 3, 1]
print largestRecArea(h)
