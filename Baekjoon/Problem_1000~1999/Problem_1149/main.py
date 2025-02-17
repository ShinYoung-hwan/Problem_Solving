import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

if __name__ == "__main__": 
    n = int(input()) # 집의 수
    rgb_cost = [ [ int(e) for e in line.split() ] for line in inputs() ] # 각 집의 색깔을 r, g, b로 색칠할 때의 비용
    
    # 각 집의 색을 r, g, b로 할 때의 최소 비용 케이스
    dp = [ [0, 0, 0] for _ in range(n) ]
    dp[0][0], dp[0][1], dp[0][2] = rgb_cost[0][0], rgb_cost[0][1], rgb_cost[0][2]
    
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb_cost[i][2]
    
    print(min(dp[n-1]))