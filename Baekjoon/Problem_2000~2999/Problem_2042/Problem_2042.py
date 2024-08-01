import sys

input = lambda: sys.stdin.readline().rstrip()

def build(l, r, cur=1):
    """ segmenTree를 A의 원소로 채운다. """
    global segmentTree
    
    if l == r: 
        segmentTree[cur] = A[l]
        return segmentTree[cur]

    m = (l+r) // 2
    segmentTree[cur] = build(l, m, 2*cur) + build(m+1, r, 2*cur+1)
    return segmentTree[cur]

def update(l, r, cur, idx, v):
    """ tree의 구간 [s, e]에서 idx번째에 해당하는 값을 v 값만큼 변경한다. """
    global segmentTree
    if l > idx or r < idx:
        return segmentTree[cur]
    
    segmentTree[cur] += v
    if l != r:
        m = (l+r) // 2
        update(l, m, 2*cur, idx, v)
        update(m+1, r, 2*cur+1, idx, v)
    
def sum_tree(s, e, cur, l, r):
    """ tree의 구간 [s, e]
        합해야하는 구간 [l, r]
    """
    # 범위를 벗어난 경우
    if l > e or r < s:
        return 0
    # 포함되는 경우
    elif l <= s and r >= e:
        return segmentTree[cur]
    
    m = (s+e) // 2
    return sum_tree(s, m, 2*cur, l, r) + sum_tree(m+1, e, 2*cur+1, l, r)

if __name__ == "__main__":
    N, M, K = map(int, input().split()) # 배열의 길이 N, M+K회의 변경횟수
    segmentTree = [ 0 ] * (4 * N)
    
    # store
    A = [ int(input()) for _ in range(N) ]
    build(0, N-1)
    # print(segmentTree)
    
    # solve
    for _ in range(M+K):
        a, b, c = map(int, input().split())

        if a == 1:
            # b(1 ≤ b ≤ N)번째 수를 c로 바꾸기
            update(0, N-1, 1, b-1, c - A[b-1])
            A[b-1] = c
        elif a == 2:
            # b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력
            print(sum_tree(0, N-1, 1, b-1, c-1))
    