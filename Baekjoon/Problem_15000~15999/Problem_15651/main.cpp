#include <iostream>
#include <vector>

using namespace std;

void printPicked(vector<int> v)
{   // print picked result //
    for(auto item: v)
        cout << item << ' ';
    cout << '\n';     
}

void pick(vector<int> &v, const int Max, const int toPick)
{
    if(toPick == 0)
    {   // already pick 8 elements //
        printPicked(v);
        return ;
    }

    for(int i = 1; i <= Max; i++)
    {        
        // set //
        v.push_back(i);

        // recursion //
        pick(v, Max, toPick-1);

        // remove //
        v.pop_back();
    }
}

int main(void)
{
    int N, M; cin >> N >> M;
    vector<int> v;

    pick(v, N, M);

    return 0;
}