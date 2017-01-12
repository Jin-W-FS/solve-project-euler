from math import log10

lines = [[int(x) for x in l.split(',')] for l in open('data/p099_base_exp.txt')]

vals = [(log10(a)*b, i+1) for i, (a, b) in enumerate(lines)]
vals.sort()

print(vals[-2:])

