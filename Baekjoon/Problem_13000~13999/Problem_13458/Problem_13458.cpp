#include <cstdio>
#include <cstdint>
#include <cmath>

const int MAXN = 1000000;

using namespace std;

int main() {
    int N; scanf("%d", &N);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);
    int B, C; scanf("%d %d", &B, &C);

    int64_t _sum = 0;
    for (int i = 0; i < N; i++) {
        _sum += 1;
        A[i] -= B;
        if (A[i] > 0) {
            _sum += ceil(static_cast<double>(A[i]) / C);
        }
    }

    printf("%llu\n", _sum);
    
    return 0;
}