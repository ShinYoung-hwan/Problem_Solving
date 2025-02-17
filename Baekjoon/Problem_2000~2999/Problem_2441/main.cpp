#include <iostream>

using namespace std;

void Stamp(int num)
{
    for(int i = 0; i < num; i++)
    {
        int j = 0;
        for(; j < i; j++) cout << ' ';
        for(; j < num; j++) cout << '*';
        cout << endl; 
    }
}

int main(void)
{
    int N; cin >> N;
    
    Stamp(N);
        
    return 0;
}