#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string &str1, string &str2)
{   // some issue in here //
    if(str1.length() < str2.length()) return true;
    else if(str1.length() == str2.length())
    {
        for(int i = 0; i < str1.length(); i++)
        {
            if(str1.at(i) < str2.at(i)) return true;
        }
    }
    return false;
}

void setDatas(vector<string> &datas, const int N)
{
    string str;
    for(int i = 0; i < N; i++)
    {
        cin >> str;
        datas.push_back(str);
    }
}

void printDatas(vector<string> &datas, const int N)
{
    for(int i = 0; i < N-1; i++)
    {
        if(datas.at(i) != datas.at(i+1))
            cout << datas.at(i) << endl;
    }
    cout << datas.at(N-1) << endl;
}

int main(void)
{
    int N; cin >> N;
    vector<string> datas; setDatas(datas, N);

    sort(datas.begin(), datas.end(), compare);
    
    printDatas(datas, N);
    return 0;
}