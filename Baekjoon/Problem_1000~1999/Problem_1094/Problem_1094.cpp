#include <cstdio>

using namespace std;

int main() {
    int X; scanf("%d", &X);

    int cnt = 0;
    int _sum = 0;
    for (int i = 6; i >= 0; i--) {
        if (_sum == X) break;

        int rest = (1 << i);

        if (_sum + rest <= X) {
            _sum += rest;
            cnt += 1;
        }
    }

    printf("%d\n", cnt);

    return 0;
}