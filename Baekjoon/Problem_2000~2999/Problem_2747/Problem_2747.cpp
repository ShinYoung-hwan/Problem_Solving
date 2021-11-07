#include <iostream>

using namespace std;

long long NthFibonum(size_t num)
{
    long long arr[46] = {0, 1,};

    for(int i = 2; i <= num; i++)
    {
        arr[i] = arr[i - 2] + arr[i - 1];
    }
    return arr[num];
}

int main(void)
{
    size_t SIZE; cin >> SIZE;

    cout << NthFibonum(SIZE) << endl;

    return 0;
}