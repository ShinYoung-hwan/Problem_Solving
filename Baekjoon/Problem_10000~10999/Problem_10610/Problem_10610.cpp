#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int MAXN = 100000;

int sum(const char N[MAXN+1], const int size) {
    int _sum = 0;
    for (int i = 0; i < size; i++) {
        _sum += N[i] - '0';
    }
    return _sum;
}

int main() {
    char N[MAXN+1]; scanf("%s", N);
    int size = strlen(N);
    sort(N, N+size, greater<int>());

    if (N[size-1] != '0') {
        printf("-1\n");
    } else if (sum(N, size) % 3 != 0) {
        printf("-1\n");
    } else {
        printf("%s\n", N);
    }

    return 0;
}