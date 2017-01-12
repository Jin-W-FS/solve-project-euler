
def find():
    for c in range(500, 1, -1):
        for b in range(1000 - c, 1, -1):
            if b > c: continue
            a = 1000 - c - b
            if a > b or a == 0: continue
            if a**2 + b**2 == c**2:
                return (a, b, c)
print(find())


