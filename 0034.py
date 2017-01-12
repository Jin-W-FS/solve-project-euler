from common import digits

factorials = [1] * 10
for i in range(1, 10):
   factorials[i] = factorials[i-1] * i


s = 0
for n in range(10, 1499999):
   if n == sum(factorials[int(s)] for s in str(n)):
      print(n)
      s += n
print("total:", s)
