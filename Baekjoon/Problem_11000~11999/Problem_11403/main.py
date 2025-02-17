import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_has_path_i2j(graph, n, i, j):
    # 정점 i 에서 정점 j로 가는 경로가 있는지 없는지
    queue = deque([ k for k in range(n) if graph[i][k] == 1 ])
    visited = [ 1 if (k in queue) else 0 for k in range(n) ]
    
    while len(queue) > 0:
        cur = queue.popleft()
        if cur == j:
            return 1
        
        for k in range(n):
            if visited[k]:
                continue
            
            if graph[cur][k] == 1:
                queue.append(k)
                visited[k] = 1
    return 0

if __name__ == "__main__":
    n = int(input())
    graph = [ [ int(item) for item in line.split() ] for line in inputs() ]
    
    for i in range(n):
        for j in range(n):
            print(is_has_path_i2j(graph, n, i, j), end=' ')
        
        print()
            