
def ways(M, N):
    # return sum(m * n for m in range(M, 0, -1) for n in range(N, 0, -1))
    return M*(M+1)*N*(N+1)//4

# S = 2000000
# M*(M+1)*N*(N+1)//4 ~ S
# M*N < 2828

print(min((abs(2000000 - ways(m, n)), m, n)
          for m in range(2828, 0, -1)
          for n in range(2828//m, 0, -1)))

