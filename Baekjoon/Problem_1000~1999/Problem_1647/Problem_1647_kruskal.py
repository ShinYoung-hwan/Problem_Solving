import sys

input = lambda: sys.stdin.readline().rstrip()

def find(parents, x):
    if parents[x] != x:
        return find(parents, parents[x])
    return x

def union(parents, x, y):
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

def kruskal(edges, n):
    # 크루스칼 알고리즘
    parents = list(range(n+1))
    
    res = []
    for a, b, c in edges:
        a_root = find(parents, a)
        b_root = find(parents, b)
        
        if a_root == b_root: continue # 같은 부모
        
        union(parents, a_root, b_root)
        res.append(c)
    
    return res

if __name__ == "__main__":
    n, m = map(int, input().split()) # 집의 개수 n, 길의 개수 m
    
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split()) # 가중 길 (a, b, c)
        edges.append((a, b, c))
    
    edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 정렬
    
    res = kruskal(edges, n)
    res.pop() # 최대 가중치 제거
    print(sum(res))