#include <iostream>
#include <cmath>
using namespace std;
enum { x, y };

int Get_Absolute(int num)
{
    if(num >= 0) return num;
    else return -num; 
}

template<size_t N>
int Count_ContactPoint(int (&pos1)[N], int r1, int (&pos2)[N], int r2)
{
    if(pos1[x] == pos2[x] && pos1[y] == pos2[y] && r1 == r2) return -1;
    float d = sqrt(pow(pos1[x] - pos2[x], 2) + pow(pos1[y] - pos2[y], 2));

    if(d > r1 + r2) return 0;
    else if(d == r1 + r2) return 1;
    else if(d > Get_Absolute(r1- r2)) return 2;
    else if(d == Get_Absolute(r1 - r2)) return 1;
    else return 0;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int pos1[2], r1; cin >> pos1[x] >> pos1[y] >> r1;
        int pos2[2], r2; cin >> pos2[x] >> pos2[y] >> r2;

        cout << Count_ContactPoint(pos1, r1, pos2, r2) << endl;
    }
    return 0;
}