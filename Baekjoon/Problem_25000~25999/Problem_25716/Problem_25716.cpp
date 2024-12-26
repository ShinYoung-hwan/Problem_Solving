#include <cstdio>

using namespace std;

int factorial(const int n) {
    int _prod = 1;
    for (int i = 1; i <= n; i++) _prod *= i;
    return _prod;
}

int main() {
    int N; scanf("%d", &N);
    printf("%d\n", factorial(N));
    return 0;
}