from math import *

a =  (1 + sqrt(5)) / 2
# log10(1/sqrt(5)) + n * log10(a) >= 999
n = ceil((999 + log10(5) / 2) / log10(a))
print(n)
