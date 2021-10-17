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

int Count_Prime(int num)
{
    int count = 0;

    for(int i = num + 1; i <= 2 * num; i++)
    {
        if(IsPrime(i)) count++;
    }

    return count;
}

int main(void)
{
    int n;
    do{
        cin >> n; if(n == 0) break;
        cout << Count_Prime(n) << endl;
    }while(n != 0);

    return 0;
}