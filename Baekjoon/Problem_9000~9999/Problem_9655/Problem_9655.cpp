#include <cstdio>

using namespace std;

int main() {
    int N; scanf("%d", &N);

    printf("%s\n", N & 1 ? "SK" : "CY");

    return 0;
}