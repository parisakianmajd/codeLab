# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

#Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#Extra spaces between words should be distributed as evenly as possible.

def fullJustify(A, B):
    if len(A) == 0:
        return []
    lines = []
    i = 0
    while i < len(A):
        line = ""
        lineWords = []
        length = 0
        k = i
        while k < len(A):
            if length + len(lineWords) + len(A[k]) <= B:
                lineWords.append(A[k])
                length += len(A[k])
            else:
                break
            k += 1
        i = k
        if k < len(A):
            if len(lineWords) > 1:
                space = (B - length)/(len(lineWords)-1)
                remain = (B - length)%(len(lineWords)-1)
                for j in range(len(lineWords)-1):
                    line += lineWords[j]
                    line += " " * space
                    if remain > 0:
                        line += " "
                    remain -= 1
                line += lineWords[-1]
            else:
                line += lineWords[0]
                line += " " * (B - len(line))
        else:
            line += lineWords[0]
            for j in range(1,len(lineWords)):
                line += " " + lineWords[j]
            line += " " * (B - len(line))
        lines.append(line)
    return lines



A = [ "glu", "muskzjyen", "ahxkp", "t", "djmgzzyh", "jzudvh", "raji", "vmipiz", "sg", "rv", "mekoexzfmq", "fsrihvdnt", "yvnppem", "gidia", "fxjlzekp", "uvdaj", "ua", "pzagn", "bjffryz", "nkdd", "osrownxj", "fvluvpdj", "kkrpr", "khp", "eef", "aogrl", "gqfwfnaen", "qhujt", "vabjsmj", "ji", "f", "opihimudj", "awi", "jyjlyfavbg", "tqxupaaknt", "dvqxay", "ny", "ezxsvmqk", "ncsckq", "nzlce", "cxzdirg", "dnmaxql", "bhrgyuyc", "qtqt", "yka", "wkjriv", "xyfoxfcqzb", "fttsfs", "m" ]
B = 144
print fullJustify(A, B)
