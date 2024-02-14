#include <iostream>

using namespace std;

void print_arr(const int* arr, const int n){
    for (int i = 0; i < n; i++){
        cout << arr[i] << ' ';
    }
    cout << endl;
}

void selection_sort(int* arr, const int n){
    int tmp, min_idx;
    for (int i = 0; i < n - 1; i++){
        // 최솟값 찾기
        min_idx = i;
        for (int j = i + 1; j < n; j++){
            min_idx = arr[min_idx] < arr[j] ? min_idx : j;
        }
        tmp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = tmp;
        printf("Swap %dth, %dth\t", i+1, min_idx+1);
        print_arr(arr, n);
    }
}

int main(){
    int n = 5;
    int arr[] = {3, 2, 2, 1, 5};

    cout << "Before Sort:\t";
    print_arr(arr, n);
    selection_sort(arr, n);
    cout << "After Sort:\t";
    print_arr(arr, n);

    return 0;
}