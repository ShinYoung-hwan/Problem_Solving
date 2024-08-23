#include <cstdio>
#include <string>
#include <algorithm>

const int MAXN = 7;
const int MAXCNT = 10;

using namespace std;

int main() {
    char N[MAXN+1]; scanf("%s", N);
    string strN = string(N);

    int counts[MAXCNT] = { 0, };

    for (char n: strN) {
        int cur = n - '0';

        // 6 and 9 balancing
        if (cur == 6 || cur == 9) {
            if (counts[6] > counts[9]) cur = 9;
            else cur = 6;
        }

        counts[cur]++;
    }

    printf("%d\n", *max_element(counts, counts+MAXCNT));

    return 0;
}