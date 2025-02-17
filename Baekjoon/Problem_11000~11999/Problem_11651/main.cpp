#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>

using namespace std;

bool compare(const pair<int, int> &a, const pair<int, int> &b)
{
    if(a.second < b.second) return true;
    else if(a.second == b.second)
    {
        if(a.first < b.first) return true;
    }
    return false;
}

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
    sort(datas.begin(), datas.end(), compare);

    printDatas(datas);

    return 0;
}