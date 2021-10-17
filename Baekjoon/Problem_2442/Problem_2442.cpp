#include <iostream>

using namespace std;

void Stamp(int num)
{
    for(int i = 1; i <= num; i++)
    {
        for(int j = 0; j < num - i; j++) cout << ' ';
        for(int j = 0; j < 2 * i - 1; j++) cout << '*';
        cout << endl;
    }
}

int main(void)
{
    int N; cin >> N;
    
    Stamp(N);
        
    return 0;
}