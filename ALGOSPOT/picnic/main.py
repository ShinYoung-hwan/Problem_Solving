import sys

input = lambda: sys.stdin.readline().rstrip()

def get_min_visited(visited: list):
    for i in range(n):
        if not visited[i]: return i

def search(me: int, toPairs: int):
    global cnt
    if not toPairs: 
        cnt += 1
        return
    
    visited[me] = True
    for friend in graph[me]:
        if visited[friend]: continue
        
        visited[friend] = True
        
        search(get_min_visited(visited), toPairs-1)
        
        visited[friend] = False
    visited[me] = False
    
if __name__ == "__main__":
    C = int(input())
    
    for t in range(C):
        n, m = map(int, input().split()) # 학생 수 n, 짝꿍 수 m
        
        graph = [ set() for _ in range(n) ]
        friends = list(map(int, input().split()))
        for i in range(0, 2*m, 2):
            u, v = friends[i], friends[i+1]
            graph[u].add(v)
            graph[v].add(u)
            
        visited = [ False ] * n
        cnt = 0
        search(0, n//2)
        
        print(cnt)
