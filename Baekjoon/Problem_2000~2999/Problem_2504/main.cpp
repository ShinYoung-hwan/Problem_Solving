#include <iostream>
#include <string>
#include <stack>

using namespace std;

int Get_Value(string str)
{
    stack<int> s;

    for(int i = 0; i < str.length(); i++)
    {
        
    }

    return s.top();
}

int main(void)
{
    string str; cin >> str;

    cout << Get_Value(str) << endl;

    return 0;
}