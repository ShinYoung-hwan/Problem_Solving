#include <iostream>
#include <string>
#include <stack>

using namespace std;

string IsProper(string str)
{
    stack<char> st;

    for(int i = 0; i < str.length(); i++)
    {
        if(str.at(i) == '(')
        {
            st.push('(');
        }
        else
        {
            if(st.empty()) return "NO";
            
            if(st.top() == '(') st.pop();
            else return "YES";
        }
    }
    if(st.empty()) return "YES";
    else return "NO";
}

int main(void)
{
    int SIZE; cin >> SIZE;

    for(int i = 0; i < SIZE; i++)
    {
        string str; cin >> str;
        cout << IsProper(str) << endl;
    }

    return 0;
}