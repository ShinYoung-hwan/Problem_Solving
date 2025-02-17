import sys

input = lambda: sys.stdin.readline().rstrip()

def build(l, r, cur=1) -> tuple:
    global segmentTree
    
    if l == r:
        segmentTree[cur] = (A[l], A[l])
        return segmentTree[cur]
    
    mid = (l + r) // 2
    lTree = build(l, mid, 2*cur)
    rTree = build(mid+1, r, 2*cur+1)
    
    segmentTree[cur] = (min(lTree[0], rTree[0]), max(lTree[1], rTree[1]))
    return segmentTree[cur]

def get_min_max(s, e, l, r, cur=1) -> tuple:
    
    if l > e or r < s: 
        return sys.maxsize, 0
    
    if l <= s and e <= r:
        return segmentTree[cur]
    
    mid = (s + e) // 2
    lTree = get_min_max(s, mid, l, r, 2*cur)
    rTree = get_min_max(mid+1, e, l, r, 2*cur+1)
    
    return min(lTree[0], rTree[0]), max(lTree[1], rTree[1])

if __name__ == "__main__":
    N, M = map(int, input().split()) # 정수의 개수 N, (l, r)의 쌍의 개수 M
    A = [ int(input()) for _ in range(N) ]
    
    segmentTree = [ (sys.maxsize, 0) ] * (4 * N) # list[(min, max)]
    build(0, N-1)
    
    for _ in range(M):
        l, r = map(int, input().split())
        print(*get_min_max(0, N-1, l-1, r-1))