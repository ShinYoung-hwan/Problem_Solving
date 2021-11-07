#include <iostream>
#include <cmath>
using namespace std;

void Sort(int& a, int& b, int& c)
{
    if(a > c)
    {
        int tmp = a;
        a = c;
        c = tmp;
    }
    if(b > c)
    {
        int tmp = b;
        b = c;
        c = tmp;
    }
}

bool IsRightAngle(const int a, const int b, const int c)
{
    if(pow(a, 2) + pow(b, 2) == pow(c, 2)) return true;
    else return false;
}

int main(void)
{
    int a, b, c; cin >> a >> b >> c;

    while(!(a == 0 && b == 0 && c == 0))
    {
        Sort(a, b, c);

        if(IsRightAngle(a, b, c)) cout << "right" << endl;
        else cout << "wrong" << endl;

        cin >> a >> b >> c;
    }
    
    return 0;
}