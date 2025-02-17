#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 10000;
int N;
int request_budgets[MAXN] = { 0, };
int budget;

bool is_valid(const int m) {
    int _sum = 0;
    for (int i = 0; i < N; i++) {
        _sum += ( request_budgets[i] <= m ? request_budgets[i] : m );
    }

    return _sum <= budget;
}

int solve(int s, int e) {
    int m = (s + e) / 2;

    while (s <= e) {
        if (is_valid(m)) {
            s = m + 1;
        } else {
            e = m - 1;
        }
        m = (s + e) / 2;
    }
    return m;
}

int main() {
    int _sum = 0, _max = 0, tmp;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &tmp);
        _sum += tmp;
        _max = max(_max, tmp);
        request_budgets[i] = tmp;
    }
    scanf("%d", &budget);

    if (_sum <= budget) {
        printf("%d\n", _max);
    } else {
        printf("%d\n", solve(0, _max));
    }

    return 0;
}