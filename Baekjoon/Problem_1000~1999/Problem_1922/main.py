import  sys

input = lambda: sys.stdin.readline().rstrip()

def kruskal(edges: list[tuple[int, int, int]], V: int) -> int:
    """크루스칼 알고리즘 O(ElogE)"""
    def _union(parents: list[int], x: int, y: int) -> None:
        if x > y:
            parents[x] = y
        else:
            parents[y] = x
    def _find(parents: list[int], x: int) -> int:
        if parents[x] != x:
            parents[x] = _find(parents, parents[x])
        return parents[x]
    
    parents = list(range(V+1))
    cost = 0
    
    for u, v, c in edges:
        u_root, v_root = _find(parents, u), _find(parents, v)
        
        if u_root == v_root: continue
        
        _union(parents, u_root, v_root)
        
        cost += c
    
    return cost

if __name__ == "__main__":
    N = int(input()) # 정점의 개수
    M = int(input()) # 간선의 개수
    
    edges = [ tuple(map(int, input().split())) for _ in range(M) ]
    edges.sort(key=lambda x: x[2])

    print(kruskal(edges, N))