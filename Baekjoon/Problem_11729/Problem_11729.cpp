#include <iostream>
#include <cmath>
/*Basic Algorithm
first, we move the smaller dist to aux
then, we move the larger disk to dest
and finally, we move the smaller disk from aux to dest
*/
using namespace std;

int RepofHanoi(int num)
{
    return pow(2, num) - 1;
}

void Hanoi(int num, int src, int dst, int aux)
{
    
    if(num == 1)
    {
         cout << src << ' ' << dst << endl;
    }
    else
    {
        Hanoi(num - 1, src, aux, dst);
        cout << src << ' ' << dst << endl;
        Hanoi(num - 1, aux, dst, src);
    }
}

int main(void)
{
    int N; cin >> N;

    cout << RepofHanoi(N) << endl;

    Hanoi(N, 1, 3, 2);

    return 0;
}