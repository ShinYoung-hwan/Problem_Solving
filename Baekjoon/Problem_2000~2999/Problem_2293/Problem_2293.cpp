#include <cstdio>

const int MAXN = 100;
const int MAXK = 10000;

using namespace std;

int main() {
    int n, k; scanf("%d %d", &n, &k);

    int coins[MAXN];
    for (int i = 0; i < n; i++) scanf("%d", &coins[i]);

    int dp[MAXK+1] = { 0, };
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        int coin = coins[i];

        for (int j = coin; j <= k; j++) {
            dp[j] += dp[j-coin];
        }
    }

    
    printf("%d\n", dp[k]);

    return 0;
}