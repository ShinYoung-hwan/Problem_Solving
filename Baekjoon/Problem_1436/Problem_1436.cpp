#include <iostream>
#include <string>

using namespace std;

int getNthDevilNum(const int N)
{
    int index = 666, curNum = 0;
    while(true)
    {       
        if(to_string(index).find("666") != string::npos)
            curNum++;

        if(curNum == N)
            return index;

        index++;
    }
}

int main(void)
{
    int N; cin >> N;

    cout << getNthDevilNum(N) << endl;
}