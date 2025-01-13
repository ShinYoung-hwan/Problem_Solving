#include <cstdio>
#include <algorithm>

using namespace std;

int N, K;

int solve(const int s, const int e) {
    // base
    if (s == e) return s;

    // default
    const int m = (s + e) / 2;
    int cnt = 0;
    for (int i = 1; i < N + 1; i++) cnt += min(N, m / i);

    return cnt >= K \
        ? solve(0, m) \
        : solve(m+1, e);
}

int main() {
    scanf("%d %d", &N, &K);

    printf("%d\n", solve(0, K));

    return 0;
}