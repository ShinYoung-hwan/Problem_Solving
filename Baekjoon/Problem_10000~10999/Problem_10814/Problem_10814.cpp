#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool compare(pair<int, string> p1, pair<int, string> p2)
{
    if(p1.first != p2.first)
    {   // compare 
        return p1.first < p2.first;
    }
    // stable sort //
    return false;
}

void setDatas(vector<pair<int, string>> &datas, const size_t N)
{   // set datas //
    int age;
    string name;

    for(int i = 0; i < N; i++)
    {
        cin >> age >> name;
        datas.push_back(make_pair(age, name));
    }
}

void printDatas(const vector<pair<int, string>> datas)
{   // print output //
    for(int i = 0; i < datas.size(); i++)
    {
        cout << datas.at(i).first << ' ' << datas.at(i).second << '\n';
    }
}

int main(void)
{
    // set input size //
    size_t N; cin >> N;
    vector<pair<int, string>> datas;
    setDatas(datas, N);

    stable_sort(datas.begin(), datas.end(), compare);
    printDatas(datas);

    return 0;    
}