#include <iostream>

using namespace std;

void Stamp(const int num)
{
    for(int i = 1 ; i <= num; i++)
    {
        for(int j = 0; j < i; j++) cout << '*';
        for(int j = 0; j < 2 * (num - i); j++) cout << ' ';
        for(int j = 0; j < i; j++) cout << '*';
        cout << endl;
    }
    for(int i = num - 1; i > 0; i--)
    {
        for(int j = 0; j < i; j++) cout << '*';
        for(int j = 0; j < 2 * (num - i); j++) cout << ' ';
        for(int j = 0; j < i; j++) cout << '*';
        cout << endl;
    }
}

int main(void)
{
    int N; cin >> N;
    
    Stamp(N);
        
    return 0;
}