#include <iostream>
#include <cmath>

using namespace std;

bool IsPrime(int num)
{
    if(num == 1) return false;
    else if(num == 2) return true;
    else if(num % 2 == 0) return false;
    else
    {
        for(int i = 3; i <= sqrt(num); i = i + 2)
        {
            if(num % i == 0) return false;
        }
        return true;
    }
}

void Get_Partition(int num)
{
    int p1, p2;
    for(int i = 2; i <= num / 2; i++)
    {
        if(IsPrime(i) && IsPrime(num - i))
        {
            p1 = i; p2 = num - i;
        }
    }

    cout << p1 << ' ' << p2 << endl;
}

int main(void)
{
    int Testcase; cin >> Testcase;
    for(int i = 0; i < Testcase; i++)
    {
        int n; cin >> n;
        if(n % 2 == 0) Get_Partition(n);
    }
    return 0;
}