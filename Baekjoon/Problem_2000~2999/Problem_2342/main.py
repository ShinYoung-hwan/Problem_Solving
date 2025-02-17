import sys

MAX = 500_000

input = lambda: sys.stdin.readline().rstrip()

# costs[i][j] i에서 j로 발을 옮길때의 드는 비용
costs = [
    [1, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]

def solve(cmds, n):
    if n == 0: return 0
    
    dp = [ [ [ MAX ] * 5 for _ in range(5) ] for _ in range(n+1) ] # dp[i][l][r] i번째에서 (l, r)을 밟을 때 총 소요된 힘
    dp[-1][0][0] = 0 # 시작 index로 -1을 부여
    
    for i in range(n):
        cmd = cmds[i]
        # 왼쪽발을 움직일 때
        for r in range(5): # 각 오른발을 고정시키고
            for k in range(5): # 이전 왼발을 기준으로 해결한다
                dp[i][cmd][r] = min(dp[i][cmd][r], dp[i-1][k][r] + costs[k][cmd])
                
        # 오른쪽발을 움직일 때
        for l in range(5): # 각 왼발을 고정시키고
            for k in range(5): # 이전 오른발을 기준으로 해결한다.
                dp[i][l][cmd] = min(dp[i][l][cmd], dp[i-1][l][k] + costs[k][cmd])
                
    # 결과 출력
    res = MAX
    for l in range(5):
        for r in range(5):
            res = min(res, dp[n-1][l][r])
    return res

if __name__ == "__main__":
    cmds = list(map(int, input().split())) # 들어오는 커맨드 cmds
    n = len(cmds) - 1
    
    print(solve(cmds, n))