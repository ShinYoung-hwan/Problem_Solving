import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    
    coins = sorted([ int(input()) for _ in range(n) ])
    
    dp = [ 0 ] * (k+1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] += dp[i-coin]
    
    print(dp[k])