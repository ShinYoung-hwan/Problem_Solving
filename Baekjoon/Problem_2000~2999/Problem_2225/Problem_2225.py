import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_000

def solve(n, k):
    # dp base
    if dp[n][k] >= 0:
        return dp[n][k]
    
    # recursion base
    if k == 0:
        dp[n][k] = (n == 0)
        return dp[n][k]
    
    # recursion default
    dp[n][k] = 0
    for i in range(n+1):
        dp[n][k] = (dp[n][k] + solve(n-i, k-1)) % MOD
    return dp[n][k]

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    dp = [ [ -1 ] * (K+1) for _ in range(N+1) ]
    
    print(solve(N, K))
            