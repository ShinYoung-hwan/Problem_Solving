import sys

input = lambda: sys.stdin.readline().rstrip()

def kruskal():
    # 크루스칼 알고리즘
    def _find(parents, x):
        if x != parents[x]:
            parents[x] = _find(parents, parents[x])
        return parents[x]
    
    def _union(parents, x, y):
        if x > y:
            parents[x] = y
        else:
            parents[y] = x
        
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    
    # 루트노드를 저장하는 부모 표시 parents 리스트 생성
    parents = list(range(V+1))
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().split()) # 간선 (a, b, c)
        edges.append((a, b, c))
    # 간선들을 가중치를 기준으로 정렬
    edges.sort(key=lambda x: x[2])
    
    res = 0
    for a, b, c in edges:
        # 간선이 이은 두 정점의 루트노드를 찾는다.
        a_root = _find(parents, a)
        b_root = _find(parents, b)
        
        if a_root == b_root: continue # 이미 하나가 되어 있음
        
        # 두 루트노드가 다르다면 큰쪽을 작은쪽에 포함시킨다.
        _union(parents, a_root, b_root)
        # 가중치를 더한다.
        res += c
        
    return res

def prim():
    import heapq
    # 프림 알고리즘
    V, E = map(int, input().split()) # 정점의 개수 V, 간선의 개수 E
    
    graph = [ [] for _ in range(V+1) ]
    for _ in range(E):
        a, b, c = map(int, input().split()) # 간선 (a, b, c)
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    heap = []
    visited = [ False ] * (V+1)
    heapq.heappush(heap, (0, 1))
    
    res = 0
    cnt = 0
    while heap:
        if cnt == V: break
        cur_weight, cur = heapq.heappop(heap)
        
        if visited[cur]: continue
        
        for next, next_weight in graph[cur]:
            heapq.heappush(heap, (next_weight, next))
        res += cur_weight
        cnt += 1
        visited[cur] = True
        
    return res
                
if __name__ == "__main__":     
    # 최소 스패닝 트리의 가중치를 출력
    # print(kruskal())
    print(prim())