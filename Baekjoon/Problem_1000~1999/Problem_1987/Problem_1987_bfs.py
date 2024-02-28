import sys

input = lambda: sys.stdin.readline().rstrip()

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

def bfs(r0, c0):
    res = 1
    queue = {(r0, c0, board[r0][c0])}
    
    while queue:
        r0, c0, visited = queue.pop()
        
        for i in range(4):
            r, c = r0 + dr[i], c0 + dc[i]
            
            if not ((0 <= r < R) and (0 <= c < C)): continue
            if board[r][c] in visited: continue
            
            queue.add((r, c, visited + board[r][c]))
            res = max(res, len(visited) + 1)
            
    return res
        
if __name__ == "__main__":
    R, C = map(int, input().split()) # 행렬의 크기 (r, c)
    board = [ input() for _ in range(R) ]
    
    print(bfs(0, 0))