import sys

input = lambda: sys.stdin.readline().rstrip()

dr = [ -1, 1, 0, 0 ]
dc = [ 0, 0, -1, 1 ]

def get_alphabet_order(alphabet):
    return ord(alphabet) - ord('A')

def dfs(r0, c0, visited, depth=1):
    global res
    
    for i in range(4):
        r, c = r0 + dr[i], c0 + dc[i]
        
        if not ((0 <= r < R) and (0 <= c < C)): continue
        if visited[get_alphabet_order(board[r][c])]: continue
        
        visited[get_alphabet_order(board[r][c])] = True
        res = max(res, depth+1)
        dfs(r, c, visited, depth+1)
        visited[get_alphabet_order(board[r][c])] = False
        

if __name__ == "__main__":
    R, C = map(int, input().split()) # 행렬의 크기 (r, c)
    board = [ input() for _ in range(R) ]
    
    res = 1
    visited = [ False ] * 26 # 알파벳 개수
    visited[get_alphabet_order(board[0][0])] = True
    dfs(0, 0, visited)
    
    print(res)