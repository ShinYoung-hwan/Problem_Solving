#include <iostream>

using namespace std;

int* Set_Arr(size_t SIZE)
{
    int* arr = new int[SIZE];
    for(int i = 0; i < SIZE; i++) cin >> arr[i];

    for(int i = 0; i < SIZE; i++)
    {
        int minpos = i;
        for(int j = i + 1; j < SIZE; j++)
        {
            if(arr[minpos] > arr[j]) minpos = j;
        }
        int tmp = arr[i];
        arr[i] = arr[minpos];
        arr[minpos] = tmp;
    }

    return arr;
}

void PrintArr(int* arr, size_t SIZE)
{
    for(int i = 0; i < SIZE; i++) cout << arr[i] << endl;
}

int main(void)
{
    size_t SIZE; cin >> SIZE;
    int* arr = Set_Arr(SIZE);

    PrintArr(arr, SIZE);

    return 0;
}