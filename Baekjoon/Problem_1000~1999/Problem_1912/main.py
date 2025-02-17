import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    
    # solve O(n)
    dp = [0] * n
    dp[0] = sequence[0]
    
    for i in range(1, n):
        dp[i] = max([dp[i-1], 0]) + sequence[i]
    
    print(max(dp))