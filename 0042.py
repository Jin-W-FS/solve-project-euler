from math import floor, sqrt

def isTriangleNum(n):
    n *= 2
    m = floor(sqrt(n))
    return m * (m + 1) == n

def wordValue(s):
    return sum((ord(c) - ord('A') + 1) for c in s)


print(sum(isTriangleNum(wordValue(word))
          for word in eval(open('data/p042_words.txt').read())))
        
        
