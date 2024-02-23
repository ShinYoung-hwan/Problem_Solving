#include <iostream>

using namespace std;

void quick_sort(int* arr, const int n) {

}

void print_arr(const int arr[], const int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i];
    }
    cout << endl;
}
int main() {
    int n = 5;
    int arr[] = {3, 2, 2, 1, 5};

    cout << "Before Sort:\t";
    print_arr(arr, n);
    quick_sort(arr, n);
    cout << "After Sort:\t";
    print_arr(arr, n);

    return 0;
}