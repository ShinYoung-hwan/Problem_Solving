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
        datas.push_back(x_i);
    }
}

void reorganizeVector(const vector<int> datas, vector<int> &results)
{
    results.push_back(datas.at(0));

    for(int i = 1; i < datas.size(); i++)
    {
        if(datas.at(i) != datas.at(i-1))
            results.push_back(datas.at(i));
    }
}

void printDatas(const vector<int> results)
{   // print vector O(N) //
    for(int i = 0; i < results.size(); i++)
    {
        cout << results.at(i) << ' ';
    }
}

int main(void)
{
    size_t N; cin >> N;
    vector<int> datas, results;

    setDatas(datas, N);

    // sort increasing order //
    sort(datas.begin(), datas.end());

    reorganizeVector(datas, results);

    printDatas(results);

    return 0;
}