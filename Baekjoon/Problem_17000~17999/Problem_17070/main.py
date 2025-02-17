import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(house, n):
    # dp[r][c][code] (r, c)로 가는 경로의 수
    # code 1: 가로, code 2: 세로, code 3: 대각선
    dp = [ [ [ 0, 0, 0 ] for _ in range(n+1) ] for _ in range(n+1) ]
    
    dp[1][2][0] = 1 # 
    
    for r in range(1, n+1):
        for c in range(1, n+1):
            
            if house[r][c] == 1: continue
            # (r, c, 0) = (r, c)에 가로로 파이프 설치 경우
            if house[r][c-1] != 1:
                dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
            # (r, c, 1) = (r, c)에 세로로 파이프 설치 경우
            if house[r-1][c] != 1:
                dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
            # (r, c, 2) = (r, c)에 대각선으로 파이프 설치 경우
            if house[r-1][c-1] != 1 and house[r-1][c] != 1 and house[r][c-1] != 1:
                dp[r][c][2] += sum(dp[r-1][c-1])
    
    # for line in dp:
    #     print(line)
    
    return sum(dp[n][n])

if __name__ == "__main__": 
    n = int(input())
    house = [ [ 0 ] * (n+1) ]
    for i in range(n):
        line = [0]
        line.extend(map(int, input().split()))
        house.append(line)
    
    # for line in house:
    #     print(line)
    # print()
    
    print(solve(house, n))