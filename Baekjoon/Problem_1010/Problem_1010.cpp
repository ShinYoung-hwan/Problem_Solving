#include <iostream>

using namespace std;

unsigned long long Factorial(const int n)
{
    unsigned long long output = 1;
    for(int i = n; i > 0; i--) output *= i;
    return output;
}


unsigned long long Permutation(const int n, const int r)
{
    unsigned long long output = 1;
    for(int i = n; i > n - r; i--) output *= i;
    return output;
}

unsigned long long Combination(const int n, const int r)
{
    unsigned long long p = Permutation(n, r);
    unsigned long long f = Factorial(r);
    unsigned long long output = p / f;
    return output;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int N, M; cin >> N >> M;
        if(N > M - N) N = M - N;

        cout << Combination(M, N) << endl;
    }
}