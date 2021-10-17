#include <iostream>

using namespace std;

int Permutation(int& Rep, const int hlen)
{
    int Sum = 0;
    int i;
    for(i = 1; Sum < hlen; i++)
    {
        Sum += i;
        Rep++;
    }
    if(hlen < Sum)
    {
        Rep--;
        return Sum - --i;
    } 
    return Sum;
}

int GetMin(int len)
{
    int Rep = 0;
    int Sum = 2 * Permutation(Rep, static_cast<int>(len / 2));
    int Maxv = Rep + 1;
    Rep *= 2;

    for(; len - Sum > 0;)
    {
        if(len - Sum <= Maxv)
        {
            Sum = Sum + len - Sum;
        }
        else
        {
            Sum += Maxv;
        }
        Rep++;
    }

    return Rep;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int x, y; cin >> x >> y;

        cout << GetMin(y - x) << endl;
    }

    return 0;
}
