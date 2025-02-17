#include <cstdio>
#include <algorithm>

const int MAXN = 200000;

using namespace std;

bool is_valid_distance(const int houses[MAXN], const int N, const int distance, const int C) {
    int cnt = 1;
    int prev = houses[0];
    for (int i = 1; i < N; i++) {
        int cur = houses[i];
        if (cur - prev >= distance) {
            cnt += 1;
            prev = cur;
        }

        if (cnt == C) return true;
    }

    return false;
}

int main() {
    int N, C; scanf("%d %d", &N, &C);
    int houses[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", houses+i);
    sort(houses, houses+N);

    int l = 0, r = houses[N-1];

    int ans = 0;
    while (l <= r) {
        int m = (l + r) / 2;

        if (is_valid_distance(houses, N, m, C)) {
            ans = m;
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    printf("%d\n", ans);

    return 0;
}