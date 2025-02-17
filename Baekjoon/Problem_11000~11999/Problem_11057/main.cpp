#include <cstdio>

const int MAXN = 1000;
const int MOD = 10007;

using namespace std;

int N;
int dp[10][MAXN] = { 0, };

int solve(const int prev=0, const int depth=0) {
    if (depth == N) return 1;

    else if (dp[prev][depth]) return dp[prev][depth];

    for (int i = prev; i < 10; i++) {
        dp[prev][depth] = (dp[prev][depth] + solve(i, depth+1)) % MOD;
    }

    return dp[prev][depth];
}

int main() {
    scanf("%d", &N);

    printf("%d\n", solve());

    return 0;
}