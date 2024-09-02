#include <cstdio>

const int MAXN = 10000;

using namespace std;

int main() {
    int N, M; scanf("%d %d", &N, &M);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", A+i);

    int cnt = 0;
    int _sum = A[0];
    int l = 0, r = 0;

    while (l < N) {
        if (_sum > M) {
            _sum -= A[l];
            l += 1;
        } else if (_sum < M) {
            if (r == N-1) break;
            r += 1;
            _sum += A[r];
        } else {
            cnt++;
            if (r == N-1) break;
            r += 1;
            _sum = _sum + A[r] - A[l];
            l += 1;
        }
    }

    printf("%d\n", cnt);

    return 0;
}