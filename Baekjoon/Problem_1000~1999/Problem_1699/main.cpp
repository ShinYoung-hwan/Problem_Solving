#include <cstdio>
#include <cstdint>
#include <vector>
#include <algorithm>

const int MAXN = 100000;

using namespace std;

int main() {
    int N; scanf("%d", &N);

    int dp[MAXN+1];
    fill(dp, dp+MAXN, INT32_MAX / 2);
    dp[1] = 1;

    vector<int> squares;
    for (int i = 1; i * i <= N; i++) {
        squares.push_back(i * i);
        dp[i * i] = 1;
    }

    for (int i = 2; i <= N; i++) {
        dp[i] = min(dp[i], dp[i-1]+1);
        for (int square: squares) {
            if (i < square) break;
            dp[i] = min(dp[i], dp[square] + dp[i-square]);
        }
    }

    printf("%d\n", dp[N]);

    return 0;
}