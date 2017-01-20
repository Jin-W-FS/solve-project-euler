
with open('data/p022_names.txt') as file:
    names = [ v.split('"')[1] for v in file.read().split(',') ]
names.sort()

def score(name):
    sc = lambda v: ord(v) - ord('A') + 1
    return sum(sc(v) for v in name)

print(sum((i+1)*score(n) for i, n in enumerate(names)))

