#include <iostream>

using namespace std;

void print_arr(const int *arr, const int n){
    for (int i = 0; i < n; i++){
        cout << arr[i] << ' ';
    }
    cout << endl;
}

void insertionSort(int *arr, const int n){
    int cur, j;
    for (int i = 1; i < n; i++){
        cur = arr[j=i];
        while (--j >= 0 && cur < arr[j]){
            arr[j+1] = arr[j];
        }
        arr[j+1] = cur;

        printf("Insert %dth, %dth\t", i+1, j+2);
        print_arr(arr, n);
    }
}

int main(void)
{
    int n = 5;
    int arr[] = {3, 4, 2, 1, 5};

    cout << "Before Sort:\t";
    print_arr(arr, n);
    insertionSort(arr, n);
    cout << "After Sort:\t";
    print_arr(arr, n);

    return 0;
}