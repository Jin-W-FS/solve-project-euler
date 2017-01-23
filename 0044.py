from common import IncSerial, count

def __nextNum(lst):
    n = len(lst) + 1
    return n * (3*n-1) // 2

pentagonals = IncSerial([], __nextNum)

def test():
    for j in count(1):
        for i in range(j):
            a, b = pentagonals[i], pentagonals[j]
            c = a + b
            if c in pentagonals:
                d = c + b
                if d in pentagonals:
                    return (b, c, d, a)
                d = c + a # may be wrong
                if d in pentagonals:
                    return (a, c, d, b)
                
print(test())
