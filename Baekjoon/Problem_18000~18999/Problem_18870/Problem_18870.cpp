#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void setDatas(vector<int> &datas, const size_t N)
{   // set datas to vector O(N) //
    int x_i;
    for(int i = 0; i < N; i++)
    {
        cin >> x_i;
        if(find(datas.begin(), datas.end(), x_i) == datas.end())
        {   // add only new item //
            datas.push_back(x_i);
        }
    }
}

void compressCoordinate(const vector<int> datas, vector<int> &result)
{   // compress coordinate in datas to result O(N) //
    
}

void printDatas(const vector<int> result)
{   // print vector O(N) //
    for(int i = 0; i < result.size(); i++)
    {
        cout << result.at(i) << ' ';
    }
}

int main(void)
{
    size_t N; cin >> N;
    vector<int> datas, result;

    setDatas(datas, N);

    compressCoordinate(datas, result);

    printDatas(result);

    return 0;
}