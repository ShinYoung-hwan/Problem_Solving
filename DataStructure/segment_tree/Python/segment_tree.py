
def build(l, r, cur=1):
    global segmentTree
    # base
    if l == r:
        segmentTree[cur] = lst[l]
        return segmentTree[cur]

    # default
    m = (l + r) // 2
    segmentTree[cur] = build(l, m, 2*cur) + build(m+1, r, 2*cur+1)
    return segmentTree[cur]
    
    
def update(l, r, idx, val, cur=1):
    global segmentTree
    # base
    if l == r:
        segmentTree[cur] = val
        return
    
    # default
    m = (l + r) // 2
    if idx <= m:
        update(l, m, idx, val, 2*cur)
    else:
        update(m+1, r, idx, val, 2*cur+1)
    segmentTree[cur] = segmentTree[2*cur] + segmentTree[2*cur+1]
    
def get_partial_sum(l, r, ql, qr, cur=1):
    # base
    # 완전히 벗어난 경우
    if qr < l or r < ql:
        return 0
    # 완전히 포함하는 경우
    elif ql <= l and r <= qr:
        return segmentTree[cur]
    # default
    m = (l + r) // 2
    return get_partial_sum(l, m, ql, qr, 2*cur) + get_partial_sum(m+1, r, ql, qr, 2*cur+1)

if __name__ == "__main__":
    lst = list(range(1, 11))
    segmentTree = [ 0 ] * (4 * len(lst))
    
    build(0, len(lst)-1)
    print(get_partial_sum(0, len(lst)-1, 4, 5))
    
    update(0, len(lst)-1, 4, 15)
    print(get_partial_sum(0, len(lst)-1, 4, 5))
    