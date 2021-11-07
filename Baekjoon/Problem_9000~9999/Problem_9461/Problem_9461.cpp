#include <iostream>

using namespace std;
long long Seq[101] = {0, 1, 1,};
int AccessedPos = 3;

long long Get_PadobanSeq(int num)
{
    for(int i = AccessedPos; i <= num; i++)
    {
        Seq[i] = Seq[i - 3] + Seq[i - 2];
        AccessedPos = i;
    }
    return Seq[num];
}

int main(void)
{
    size_t SIZE; cin >> SIZE;

    for(int i = 0; i < SIZE; i++)
    {
        int num; cin >> num;
        cout << Get_PadobanSeq(num) << endl;
    }

    return 0;
}