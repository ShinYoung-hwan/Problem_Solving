import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve(graph, Ds, in_degree, n, w):
    # n개의 정점을 갖고 있는 graph와 Ds정보에서 w건물을 짓기위한 최소시간 위상정렬 알고리즘을 통해 구하기
    dp = [ 0 ] * (n+1)
    queue = deque()
    
    # 진입차수가 0인 것부터 확인
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = Ds[i]
            
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            dp[next] = max(dp[cur] + Ds[next], dp[next])
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
    
    return dp[w]

if __name__ == "__main__": 
    for T in range(int(input())):
        n, k = map(int, input().split()) # 건물의 개수 n, 건설 순서 규칙 개수 k
        Ds = [ 0 ] + [ int(Di) for Di in input().split() ] # 각 건물을 짓는데 걸리는 시간
        
        graph = [ [] for _ in range(n+1) ] # 그래프 정보
        in_degree = [ 0 ] * (n+1) # 진입차수
        for _ in range(k):
            x, y = map(int, input().split()) # 건설순서 x y
            graph[x].append(y)
            in_degree[y] += 1 # y 정점의 진입차수 +1
        
        w = int(input()) # 목표 건물
        
        print(solve(graph, Ds, in_degree, n, w))