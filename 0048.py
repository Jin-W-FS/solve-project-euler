N = 10**10
print(sum(n**n % N for n in range(1, 1001)) % N)
