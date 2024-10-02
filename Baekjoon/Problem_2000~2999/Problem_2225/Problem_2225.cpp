#include <cstdio>
#include <algorithm>

using namespace std;
const int MOD = 1000000000;
const int MAXN = 200;

int dp[MAXN+1][MAXN+1];

int solve(const int n, const int k) {
    // dp base
    if (dp[n][k] >= 0) return dp[n][k];

    // recursion base
    else if (k == 0) {
        dp[n][k] = (n == 0);
        return dp[n][k];
    }

    // recursion default
    dp[n][k] = 0;
    for (int i = 0; i <= n; i++) {
        dp[n][k] = (dp[n][k] + solve(n-i, k-1)) % MOD;
    }
    return dp[n][k];
}

int main() {
    int N, K; scanf("%d %d", &N, &K);

    for (int r = 0; r <= N; r++) {
        fill(dp[r], dp[r]+K+1, -1);
    }

    printf("%d\n", solve(N, K));

    return 0;
}