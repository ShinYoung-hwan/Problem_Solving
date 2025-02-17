import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve():
    queue = deque()
    
    # 진입차수가 0인 것부터 고려
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        
        for next in graph[cur]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
            
if __name__ == "__main__":
    n, m = map(int, input().split()) # 학생 수 n, 비교 수 m
    
    graph = [ [] for _ in range(n+1) ]
    in_degree = [ 0 ] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    solve()