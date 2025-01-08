#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 20000;
int fences[MAXN] = { 0, };

int solve(const int l, const int r) {
    // base
    if (l >= r) return fences[l];

    // default
    int m = (l + r) / 2;
    int ml = m, mr = m+1;
    // left & right
    int ret = max(solve(l, ml), solve(mr, r));

    // mid
    int h = min(fences[ml], fences[mr]);
    ret = max(ret, 2 * h);
    while (l < ml || mr < r) {
        if (mr < r && (l == ml || fences[ml-1] < fences[mr+1])) {
            mr++;
            h = min(h, fences[mr]);
        } else {
            ml--;
            h = min(h, fences[ml]);
        }
        ret = max(ret, h * (mr - ml +1));
    }
    return ret;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);

    for (int t = 0; t < C; t++) {
        int N; scanf("%d", &N);
        for (int i = 0; i < N; i++) scanf("%d", &fences[i]);

        printf("%d\n", solve(0, N-1));
    }

    return 0;
}