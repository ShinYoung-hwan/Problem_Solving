#include <cstdio>
#include <algorithm>

using namespace std;
const int MAXN = 1000000;

int zero_cnt = 0;
int one_cnt = 0;

void update_cnt(const int s) {
    if (s == '0') zero_cnt++;
    else one_cnt++;
}

int main() {
    char S[MAXN+1]; scanf("%s", S);

    char prev = S[0];
    update_cnt(prev);

    for (int i = 1; S[i] != '\0'; i++ ) {
        char s = S[i];
        if (prev == s) continue;

        update_cnt(s);
        prev = s;
    }

    printf("%d\n", min(zero_cnt, one_cnt));

    return 0;
}