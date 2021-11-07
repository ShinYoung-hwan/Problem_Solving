#include <iostream>

using namespace std;

int Get_Max(int* store, int N, int M)
{
    int output = 0;

    for(int i = N - 1; i >= 2; i--)
    {
        for(int j = i - 1; j >= 1; j--)
        {
            for(int k = j - 1; k >= 0; k--)
            {
                if(store[i] + store[j] + store[k] <= M  && store[i] + store[j] + store[k] > output){
                    output = store[i] + store[j] + store[k];
                }
            }
        }
    }

    return output;
}

int main(void)
{
    int N, M; cin >> N >> M;
    int* Store = new int[N];
    for(int i = 0; i < N; i++) cin >> Store[i];

    cout << Get_Max(Store, N, M) << endl;

    delete[] Store;

    return 0;
}