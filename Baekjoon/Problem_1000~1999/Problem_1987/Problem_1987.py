import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def dfs(board, R, C, x0, y0, visited:list):
    ans = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[ord(board[y0][x0])-ord('A')] = True
    
    for i in range(4):
        x, y = x0 + dx[i], y0 + dy[i]
        
        if not ((0 <= x < C) and (0 <= y < R)): continue
        if visited[ord(board[y][x])-ord('A')] : continue
        
        visited[ord(board[y][x])-ord('A')] = True
        tmp = dfs(board, R, C, x, y, visited)
        if ans < tmp: ans = tmp
        
        visited[ord(board[y][x])-ord('A')] = False
    
    return ans + 1

if __name__ == "__main__":
    R, C = map(int, input().split()) # 가로 R, 세로 C 크기의 배열
    board = [ list(line.rstrip()) for line in inputs() ]
    
    visited = [ False ] * 26 
    print(dfs(board, R, C, 0, 0, visited))