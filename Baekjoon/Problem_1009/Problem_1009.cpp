#include <iostream>

using namespace std;

int Get_ComNum(const int a, const int b)
{
    switch(a % 10)
    {
        case 0: return 10;
        case 1: return 1;
        case 2:
            if(b % 4 == 0) return 6;
            else if(b % 4 == 1) return 2;
            else if(b % 4 == 2) return 4;
            else return 8;
        case 3:
            if(b % 4 == 0) return 1;
            else if(b % 4 == 1) return 3;
            else if(b % 4 == 2) return 9;
            else return 7;
        case 4:
            if(b % 2 == 0) return 6;
            else return 4;
        case 5: return 5;
        case 6: return 6;
        case 7:
            if(b % 4 == 0) return 1;
            else if(b % 4 == 1) return 7;
            else if(b % 4 == 2) return 9;
            else return 3;
        case 8:
            if(b % 4 == 0) return 6;
            else if(b % 4 == 1) return 8;
            else if(b % 4 == 2) return 4;
            else return 2;
        case 9:
            if(b % 2 == 0) return 1;
            else return 9;
    }
    return -1;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int a, b; cin >> a >> b;

        cout << Get_ComNum(a, b) << endl;
    }

    return 0;
}