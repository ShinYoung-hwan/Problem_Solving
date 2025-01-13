#include <cstdio>
#include <vector>

using namespace std;

int binary_search(const vector<int> &sequence, const int s, const int e, const int target) {
    // base
    if (s >= e) return s;

    // default
    const int m = (s + e) / 2;
    if (sequence[m] >= target) return binary_search(sequence, s, m, target);
    else return binary_search(sequence, m+1, e, target);
}

int solve(const vector<int> &sequence) {
    vector<int> lis;

    for (auto e: sequence) {
        // 마지막 원소보다 큰 경우
        if (lis.empty() || e > lis.back()) {
            lis.push_back(e);
        } else {
            const int index = binary_search(lis, 0, lis.size(), e);
            lis[index] = e;
        }
    }

    return lis.size();
}

int main() {
    int N; scanf("%d", &N);
    vector<int> A(N); for (int i = 0; i < N; i++) scanf("%d", &A[i]);

    printf("%d\n", solve(A));

    return 0;
}