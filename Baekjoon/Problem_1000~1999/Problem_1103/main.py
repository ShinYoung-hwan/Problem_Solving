import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
is_in = lambda r, c: (0 < r <= N) and (0 < c <= M)

dr = [ 0, -1, 0, 1 ]
dc = [ 1, 0, -1, 0 ]

def dfs(r0: int=1, c0: int=1) -> int:
    global visited, n_descendants

    w = ord(board[r0][c0]) - ord('0')
    for i in range(4):
        r, c = r0 + w * dr[i], c0 + w * dc[i]
        
        if not is_in(r, c): continue # 범위 밖으로 벗어난 경우
        elif board[r][c] == 'H': continue # 다음 위치가 hole인 경우
        elif visited[r][c]: return -1 # loop를 식별한 경우
        elif n_descendants[r][c] != 0 and n_descendants[r0][c0] > n_descendants[r][c]: continue # 해당 위치로 이동하는 것이 오히려 부족한 경우

        visited[r][c] = True
        n_child_descendants = dfs(r, c)
        visited[r][c] = False
        if n_child_descendants == -1: return -1
        
        n_descendants[r0][c0] = max(n_descendants[r0][c0], n_child_descendants)
        
    return n_descendants[r0][c0] + 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [ '0' * (M+1) ]
    
    for r in range(N): board.append('0' + input())
    
    visited = [ [ False ] * (M+1) for _ in range(N+1) ] 
    n_descendants = [ [ 0 ] * (M+1) for _ in range(N+1) ] # 현재 위치에서 갈 수 있는 최대 깊이...
    visited[1][1] = True
    print(dfs())