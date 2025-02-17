import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def bfs(movers, src, dest):
    visited = [ False ] * (dest + 1)
    queue = deque([(src, 0)])
    visited[src] = True
    
    dice = [1, 2, 3, 4, 5, 6]
    
    while len(queue) > 0:
        cur, cnt = queue.popleft() # 현재 위치와 던진 주사위 횟수

        if cur == dest: break
        
        for d in dice:
            next = cur + d
            
            if next > dest: continue
            if visited[next]:
                continue
            
            if next in movers:
                next = movers[next]
            
            visited[next] = True
            queue.append((next, cnt + 1))
    
    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split()) # n개의 사다리, m개의 뱀
    
    movers = dict() # key -> value 이동
    
    for u, v in [ map(int, move.split()) for move in inputs() ]:
        movers[u] = v
        
    print(bfs(movers, 1, 100))
    
    