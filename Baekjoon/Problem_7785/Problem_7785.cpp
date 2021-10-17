#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(void)
{
    int SIZE; cin >> SIZE;
    set<string> IsWorking;
    
    for(int i = 0; i < SIZE; i++)
    {
        string name; cin >> name;
        string IOput; cin >> IOput;

        if(IOput == "enter")
        {
            IsWorking.insert(name);
        }
        else
        {
            IsWorking.erase(IsWorking.find(name));
        }
    }

    for(set<string>::reverse_iterator iter = IsWorking.rbegin(); iter != IsWorking.rend(); iter++)
    {
        cout << *iter << '\n';
    }

    return 0;
}
