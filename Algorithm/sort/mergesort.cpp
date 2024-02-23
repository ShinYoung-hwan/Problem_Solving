#include <iostream>

using namespace std;

void print_arr(const int *arr, const int n){
    for (int i = 0; i < n; i++){
        cout << arr[i] << ' ';
    }
    cout << endl;
}

void merge(int *arr, const int n, const int left, const int mid, const int right) {
    int *sorted = new int[n];

    // 두 배열에서 차례대로 정렬 순으로 복사
    int i = left, j = mid + 1;
    int k = left;
    while (i <= mid && j <= right) {
        if (arr[i] < arr[j]) {
            sorted[k++] = arr[i++];
        } else {
            sorted[k++] = arr[j++];
        }
    }

    // 남아있는 값 복사
    while (i <= mid) {
        sorted[k++] = arr[i++];
    } while (j <= right) {
        sorted[k++] = arr[j++];
    }

    // 정렬된 내용을 기존 배열에 반영
    for (i = left; i <= right; i++) {
        arr[i] = sorted[i];
    }

    delete[] sorted;
}

void merge_sort(int *arr, const int n, const int left, const int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        merge_sort(arr, n, left, mid);
        merge_sort(arr, n, mid+1, right);
        merge(arr, n, left, mid, right);
        printf("sort arr[%d:%d]:\t", left, right);
        print_arr(arr, n);
    }
}

int main(){
    int n = 5;
    int arr[] = {3, 2, 2, 1, 5};

    cout << "Before Sort:\t";
    print_arr(arr, n);
    merge_sort(arr, n, 0, n-1);
    cout << "After Sort:\t";
    print_arr(arr, n);
    return 0;
}