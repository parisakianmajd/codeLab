#Given a number, find the next smallest palindrome larger than the number. For example if the number is 125, next smallest palindrome is 131.

# Solution
#       if number of digits is ODD:
#           mirror the number around the center number e.g. 125 --> 121
#           if the result is larger than the number, we're done, otherwise, increment the middle digit 125 -> 121 -> 131
#           if the middle digit is 9, round the number to the next number and do the same process. e.g. 397 -> 400 -> 404
#       if number of digits is even
#           take the middle two digits as center e.g. 1234 -> 1221 -> 1331

def roundUp(num):
    n = len(num)
    num = int(num)
    increment = pow(10,(n/2)+1)
    return ((num/increment)+1)*increment

def nextPalindrome(num):
    num = str(num)
    n = len(num)
    leftHalf = num[:n/2]
    middle = num[(n-1)/2]
    if n % 2 != 0:
        increment = pow(10, n/2)
        newNum = int(leftHalf + middle + leftHalf[::-1])
    else:
        increment = int(1.1*pow(10, n/2))
        newNum= int(leftHalf + leftHalf[::-1])
        
    if newNum > int(num):
        return newNum
    elif middle != '9':
        return newNum + increment
    else:
        return nextPalindrome(roundUp(num))

print nextPalindrome(123)
print nextPalindrome(198)
print nextPalindrome(1997)

print nextPalindrome(1234)



