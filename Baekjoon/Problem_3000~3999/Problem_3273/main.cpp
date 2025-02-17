#include <cstdio>
#include <algorithm>

using namespace std;
const int MAXN = 100000;

int main() {
    int N; scanf("%d", &N);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);
    int X; scanf("%d", &X);

    sort(A, A+N);

    int answer = 0;
    int l = 0, r = N-1;
    while (l < r) {
        int _sum = A[l] + A[r];
        if (_sum == X) {
            answer++;
            l++;
            r--;
        } else if (_sum > X) {
            r--;
        } else {
            l++;
        }
    }

    printf("%d\n", answer);

    return 0;
}