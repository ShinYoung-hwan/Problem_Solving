#include <iostream>
#include <utility>
#include <map>

using namespace std;

int main(void)
{
    map<int, int> frequency;
    pair<int, int> mode; mode.first = 0;//pair<max rep, mode>
    int Sum = 0;
    
    for(int i = 0; i < 10; i++)
    {
        int input; cin >> input;
        Sum += input;
        if(frequency.find(input) == frequency.end())
        {
            frequency[input] = 1;
            if(mode.first < frequency[input]){
                mode.first = frequency[input];
                mode.second = input;
            } 
        }
        else
        {
            frequency[input] += 1;
            if(mode.first < frequency[input]){
                mode.first = frequency[input];
                mode.second = input;
            } 
        }
    }

    cout << Sum / 10 << endl;
    cout << mode.second << endl;
    return 0;
}