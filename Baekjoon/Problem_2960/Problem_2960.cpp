#include <iostream>
#include <utility>

using namespace std;

int N, K, Rep = 1;

bool* Set_Arr()
{
    bool* arr = new bool(N + 1);
    for(int i = 0; i <= N; i++) arr[i] = false;
    return arr;
}

int Get_NonAccessFirst(bool* IsAccessed)
{
    for(int i = 3; i < N; i++)
        if(IsAccessed[i] == false) return i;
}

int Get_NonAccessSecond(bool* IsAccessed, int first, int second)
{
    int Nsecond = second;

    while(first * Nsecond <= N)
    {
    }

    return Nsecond;
}

int Get_nthValue(bool* IsAccessed, int a, int b)
{
    if(K == Rep) return a * b;
    else
    {
        Rep++;
        if(a * b > N)
        {
            return Get_nthValue(IsAccessed, Get_NonAccessFirst(IsAccessed), 1);
        }
        else {
            return Get_nthValue(IsAccessed, a, Get_NonAccessSecond(IsAccessed, a, b));
        }
    }
}

int main(void)
{
    int N, K; cin >> N >> K;
    bool* IsAccessed = Set_Arr();
    cout << Get_nthValue(IsAccessed, 2, 1) << endl;
    delete[] IsAccessed;
    
    return 0;
}