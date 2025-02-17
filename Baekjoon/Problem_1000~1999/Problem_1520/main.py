import sys
sys.setrecursionlimit(10 ** 4)

input = lambda: sys.stdin.readline().rstrip()
isIn = lambda r, c: (0 <= r < R) and (0 <= c < C)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r0=0, c0=0, visited=set()):
    global dp
    # base
    if dp[r0][c0] >= 0:
        return dp[r0][c0]
    
    # default
    cnt = 0
    for i in range(4):
        r, c = r0 + dr[i], c0 + dc[i]
        
        if not isIn(r, c): continue
        if (r, c) in visited:  continue
        if board[r0][c0] <= board[r][c]: continue
        if dp[r][c] == 0: continue
        
        visited.add((r, c))
        cnt += DFS(r, c, visited)
        visited.remove((r, c))
        
    dp[r0][c0] = cnt
    return dp[r0][c0]

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(R) ]
    
    dp = [ [ -1 ] * C for _ in range(R) ]
    dp[R-1][C-1] = 1
    
    DFS()
    
    print(dp[0][0])