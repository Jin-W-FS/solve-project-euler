from math import factorial

def PermuteN(nums, N):
    '''N counts from 0'''
    rem = N
    nums = list(sorted(nums))
    rlt = 0
    i = len(nums)
    while nums:
        i -= 1
        f = factorial(i)
        n, rem = divmod(rem, f)
        rlt = rlt * 10 + nums.pop(n)
    return rlt

print(PermuteN(range(10), 1000000 - 1))
