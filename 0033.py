# a*10+b / b*10+c == a / c

for a in range(1, 10):
   for b in range(a+1, 10):
      for c in range(10):
         if c == a or c == b: continue
         x, y = (a*10+b), (b*10+c)
         if x*c == a*y:
            print('{}/{} == {}/{}'.format(x, y, a, c))
            
