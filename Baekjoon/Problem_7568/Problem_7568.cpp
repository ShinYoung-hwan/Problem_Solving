#include <iostream>
#include <utility>

using namespace std;

pair<int, int>* Set_Datas(size_t size)
{
    pair<int, int>* datas = new pair<int, int>[size];

    for(int i = 0; i < size; i++)
    {
        cin >> datas[i].first >> datas[i].second;
    }

    return datas;
}

void Print_Ranks(pair<int, int>* datas, size_t size)
{
    for(int i = 0; i < size; i++)
    {
        int rank = 1;
        for(int j = 0; j < size; j++)
        {
            if(datas[i].first < datas[j].first && datas[i].second < datas[j].second) rank++;
        }
        cout << rank << ' ';
    }
}

int main()
{
    int num; cin >> num;

    pair<int, int>* datas = Set_Datas(num);

    Print_Ranks(datas, num);

    return 0;
}