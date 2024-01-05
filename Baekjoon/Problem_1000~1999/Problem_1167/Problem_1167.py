import sys
sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()  

def dfs(cur, res=0):
    global graph, visited
    for next, weight in graph[cur]:
        if visited[next] >= 0:
            continue
        
        visited[next] = res + weight
        dfs(next, visited[next])
            
    
if __name__ == "__main__":
    n = int(input()) # 노드의 개수
    
    # 그래프 저장
    graph = [ [] for _ in range(n+1) ]
    for _ in range(n): # 인접 그래프 형태의 그래프
        edge_info = list(map(int, input().split()))
        for i in range(1, len(edge_info), 2):
            if edge_info[i] == -1:
                break
            graph[edge_info[0]].append((edge_info[i], edge_info[i+1]))
    
    # 그래프 탐색
    visited = [ -1 ] * (n+1)
    visited[1] = 0
    dfs(1)
    start = visited.index(max(visited))
    visited = [ -1 ] * (n+1)
    visited[start] = 0
    dfs(start)
    
    print(max(visited))