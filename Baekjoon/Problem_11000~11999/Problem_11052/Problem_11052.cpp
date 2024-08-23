#include <cstdio>
#include <algorithm>

const int MAXN = 1000;

using namespace std;

int main() {
    int N; scanf("%d", &N);

    int P[MAXN]; 
    for (int i = 0; i < N; i++) scanf("%d", &P[i]);

    int maxp[MAXN+1] = { 0, };
    for (int i = 1; i <= N; i++) {
        maxp[i] = P[i-1];

        for (int j = 0; j <= i / 2; j++) {
            maxp[i] = max(maxp[i], maxp[j] + maxp[i-j]);
        }
    }

    printf("%d\n", maxp[N]);

    return 0;
}