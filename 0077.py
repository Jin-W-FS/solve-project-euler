from common import Prims, WaysSumToWith, count

WaysSumTo = WaysSumToWith(Prims)
for n in count():
    if WaysSumTo(n) > 5000: break
print(n)
