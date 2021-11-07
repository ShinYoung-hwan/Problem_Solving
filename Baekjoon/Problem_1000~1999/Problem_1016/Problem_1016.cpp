#include <iostream>
#include <cmath>

using namespace std;

bool IsNoneSqureNum(const unsigned long long num)
{
    if(num < 4) return true;
    
    for(unsigned long long i = 2; i * i <= num; i++)
    {
        if(num % (i * i) == 0) return false;
    }
    return true;
}

unsigned long long Count_NoneSquareNum(const unsigned long long min, const unsigned long long max)
{
    unsigned long long output = 0;
    for(unsigned long long i = min; i <= max; i++)
    {
        if(IsNoneSqureNum(i)) 
        {
            output++;
        }
    }
    return output;
}

int main(void)
{
    unsigned long long M, N; cin >> M >> N;

    cout << Count_NoneSquareNum(M, N) << endl;

    return 0;
}