import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n = int(input())

    # set datas
    dp = [ [ 0 ] * 10 for _ in range(n) ]
    dp[0] = [1] * 10
    
    for r in range(1, n):
        # c == 0
        dp[r][0] = dp[r-1][1]
        
        # c == 9
        dp[r][9] = dp[r-1][8]
        
        # else
        for c in range(1, 9):
            dp[r][c] = dp[r-1][c-1] + dp[r-1][c+1]
    
    # solve
    print(sum(dp[n-1][1:]) % 1_000_000_000)