#include <cstdio>
#include <vector>

const int MAXN = 1000000;

using namespace std;

int main() {
    int N; scanf("%d", &N);
    int A[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);

    // solve
    int NGE[MAXN];
    fill(NGE, NGE+N, -1);
    vector<int> stack;

    for (int i = 0; i < N-1; i++) {
        if (A[i] < A[i+1]) {
            NGE[i] = A[i+1];

            while (!stack.empty() && A[stack.back()] < A[i+1]) {
                NGE[stack.back()] = A[i+1];
                stack.pop_back();
            }
        } else {
            stack.push_back(i);
        }
    }
    
    for (int i = 0; i < N; i++) printf("%d ", NGE[i]);
    printf("\n");

    return 0;
}