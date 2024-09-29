#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
const int MAXN = 10;

int N, M;
int A[MAXN];

void solve(vector<int> &sequence, const int start=0) {
    // base
    if (sequence.size() == M) {
        for (auto e: sequence) {
            printf("%d ", e);
        }
        printf("\n");
        return;
    }

    // default
    for (int i = start; i < N; i++) {
        sequence.push_back(A[i]);
        solve(sequence, i+1);
        sequence.pop_back();
    }
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) scanf("%d", &A[i]);
    sort(A, A+N);

    vector<int> sequence;
    solve(sequence);

    return 0;
}