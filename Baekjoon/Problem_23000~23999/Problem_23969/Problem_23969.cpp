#include <cstdio>

using namespace std;

int N, K;
int A[10000];

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

bool bubble_sort() {
    int cnt = 0;
    for (int last = N; last > 0; last--) {
        for (int i = 0; i < last-1; i++) {
            if (A[i] > A[i+1]) {
                swap(A[i], A[i+1]);
                cnt++;

                if (cnt == K) {
                    return true;
                }
            }
        }
    }

    return false;
}

int main() {
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);

    if (!bubble_sort()) {
        printf("-1\n");
    } else {
        for (int i = 0; i < N; i++) 
            printf("%d ", A[i]);
        printf("\n");
    }
    
    return 0;
}