# Longest Palindromic Substring


def longestPalindrome(self, A):
        maxLen = 1

        start = 0
        length = len(A)

        low = 0
        high = 0

        # One by one consider every character as center point of 
        # even and length palindromes
        for i in xrange(1, length):
            # Find the longest even length palindrome with center points as i-1 and i.
            # and odd length ones centered at i-1, i+1
            for (low, high) in [(i-1, i), (i-1, i+1)]:
                while low >= 0 and high < length and A[low] == A[high]:
                    if high - low + 1 > maxLen:
                        start = low
                        maxLen = high - low + 1
                    low -= 1
                    high += 1
        return A[start:start + maxLen]
