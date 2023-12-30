import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()

def get_n_connected_component(graph, n):
    # n 개의 정점으로 이루어진 그래프에서 연결 요소 개수 구하기
    visited = [ False ] * (n+1)
    n_connected_component = 0
    
    for i in range(1, n+1):
        if visited[i]: continue
        
        queue = deque([i])
        n_connected_component += 1
        
        while len(queue) > 0:
            cur = queue.popleft()
            
            for next in graph[cur]:
                if visited[next]: continue

                queue.append(next)
                visited[next] = True
    return n_connected_component

if __name__ == "__main__":
    n, m = map(int, input().split()) # n개의 정점, m개의 간선
    graph = [ set() for _ in range(n+1) ]
    
    for _ in range(m): # m개의 간선 입력 받기
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
        
    print(get_n_connected_component(graph, n))