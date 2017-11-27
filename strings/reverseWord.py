# Given an input string, reverse all the words
import string

def reverseWords(text):
    print ' '.join(text.split()[::-1])

def reverseWords2(text):
    index = 0
    space = string.whitespace
    words = []
    while index < len(text):
        if text[index] not in space:
            wordStart = index
            while index < len(text) and text[index] not in space:
                index += 1
            words.append(text[wordStart:index])
        index += 1
    print ' '.join(reversed(words))

reverseWords('CS    degree')
reverseWords2('CS      degree')
