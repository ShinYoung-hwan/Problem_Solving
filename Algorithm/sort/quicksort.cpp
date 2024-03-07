#include <iostream>

using namespace std;

void print_arr(const int arr[], const int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i];
    }
    cout << endl;
}

int get_pivot(int* arr, const int left, const int right) {
    return arr[(left+right)/2];
}

void quick_sort(int* arr, const int left, const int right) {
    // base case
    if (left >= right) return;

    // Divide
    int i = left, j = right;
    int pivot = get_pivot(arr, left, right);
    int tmp;
    while (i <= j) {
        while (arr[i] < pivot) i++; // 피벗 왼쪽에서 피벗보다 큰 것을 찾는다.
        while (pivot < arr[j]) j--; // 피벗 오른쪽에서 피벗보다 작은 것을 찾는다.

        // swap
        if (i <= j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;

            printf("pivot is %d swap %dth %dth: ", pivot, i, j);
            print_arr(arr, 5);

            i++; j--;
            
        }
    }
    // Conquer
    quick_sort(arr, left, j);
    quick_sort(arr, i, right);
}

int main() {
    int n = 5;
    int arr[] = {3, 4, 2, 1, 5};

    cout << "Before Sort:\t";
    print_arr(arr, n);
    quick_sort(arr, 0, n-1);
    cout << "After Sort:\t";
    print_arr(arr, n);

    return 0;
}