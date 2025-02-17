import sys

MAX = 10000 + 1

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = sorted(list(set([ int(input()) for _ in range(N) ])))
    dp = [ MAX ] * (K+1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, K+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    
    print(-1 if dp[K] == MAX else dp[K])