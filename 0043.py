from common import Arranges, cmbdigits

def cmb(v):
    return 100*v[0] + 10*v[1] + v[2]

def check(v):
    if v[0] == 0: return False
    if v[5] not in (0, 5): return False  # v[3:6] % 5 == 0
    if v[3] % 2 != 0: return False  # v[1:4] % 2 == 0
    if sum(v[2:5]) % 3 != 0: return False   # v[2:5] % 3 == 0
    if cmb(v[4:7]) % 7 != 0: return False
    if cmb(v[5:8]) % 11 != 0: return False
    if cmb(v[6:9]) % 13 != 0: return False
    if cmb(v[7:10]) % 17 != 0: return False
    return True

lst = []
for v in Arranges(list(range(10))):
    if check(v): lst.append(v)
print(sum(cmbdigits(v) for v in lst))
