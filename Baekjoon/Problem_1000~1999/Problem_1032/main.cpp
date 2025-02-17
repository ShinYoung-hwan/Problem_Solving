#include <iostream>
#include <string>

using namespace std;

void CompareStr(string& str)
{
    string cstr; cin >> cstr;

    for(int i = 0; i < str.length(); i++)
    {
        if(str.at(i) != cstr.at(i)) str.at(i) = '?';
    }
}

int main(void)
{
    int Testcase; cin >> Testcase;
    string str; cin >> str;

    for (int i = 1; i < Testcase; i++)
    {
        CompareStr(str);
    }    
    cout << str << endl;

    return 0;
}