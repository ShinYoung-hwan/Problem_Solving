import sys

sys.setrecursionlimit(10**5)

input = lambda: sys.stdin.readline().rstrip()

def find(parents, x):
    if x != parents[x]:
        parents[x] = find(parents, parents[x])
        return parents[x]
    return x

def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    
    if x > y:
        parents[x] = y
    else:
        parents[y] = x
        
def solve(selections, m):
    parents = list(range(n))
    cnt = 0
    for i in range(m):
        u, v = selections[i]
        cnt += 1
        if find(parents, u) == find(parents, v):
            return cnt
        
        union(parents, u, v)
        
    return 0

if __name__ == "__main__":
    n, m = map(int, input().split()) # 점의 개수 n, 차례의 수 m
    
    selections = [tuple(map(int, input().split())) for _ in range(m) ]
    
    print(solve(selections, m))
