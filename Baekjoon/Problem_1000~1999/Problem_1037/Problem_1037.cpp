#include <iostream>

using namespace std;

int* SetFactors(const size_t size)
{
    int* factors = new int[size];

    for(int i = 0; i < size; i++) cin >> factors[i];
    return factors;
}

int Findmultiple(const size_t size, const int* Factors)
{
    if(size == 1) return Factors[0] * Factors[0];
    else
    {
        int min = Factors[0], max = min;

        for(int i = 1; i < size; i++)
        {
            if(min > Factors[i]) min = Factors[i];
            if(max < Factors[i]) max = Factors[i];
        }

        return min * max;
    }
}

int main(void)
{
    int NumofFactors; cin >> NumofFactors;

    int* Factors = SetFactors(NumofFactors);

    cout << Findmultiple(NumofFactors, Factors) << endl;
    
    delete[] Factors;
    return 0;
}