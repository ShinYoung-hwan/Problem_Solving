#include <cstdio>
#include <cstring>

const int MAXN = 1000;
const int MOD = 10007;

using namespace std;

int dp[MAXN][MAXN];

int comb(const int N, const int K) {
    if (K == N) return 1;
    else if (K == 0) return 1;

    if (!dp[N][K]) {
        dp[N][K] = (comb(N-1, K-1) + comb(N-1, K)) % MOD;
    }

    return dp[N][K];
}

int main() {
    int N, K; scanf("%d %d", &N, &K);
    memset(dp, 0, sizeof(dp));

    printf("%d\n", comb(N, K));

    return 0;
}