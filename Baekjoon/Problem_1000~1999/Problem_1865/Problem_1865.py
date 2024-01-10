import sys

inf = int(1e9)

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def solve(graph, n, dist, src=1):
    # 각 모든 정점에 대해서 자기자신으로 돌아올 때 시간이 되돌아가 있는 경우가 있는지 확인
    dist[src] = 0
    
    for check in range(n):
        for cur in range(1, n+1):
            for next, next_weight in graph[cur]:
                if dist[next] > dist[cur] + next_weight:
                    dist[next] = dist[cur] + next_weight
                    if check == n-1: # 음수 사이클 존재
                        return "YES"
    
    return "NO"

if __name__ == "__main__":
    testcase = int(input())
    
    for t in range(testcase):
        n, m, w = map(int, input().split()) # N개의 정점, M개의 양의 간선, W개의 음의 간선
        
        graph = [ [] for _ in range(n+1) ]
        for _ in range(m): # 양의 간선 무방향
            s, e, t = map(int, input().split())
            graph[s].append((e, t))
            graph[e].append((s, t))
        
        for _ in range(w): # 음의 간선 유방향
            s, e, t = map(int, input().split())
            graph[s].append((e, -t))
        
        dist = [ inf ] * (n+1)
        print(solve(graph, n, dist))