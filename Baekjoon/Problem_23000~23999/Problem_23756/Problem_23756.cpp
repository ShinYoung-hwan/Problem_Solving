#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int N; scanf("%d", &N);
    int A[100]; for (int i = 0; i <= N; i++) scanf("%d", &A[i]);

    int _sum = 0;
    for (int i = 0; i < N; i++) {
        _sum += min(abs(A[i] - A[i+1]), min(abs(A[i] + 360 - A[i+1]), abs(A[i] - A[i+1] - 360)));
    }
    
    printf("%d\n", _sum);
    
    return 0;
}