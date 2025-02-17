import sys

input = lambda: sys.stdin.readline().rstrip()

def build(l, r, cur=1):
    global segmentTree
    if l == r:
        segmentTree[cur] = A[l]
        return segmentTree[cur]
    
    m = (l + r) // 2
    segmentTree[cur] = build(l, m, 2*cur) + build(m+1, r, 2*cur+1)
    return segmentTree[cur]

def update(s, e, idx, v, cur=1):
    global segmentTree
    # base case
    if s == e:
        segmentTree[cur] = v
        return
        
    # default case
    m = (s+e) // 2
    if (idx <= m):
        update(s, m, idx, v, 2*cur)
    else:
        update(m+1, e, idx, v, 2*cur+1)
        
    segmentTree[cur] = segmentTree[2*cur] + segmentTree[2*cur+1]
    
def get_sum(s, e, l, r, cur=1):
    # base case
    # 범위를 벗어난 경우
    if r < s or l > e:
        return 0
    # 범위에 온전히 포함되는 경우
    elif l <= s and e <= r:
        return segmentTree[cur]
    # default case
    m = (s+e) // 2
    return get_sum(s, m, l, r, 2*cur) + get_sum(m+1, e, l, r, 2*cur+1)

if __name__ == "__main__":
    N, Q = map(int, input().split()) # 정수의 개수 N, 쿼리의 개수 Q
    A = list(map(int, input().split()))
    segmentTree = [ 0 ] * (4 * N)
    build(0, N-1)
    
    # Q개의 쿼리 수행
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        
        # x ~ y의 구간 합
        if x > y: x, y = y, x
        print(get_sum(0, N-1, x-1, y-1))
        
        # a번째 숫자를 b로 교체
        update(0, N-1, a-1, b)
        