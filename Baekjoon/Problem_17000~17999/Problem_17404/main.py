import sys
import math

input = lambda: sys.stdin.readline().rstrip()

def set_dp(dp: dict, rgb_cost: list, n: int):
    dp['r'][0][0], dp['r'][0][1], dp['r'][0][2] = rgb_cost[0][0], math.inf, math.inf # r을 먼저 선택할 경우
    dp['g'][0][0], dp['g'][0][1], dp['g'][0][2] = math.inf, rgb_cost[0][1], math.inf # g를 먼저 선택할 경우
    dp['b'][0][0], dp['b'][0][1], dp['b'][0][2] = math.inf, math.inf, rgb_cost[0][2] # b를 먼저 선택할 경우
    
    for i in range(1, n):
        dp['r'][i][0] = min(dp['r'][i-1][1], dp['r'][i-1][2]) + rgb_cost[i][0]
        dp['r'][i][1] = min(dp['r'][i-1][0], dp['r'][i-1][2]) + rgb_cost[i][1]
        dp['r'][i][2] = min(dp['r'][i-1][0], dp['r'][i-1][1]) + rgb_cost[i][2]
        
        dp['g'][i][0] = min(dp['g'][i-1][1], dp['g'][i-1][2]) + rgb_cost[i][0]
        dp['g'][i][1] = min(dp['g'][i-1][0], dp['g'][i-1][2]) + rgb_cost[i][1]
        dp['g'][i][2] = min(dp['g'][i-1][0], dp['g'][i-1][1]) + rgb_cost[i][2]
        
        dp['b'][i][0] = min(dp['b'][i-1][1], dp['b'][i-1][2]) + rgb_cost[i][0]
        dp['b'][i][1] = min(dp['b'][i-1][0], dp['b'][i-1][2]) + rgb_cost[i][1]
        dp['b'][i][2] = min(dp['b'][i-1][0], dp['b'][i-1][1]) + rgb_cost[i][2]
    
    dp['r'][-1][0] = math.inf
    dp['g'][-1][1] = math.inf
    dp['b'][-1][2] = math.inf

if __name__ == "__main__":
    n = int(input()) # 집의 개수 n
    rgb_cost = [ list(map(int, input().split())) for _ in range(n) ] # 각 집을 r, g, b로 칠할 떄의 배용
    
    dp = { # i번째 집까지 칠하는 비용의 최소배용
        'r': [ [ 0, 0, 0 ] for _ in range(n) ],
        'g': [ [ 0, 0, 0 ] for _ in range(n) ],
        'b': [ [ 0, 0, 0 ] for _ in range(n) ],
    }
    # print(dp)
    set_dp(dp, rgb_cost, n)
    # print(dp)
    
    print(min(dp['r'][-1] + dp['g'][-1] + dp['b'][-1]))