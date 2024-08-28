#include <cstdio>
#include <cstdint>

using namespace std;

int main() {
    int64_t S; scanf("%lld", &S);

    int64_t sum = 0, cur = 1;

    while (sum < S) {
        sum += cur;
        cur += 1;
    }

    printf("%lld\n", sum == S ? cur-1 : cur-2);

    return 0;
}