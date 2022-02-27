#include <iostream>
#include <string>

using namespace std;

size_t getNumOfDigit(const int n)
{   /* x_1 = 1
     * x_t = x_(t-1)*10 + 1
     * 
     * x_t mod n = ((x_(t-1)*10) mod n + 1 mod n) mod n
     * x_t  = (x_(t-1)*10) mod n + 1 mod n
     *      = (x_(t-1)*10) mod n + 1
     */
    long num = 1;
    size_t cnt = 1;

    while((num = num % n))
    {
        num = num * 10 + 1;
        cnt++;
    }

    return cnt;
}

int main(void)
{
    int n;

    while(cin >> n)
    {
        cout << getNumOfDigit(n) << '\n';
    }
    
    return 0;
}