#include <cstdio>
#include <algorithm>

const int MAXN = 100000;
using namespace std;

bool compare(const int x, const int y) {
    return x > y;
}

int main() {
    int N; scanf("%d", &N);
    int ropes[N];
    for (int i = 0; i < N; i++) scanf("%d", &ropes[i]);

    sort(ropes, ropes+N, compare);

    int answer = 0;
    for (int i = 0; i < N; i++) {
        answer = max(answer, ropes[i] * (i+1));
    }

    printf("%d\n", answer);

    return 0;
}