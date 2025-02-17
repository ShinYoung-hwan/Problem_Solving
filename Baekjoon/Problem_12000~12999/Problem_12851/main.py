import sys
from collections import deque

SIZE = 100_001

input = lambda: sys.stdin.readline().rstrip()

def bfs(src, dest):
    # src -> dest
    visited = [ 0 ] * SIZE
    queue = deque([src])
    
    cnt, res = 0, 0
    while queue:
        cur = queue.popleft()
        tmp = visited[cur]
        
        if cur == dest: # 만난경우
            res = tmp
            cnt += 1
            continue
        
        for next in [ cur-1, cur+1, 2*cur ]:
            if not (0 <= next < SIZE): continue # 범위가 유효한지 확인
            if not (visited[next] == 0 or visited[next] == visited[cur] + 1): continue # 초회 방문이나 최적케이스가 아닌 경우

            visited[next] = visited[cur] + 1
            queue.append(next)
    
    return ''.join([str(res), '\n', str(cnt)])
    
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    
    print(bfs(n, k))