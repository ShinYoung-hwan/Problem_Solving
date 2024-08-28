#include <cstdio>
#include <deque>
#include <utility>

using namespace std;

pair<int, int> find(const deque<int> &deq, const int target) {
    int l = 0, r = 0;
    int length = deq.size();

    // left
    int cur = 0;
    while (deq[cur] != target) {
        l += 1;
        cur = cur == 0 ? length - 1 : (cur - 1) % length;
    }

    // right
    cur = 0;
    while (deq[cur] != target) {
        r += 1;
        cur = (cur + 1) % length;
    }

    return {l, r};
}

int main() {
    int N, M; scanf("%d %d", &N, &M);

    deque<int> deq;
    for (int i = 1; i <= N; i++) deq.push_back(i);

    int answer = 0;
    for (int i = 0; i < M; i++) {
        int target; scanf("%d", &target);

        pair<int, int> tmp = find(deq, target);
        int l = tmp.first, r = tmp.second;

        if (l <= r) {
            answer += l;

            for (int j = 0; j < l; j++) {
                deq.push_front(deq.back());
                deq.pop_back();
            }
        } else {
            answer += r;
            
            for (int j = 0; j < r; j++) {
                deq.push_back(deq.front());
                deq.pop_front();
            }
        }

        deq.pop_front();
    }

    printf("%d\n", answer);

    return 0;
}