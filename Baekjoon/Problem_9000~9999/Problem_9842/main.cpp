#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

bool is_prime(const int val, const vector<int> &primes) {
    if (val == 2) return true;

    for (auto i: primes) {
        if (i > static_cast<int>(ceil(sqrt(val)))) break;
        else if (val % i == 0) return false;
    }
    return true;
}

int main() {
    int N; scanf("%d", &N);
    vector<int> primes;
    
    int val = 1;
    while (primes.size() < N) {
        if (is_prime(++val, primes)) {
            primes.push_back(val);
        }
    }

    printf("%d\n", primes[N-1]);
    
    return 0;
}