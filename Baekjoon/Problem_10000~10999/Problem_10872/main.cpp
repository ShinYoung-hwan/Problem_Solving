#include <iostream>

using namespace std;

int Pact(const int num)
{
    if(num == 0) return 1;
    else return num * Pact(num - 1);
}
int main(void)
{
    int num; cin >> num;

    cout << Pact(num) << endl;

    return 0;
}