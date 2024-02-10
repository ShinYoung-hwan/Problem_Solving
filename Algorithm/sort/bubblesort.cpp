#include <iostream>

using namespace std;

void bubble_sort(int *arr, const int n)
{

    int tmp;
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[i] < arr[j])
            {
                tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}

int main()
{
    int arr[] = {8, 4, 1, 3, 2, 5, 6, 7};
    int n = 8;

    bubble_sort(arr, n);

    for (int arri : arr)
    {
        cout << arri << ' ';
    }

    return 0;
}