#include <cstdio>

using namespace std;

int main() {
    int K, C; scanf("%d %d", &K, &C);
    
    for (int i = 0; i < C; i++) {
        int M, N; scanf("%d %d", &M, &N);
        if (M == N) {
            printf("%d\n", 1);
        } else if (M > N) {
            printf("%d\n", 2*M - N - K <= 2);
        } else { // M < N
            printf("%d\n", 2*N - M - K <= 1);
        }
    }
    
    return 0;
}