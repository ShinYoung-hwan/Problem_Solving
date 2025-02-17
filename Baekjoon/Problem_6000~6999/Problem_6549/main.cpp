#include <cstdio>
#include <cstdint>
#include <algorithm>

using namespace std;
const int MAXN = 100000;
int64_t hist[MAXN] = { 0, };

int64_t solve(const int l, const int r) {
    // base
    if (l >= r) return hist[l];

    // default
    int m = (l + r) / 2;
    int ml = m, mr = m+1;
    // left & right
    int64_t ret = max(solve(l, ml), solve(mr, r));

    // mid
    int64_t h = min(hist[ml], hist[mr]);
    ret = max(ret, 2 * h);
    while (l < ml || mr < r) {
        if (mr < r && (l == ml || hist[ml-1] < hist[mr+1])) {
            mr++;
            h = min(h, hist[mr]);
        } else {
            ml--;
            h = min(h, hist[ml]);
        }
        ret = max(ret, h * (mr - ml +1));
    }
    return ret;
}

int main() {
    while (true) {
        int N; scanf("%d", &N);
        if (N == 0) break;

        for (int i = 0; i < N; i++) scanf("%lld", &hist[i]);
        printf("%lld\n", solve(0, N-1));
    }
    
    return 0;
}