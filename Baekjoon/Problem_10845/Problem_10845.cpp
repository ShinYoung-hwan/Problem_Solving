#include <iostream>
#include <queue>

using namespace std;

void QueueOp(queue<int>& q)
{
    string type; cin >> type;
    int num;

    if(type == "push") 
    {
        cin >> num;
        q.push(num);
    }
    else if(type == "pop")
    {
        if(q.empty()) cout << -1 << endl;
        else
        {
            cout << q.front() << endl;
            q.pop();
        }
    }
    else if(type == "size")
    {
        cout << q.size() << endl;
    }
    else if(type == "empty")
    {
        if(q.empty()) cout << 1 << endl;
        else cout << 0 << endl;
    }
    else if(type == "front")
    {
        if(q.empty()) cout << -1 << endl;
        else cout << q.front() << endl;
    }
    else if(type == "back")
    {
        if(q.empty()) cout << -1 << endl;
        else cout << q.back() << endl;
    }
}

int main(void)
{
    int SIZE; cin >> SIZE;
    queue<int> qu;
    for(int i = 0; i < SIZE; i++)
    {
        QueueOp(qu);
    }   

    return 0;
}