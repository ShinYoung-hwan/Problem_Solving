#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;
const int MAXN = 8;

int main() {
    int N; scanf("%d", &N);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);

    int answer = 0;
    int idx_array[MAXN];
    for (int i = 0; i < N; i++) idx_array[i] = i;
    do {
        int _sum = 0;
        for (int *it = idx_array; it != idx_array+N-1; it++) {
            _sum += abs(A[*it] - A[*(it+1)]);
        }
        answer = max(answer, _sum);
    } while (next_permutation(idx_array, idx_array+N));

    printf("%d\n", answer);

    return 0;
}