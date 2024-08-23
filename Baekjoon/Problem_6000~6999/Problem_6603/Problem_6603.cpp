#include <cstdio>
#include <vector>

const int MAXK = 13;

using namespace std;

void solve(const int S[MAXK], const int k, vector<int> &stack, const int start=0) {    
    if (stack.size() == 6) {
        for (auto e: stack) printf("%d ", e);
        printf("\n");
        return;
    }
    
    for (int i = start; i < k; i++) {
        stack.push_back(S[i]);
        solve(S, k, stack, i+1);
        stack.pop_back();
    }
}

int main() {
    while (true) {
        int k; scanf("%d", &k);
        if (k == 0) break;

        int S[MAXK];
        for (int i = 0; i < k; i++) scanf("%d", &S[i]);

        vector<int> stack;
        solve(S, k, stack);
        printf("\n");
    }

    return 0;
}