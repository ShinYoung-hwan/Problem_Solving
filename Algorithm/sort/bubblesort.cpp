#include <iostream>

using namespace std;

void print_arr(const int *arr, const int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl;
}

void bubble_sort(int *arr, const int n)
{
    int tmp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
                printf("Swap %dth, %dth\t", j + 1, j + 2);
                print_arr(arr, n);
            }
        }
    }
}

int main()
{
    int n = 5;
    int arr[] = {3, 4, 2, 1, 5};
    cout << "Before Sort:\t";
    print_arr(arr, n);
    bubble_sort(arr, n);
    cout << "After Sort:\t";
    print_arr(arr, n);

    return 0;
}