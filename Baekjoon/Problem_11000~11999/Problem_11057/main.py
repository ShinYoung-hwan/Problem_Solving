import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 10_007

def solve(prev=0, depth=0):
    global dp
    
    if depth == N:
        return 1
    
    elif dp[prev][depth]:
        return dp[prev][depth]
    
    for i in range(prev, 10):
        dp[prev][depth] = (dp[prev][depth] + solve(i, depth+1)) % MOD
        
    return dp[prev][depth]

if __name__ == "__main__":
    N = int(input())
    
    dp = [ [ 0 ] * N for _ in range(10) ]
    
    print(solve())