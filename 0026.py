
def recurringCycleLen(n):
    if n % 2 == 0 or n % 5 == 0:
        # should be the same as n//2 or n//5, so mark as 0
        return 0
    # find N that 10**N % n == 1
    loop, d = 1, 9
    while d % n:
        d = d * 10 + 9
        loop += 1
    return loop

print(max((recurringCycleLen(i), i) for i in range(1, 1000)))

