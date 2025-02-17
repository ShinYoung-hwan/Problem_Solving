#include <cstdio>
#include <cstdint>

using namespace std;

const int MAXN = 100000;
int N;
int64_t K; 

bool update_sum(int64_t &_sum, const int val) {
    _sum += val;
    return K < _sum ? true : false;
}

bool go_forward(const int course_length[MAXN], int64_t &_sum) {
    for (int i = 0; i < N; i++) {
        if (update_sum(_sum, course_length[i])) {
            printf("%d\n", i+1);
            return true;
        }
    }
    return false;
}

void go_backward(const int course_length[MAXN], int64_t &_sum) {
    for (int i = N-1; i >= 0; i--) {
        if (update_sum(_sum, course_length[i])) {
            printf("%d\n", i+1);
            return;
        }
    }
}

int main() {
    scanf("%d %lld", &N, &K);
    int course_length[MAXN];
    for (int i = 0; i < N; i++) scanf("%d", &course_length[i]);

    int64_t _sum = 0;
    if (!go_forward(course_length, _sum)) {
        go_backward(course_length, _sum);
    }

    return 0;
}