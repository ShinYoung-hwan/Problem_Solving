import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in(x, y, w, h):
    return (0 <= x < w) and (0 <= y < h)

def get_start_pos(campus, w, h):
    # 가로 w, 높이 h인 캠퍼스에서 I 찾기
    for y in range(h):
        for x in range(w):
            if campus[y][x] == 'I':
                return x, y
    
def bfs(campus, w, h, sx, sy):
    # 가로 w, 높이 h인 캠퍼스에서 sx, sy 위치에서 시작해 상하좌우로 이동하며 사람 수 찾기
    res = 0
    queue = deque()
    queue.append((sx, sy))
    campus[sy][sx] = 'X'
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while len(queue):
        cx, cy = queue.popleft()
        
        for i in range(4):
            x, y = cx + dx[i], cy + dy[i]
            
            if not is_in(x, y, w, h):
                continue
            if campus[y][x] == 'X':
                continue

            
            if campus[y][x] == 'P':
                res += 1
            queue.append((x, y))
            campus[y][x] = 'X'
    
    res = 'TT' if res == 0 else res
    return res

if __name__ == "__main__":
    n, m = map(int, input().split()) # 세로n, 가로m 크기릐 캠퍼스
    campus = [ list(line.rstrip()) for line in inputs() ] # O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐
    sx, sy = get_start_pos(campus, m, n) # 'I'의 위치
    
    print(bfs(campus, m, n, sx, sy))
    
    