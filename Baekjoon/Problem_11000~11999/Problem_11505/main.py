import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_007

def build(l, r, cur=1):
    global segmentTree
    # base
    if l == r:
        segmentTree[cur] = A[l]
        return segmentTree[cur]
    
    # default
    m = (l+r) // 2
    segmentTree[cur] = (build(l, m, 2*cur) * build(m+1, r, 2*cur+1)) % MOD
    return segmentTree[cur]

def update(s, e, idx, val, cur=1):
    global segmentTree
    
    m = (s+e) // 2
    if s == e:
        segmentTree[cur] = val
        return
    
    if idx <= m:
        update(s, m, idx, val, 2*cur)
    else:
        update(m+1, e, idx, val, 2*cur+1)
        
    segmentTree[cur] = (segmentTree[2*cur] * segmentTree[2*cur+1]) % MOD
    
def get_product(s, e, l, r, cur=1):
    # base
    # 구간이 벗어남
    if r < s or l > e:
        return 1
    # 완전히 구간이 포함되어 있음
    if l <= s and e <= r:
        return segmentTree[cur]
    # default
    m = (s+e) // 2
    return (get_product(s, m, l, r, 2*cur) * get_product(m+1, e, l, r, 2*cur+1)) % MOD

if __name__ == "__main__":
    N, M, K = map(int, input().split()) 
    A = [ int(input()) for _ in range(N) ]
    segmentTree = [ 0 ] * (4 * N)
    build(0, N-1)
    
    for _ in range(M+K):
        a, b, c = map(int, input().split())
        
        if a == 1: # update bth clement to c
            update(0, N-1, b-1, c)
            A[b-1] = c
        elif a == 2: # get product b to c
            print(get_product(0, N-1, b-1, c-1))