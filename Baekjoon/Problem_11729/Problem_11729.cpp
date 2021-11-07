#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int repofHanoi(const int num)
{
    return pow(2, num) - 1;
}

void Hanoi(const int num, const int src, const int dst, const int aux)
{
    if(num == 1)
    {
        printf("%d %d\n", src, dst);
    }
    else
    {
        Hanoi(num - 1, src, aux, dst);
        printf("%d %d\n", src, dst);
        Hanoi(num - 1, aux, dst, src);
    }
}

int main(void)
{
    int N; cin >> N;

    cout << repofHanoi(N) << endl;

    Hanoi(N, 1, 3, 2);

    return 0;
}