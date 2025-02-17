#include <iostream>

using namespace std;

unsigned long num[1000001] = {0, }; 

unsigned long getNum(const int N)
{
    // basic case //
    if(N == 1) // 1 //
        return 1; // 00, 11 //
    else if(N == 2)
        return 2;
    
    // recursive case //
    // add 00 from N-2, add 1 from N-1 // 
    if(!num[N])
    {   // not computed //
        num[N] = (getNum(N-1)  + getNum(N-2)) % 15746;
    }    
    return num[N];
}

int main(void)
{
    int N; cin >> N;

    cout << getNum(N)<< '\n';

    return 0;
}