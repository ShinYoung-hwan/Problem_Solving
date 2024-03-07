import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def topology_sort(graph, in_degree, N):
    # 위상 정렬을 이용해 가수들의 공연 순서를 선후관계를 고려해 짠다.
    queue = deque()
    
    # 진입차수가 0인 것부터 고려
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    
    res = [  ]
    while queue:
        cur = queue.popleft()
        res.append(cur)
        
        for next in graph[cur]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
        
    return res if len(res) == N else [ 0 ]

if __name__ == "__main__":
    N, M = map(int, input().split()) # 가수의 수 n, 보조 pd의 수 m
    
    # 선후 관계 그래프 
    graph = [ [ ] for _ in range(N+1) ]
    in_degree = [ 0 ] * (N+1)
    for _ in range(M):
        tmp = list(map(int, input().split()))
        n, singers = tmp[0], tmp[1:] # 각 pd의 담당 가수의 수 n, 담당 가수 singers
        
        for i in range(n-1):
            a, b = singers[i], singers[i+1]
            graph[a].append(b)
            in_degree[b] += 1
    
    # 위상 정렬 결과를 출력
    for e in topology_sort(graph, in_degree, N):
        print(e)