#include <iostream>
#include <utility>

using namespace std;

void NumofCall(const int n)
{
    pair<int, int> fib;
    fib.first = 1, fib.second = 0;

    for(int i = 0; i < n; i++)
    {
        int tmp = fib.first;
        fib.first = fib.second;
        fib.second = tmp + fib.first;
    }

    cout << fib.first << ' ' << fib.second << endl;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int num; cin >> num;

        NumofCall(num);
    }

    return 0;
}