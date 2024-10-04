#include <cstdio>

using namespace std;

int main() {
    int T; scanf("%d", &T);
    int rest_alphas[6] = { 0, 2, 2, 4, 3, 5 };

    for (int t = 0; t < T; t++) {
        int N; scanf("%d", &N);

        int rest = N % 6;
        int division = N / 6;
        int base = 5 * division;

        printf("%d\n", base + rest_alphas[rest]);
    }

    return 0;
}