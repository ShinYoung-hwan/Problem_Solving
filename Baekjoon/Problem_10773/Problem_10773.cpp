#include <iostream>
#include <stack>

using namespace std;

unsigned int StackOperation(size_t SIZE)
{
    stack<int> s;
    for(int i = 0; i < SIZE; i++)
    {
        int num; cin >> num;
        if(num == 0) s.pop();
        else s.push(num);
    }

    unsigned int output = 0;

    int stacksize = s.size();
    for(int i = 0; i < stacksize; i++)
    {
        output += s.top();
        s.pop();
    }
    return output;
}

int main(void)
{
    size_t SIZE; cin >> SIZE;

    cout << StackOperation(SIZE) << endl;

    return 0;
}