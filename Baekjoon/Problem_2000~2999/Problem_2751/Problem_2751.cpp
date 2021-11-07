#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

void setDatas(vector<int> &datas, const int N)
{   // Use vector STL for store datas //
    // Time Complexity: O(N) //
    int num;
    for(int i = 0; i < N; i++)
    {
        cin >> num;
        datas.push_back(num);
    }
}

void printDatas(const vector<int> &datas)
{
    for(auto item : datas)
        printf("%d\n", item);
}

int main(void)
{
    int N; cin >> N;
    vector<int> datas; setDatas(datas, N);

    // Use standard "sort function" in "algorithm library" //
    // Time Complexity: O(N lgN) //
    sort(datas.begin(), datas.end());

    printDatas(datas);

    return 0;
}