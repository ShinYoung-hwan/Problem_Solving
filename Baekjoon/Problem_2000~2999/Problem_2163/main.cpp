#include <iostream>

using namespace std;
void Swap(int& min, int& max)
{
    if(min > max)
    {
        int tmp = min;
        min = max;
        max = tmp;
    }
}

int Get_MinRep(int min, int max)
{
    return (min - 1) + (max - 1) * min;
}

int main(void)
{
    int N, M; cin >> N >> M; Swap(N, M);

    cout << Get_MinRep(N, M) << endl;

    return 0;
}