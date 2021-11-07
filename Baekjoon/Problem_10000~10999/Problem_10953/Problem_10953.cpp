#include <iostream>
#include <string>

using namespace std;

int Plus(string str)
{
    int pos = str.find(',');
    int A = stoi(str.substr(0,pos));
    int B = stoi(str.substr(pos + 1, str.length()));
    
    return A + B;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        string str; cin >> str;

        cout << Plus(str) << endl;
    }
    
    return 0;
}