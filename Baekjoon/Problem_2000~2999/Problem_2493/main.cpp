#include <cstdio>
#include <vector>

const int MAXN = 500000;

using namespace std;

int main() {
    int N; scanf("%d", &N);
    int towers[MAXN] = { 0, };
    for (int i = 0; i < N; i++) scanf("%d", towers+i);

    // solve O(2N)
    vector<int> stack;
    for (int i = 0; i < N; i++) {
        while (!stack.empty() && towers[stack.back()] < towers[i]) stack.pop_back();

        printf("%d ", stack.empty() ? 0 : stack.back()+1);
        stack.push_back(i);
    }

    return 0;
}