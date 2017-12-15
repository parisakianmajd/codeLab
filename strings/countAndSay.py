#The count-and-say sequence is the sequence of integers beginning as follows:

#1, 11, 21, 1211, 111221, ...
#1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.

def say(word):
    char = word[0]
    c = 1
    i  = 1
    rt = ""
    while i < len(word):
        if word[i] == char:
            c += 1
        else:
            rt += str(c) + char
            c = 1
            char = word[i]
        i += 1
    rt +=  str(c) + char
    return rt
            


def countAndSay(A):
    if A == 1:
        return 1
    word = '1'
    for a in xrange(A):
        word = say(word)
        
    return word
    
        
            
        
        


print countAndSay(10)
