#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare_decendingOrder(const int &a, const int &b){ return a > b; }

void setDatas(vector<int> &datas)
{
    string str; cin >> str;

    for(auto item : str)
    {
        datas.push_back(item - '0');
    }
}

void printDatas(vector<int> &datas)
{
    for(auto item : datas)
        cout << item;
}

int main(void)
{
    vector<int> datas; setDatas(datas);

    sort(datas.begin(), datas.end(), compare_decendingOrder);

    printDatas(datas);
}