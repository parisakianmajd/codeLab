# Check whether a given string is an interleaving of two other given strings


# cache keeps the false attemps
def isShuffle(str1, str2, str3, cache()):
    if (str1, str2) in cache:
        return False
    
    if len(str1) + len(str2) != len(str3):
        return False
    if not str1 or not str2 or not str3:
        if str1 + str2 = str3:
            return True
        else:
            return False
    if str1[0] != str3[0] and str2[0] !== str3[0]:
        return False
    
    if str1[0] == str3[0] and isShuffle(str1[1:], str2, str3[1:]):
        return True
    
    if str2[0] == str3[0] and isShuffle(str1, str2[1:], str3[1:]):
        return True

    cache.add((str1, str2))
    return False

def isShuffle2(str1, str2, str3):
 
    i = 0
    j = 0
    k = 0
 
    while k != len(str3)-1:
 
        if str1[i] == str3[k]:
            i+=1
 
        elif str2[j] == str3[k]:
            j+=1
 
        else:
            return False
 
        k+=1
 
    if str1[i-1] or str2[j-1]:
        return False
 
    return True
 
