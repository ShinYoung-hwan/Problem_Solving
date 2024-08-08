import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def is_bidivisible(graph, visited, start=1):
    """ BFS를 기반으로 탐색 O(V+E) """
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        cur = queue.popleft()
        
        for next in graph[cur]:
            
            if visited[next] >= 0: 
                if (visited[cur] & 1) == (visited[next] & 1):
                    return False
                continue
            
            queue.append(next)
            visited[next] = visited[cur] + 1
            
    return True

if __name__ == "__main__":
    for test_case in range(int(input())):
        V, E = map(int, input().split())
        
        graph = [ [] for _ in range(V+1) ]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        
        """ IDEA: 각 vertex에 홀수와 짝수를 부여하면서 홀수끼리 인접하거나 짝수끼리 인접하면 False """
        answer = True
        visited = [ -1 ] * (V+1)
        for i in range(1, V+1):
            if visited[i] >= 0: continue # skip searched space
            
            if not is_bidivisible(graph, visited, i):
                answer = False
                break
        
        print("YES" if answer else "NO")