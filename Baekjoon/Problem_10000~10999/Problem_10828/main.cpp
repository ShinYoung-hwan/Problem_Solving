#include <iostream>
#include <string>
#include <stack>

using namespace std;

void StackOperation(size_t SIZE)
{
    stack<int> s;
    for(int i = 0; i < SIZE; i++)
    {
        string type; cin >> type;
        
        if(type == "push")
        {
            int x; cin >> x;
            s.push(x);
        }
        else if(type == "pop")
        {
            if(s.empty() == true) cout << -1 << endl;
            else 
            {
                cout << s.top() << endl;
                s.pop();
            }
        }
        else if(type == "size") cout << s.size() << endl;
        else if(type == "empty")
        {
            if(s.empty() == true) cout << 1 << endl;
            else cout << 0 << endl;
        }
        else if(type == "top")
        {
            if(s.empty() == true) cout << -1 << endl;
            else 
            {
                cout << s.top() << endl;
            }
        }
    }
}

int main(void)
{
    size_t SIZE; cin >> SIZE;

    StackOperation(SIZE);

    return 0;
}