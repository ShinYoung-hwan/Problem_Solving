#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string str1, string str2)
{   
    if(str1.length() == str2.length()) 
    {   // if same length, dictionary order //
        return str1 < str2;
    }
    // if different length //
    return str1.length() < str2.length();
}

void setDatas(vector<string> &datas, const int N)
{
    string str;
    for(int i = 0; i < N; i++)
    {
        cin >> str;
        if(find(datas.begin(), datas.end(), str) == datas.end())
        {   // if the input is already found, do not store //
            datas.push_back(str);
        }
    }
}

void printDatas(vector<string> &datas, const int N)
{
    for(string item: datas)
    {   // print all items in vector //
        cout << item << '\n';
    }
}

int main(void)
{
    int N; cin >> N;
    vector<string> datas; setDatas(datas, N);

    sort(datas.begin(), datas.end(), compare);
    
    printDatas(datas, N);
    return 0;
}