import sys
import math

input: lambda: sys.stdin.readline().rstrip()

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
    
    # 루트노드를 저장하는 부모 표시 parents 리스트 생성
    parents = list(range(n+1))
    
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
        
    return round(res, 2)

if __name__ == "__main__":
    n = int(input()) # 별의 개수 n
    
    stars = [ tuple(map(float, input().split())) for _ in range(n) ]
    
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            d = round(math.sqrt( (x2 - x1) ** 2 + (y2 - y1) **2 ), 3)
            edges.append((i, j, d))
    edges.sort(key=lambda x: x[2])
    
    print(kruskal())
    