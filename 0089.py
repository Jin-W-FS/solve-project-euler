import RomanNum

s = 0
for line in open('data/p089_roman.txt'):
    line = line.strip()
    short = RomanNum.toRoman(RomanNum.toDigit(line))
    d = len(line) - len(short)
    assert(d >= 0)
    s += d
    # print(line, short, d)
print(s)
