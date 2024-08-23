#define N 1000

typedef int Item;

Item segmentTree[4 * N];

/* build segment tree, O(NlogN) */
Item build(const int arr[], const int l, const int r, const int cur) {
    // base
    if (l == r) {
        return segmentTree[cur] = arr[l];
    }

    // default
    int m = (l + r) / 2;
    return segmentTree[cur] = build(arr, l, m, 2*cur) + build(arr, m+1, r, 2*cur+1);
}

/* build segment tree's element, O(logN) */
void update(const int l, const int r, const int idx, const int val, const int cur) {
    // base
    if (l == r) {
        segmentTree[cur] = val;
        return;
    }

    // default
    int m = (l + r) / 2;
    if (idx <= m) {
        update(l, m, idx, val, 2*cur);
    } else {
        update(m+1, r, idx, val, 2*cur+1);
    }
    segmentTree[cur] = segmentTree[2*cur] + segmentTree[2*cur+1];
}

/* get partial sum, O(logN) */
Item get_partial_sum(const int l, const int r, const int ql, const int qr, const int cur) {
    // base
    // 범위를 완전히 벗어난 경우
    if (qr < l || r < ql) {
        return 0;
    } 
    // 범위가 완전히 포함되는 경우
    else if (ql <= l && r <= qr) {
        return segmentTree[cur];
    }

    // default
    int m = (l + r) / 2;
    return get_partial_sum(l, m, ql, qr, 2*cur) + get_partial_sum(m+1, r, ql, qr, 2*cur+1);
}

void print_segment_tree() {
    for (int i = 0; i < 4 * 10; i++) {
        printf("%d ", segmentTree[i]);
    }
    printf("\n");
}