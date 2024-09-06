#include <cstdio>
#include <algorithm>

const int MAXN = 1000;

using namespace std;

int main() {
    int N; scanf("%d", &N);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", A+i);

    // solve
    int dp[MAXN];
    fill(dp, dp+N, 1);

    for (int i = 1; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (A[i] < A[j]) {
                dp[i] = max(dp[i], dp[j]+1);
            }
        }
    }
        
    printf("%d\n", *max_element(dp, dp+N));

    return 0;
}