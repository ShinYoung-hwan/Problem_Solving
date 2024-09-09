#include <cstdio>
#include <set>
#include <algorithm>

const int MAXN = 100;
const int MAXK = 10000;

using namespace std;

int main() {
    int N, K; scanf("%d %d", &N, &K);
    set<int> coins;
    for (int i = 0; i < N; i++) {
        int coin; scanf("%d", &coin);
        coins.insert(coin);
    }
    
    int dp[MAXK+1] = { 0 };
    fill(dp+1, dp+K+1, MAXK+1);

    for (int coin: coins) {
        for (int i = coin; i <= K; i++) {
            dp[i] = min(dp[i], dp[i-coin]+1);
        }
    }
    
    printf("%d", dp[K] == MAXK+1 ? -1 : dp[K]);
    
    return 0;
}