#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>

using namespace std;

void setDatas(vector<pair<int, int>> &datas)
{
    int N; cin >> N;
    int x, y;
    for(int i = 0; i < N; i++)
    {
        scanf("%d %d", &x, &y);
        datas.push_back(make_pair(x, y));
    }
}

void printDatas(vector<pair<int, int>> &datas)
{
    for(auto item: datas)
    {
        printf("%d %d\n", item.first, item.second);
    }
}

int main(void)
{
    vector<pair<int, int>> datas; setDatas(datas);

    // sort vector<pair> //
    // compare from first to second by acending order //
    sort(datas.begin(), datas.end());

    printDatas(datas);

    return 0;
}