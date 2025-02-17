#include <iostream>
#include <vector>

using namespace std;

void printPicked(vector<int> v)
{   // print picked result //
    for(auto item: v)
        cout << item << ' ';
    cout << '\n';     
}

void pick(vector<int> &v, bool *isPicked, const int Max, const int toPick)
{
    if(toPick == 0)
    {   // already pick 8 elements //
        printPicked(v);
        return ;
    }

    for(int i = 1; i <= Max; i++)
    {
        // back tracking condition //
        if(isPicked[i])
            continue;
        
        // set //
        v.push_back(i);
        isPicked[i] = true;

        // recursion //
        pick(v, isPicked, Max, toPick-1);

        // remove //
        v.pop_back();
        isPicked[i] = false;
    }
}

int main(void)
{
    int N, M; cin >> N >> M;
    vector<int> v;
    bool isPicked[9] = {0, };

    pick(v, isPicked, N, M);

    return 0;
}