import sys
sys.setrecursionlimit(10 ** 4)

input = lambda: sys.stdin.readline().rstrip()

MOD = 10_007

def comb(N, K):
    if N == K: return 1
    elif K == 0: return 1
    
    if not dp[N][K]:
        dp[N][K] = (comb(N-1, K-1) + comb(N-1, K)) % MOD
    
    return dp[N][K]

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    dp = [ [ 0 ] * (N+1) for _ in range(N+1) ]

    print(comb(N, K))
    