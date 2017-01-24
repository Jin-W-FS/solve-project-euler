from common import digits
print(max(((sum(digits(a**b)), a, b) for a in range(1, 100) for b in range(1, 100))))
