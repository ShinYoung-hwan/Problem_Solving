#include <iostream>

using namespace std;

int Fibo(const int num)
{
    if(num == 0) return 0;
    else if(num == 1) return 1;
    else return Fibo(num - 2) + Fibo(num -1);
}

int main(void)
{
    int num; cin >> num;

    cout << Fibo(num) << endl;

    return 0;
}