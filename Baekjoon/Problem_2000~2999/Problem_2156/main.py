import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(n, alchols):
    if n == 1:
        return alchols[0]
    
    dp = [ 
        [ 0 ] * n, # 한잔 이상 건너뛰고 마시는 경우
        [ 0 ] * n  # 두잔 연속으로 마시는 경우
    ]
    dp[0][0], dp[0][1] = alchols[0], alchols[1]
    dp[1][0], dp[1][1] = 0, alchols[0] + alchols[1]
    
    max_value = dp[0][0]
    for i in range(2, n):
        dp[0][i] = max_value + alchols[i]
        dp[1][i] = dp[0][i-1] + alchols[i]
        
        max_value = max([max_value, dp[0][i-1], dp[1][i-1]])
    
    return max([dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2]])
    
if __name__ == "__main__":
    n = int(input())
    alchols = [ int(input()) for _ in range(n) ]
    
    print(solve(n, alchols))
