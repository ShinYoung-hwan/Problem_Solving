#include <cstdio>

using namespace std;
const int SIZE = 20;
int get_element_of_sum_of_sequence(const int);

int sequence[SIZE] = { 1, 3, };
int sum_of_sequence[SIZE] = { 1, };
int get_element_of_sequence(const int N) { 
    // base
    if (sequence[N]) return sequence[N];

    // default
    return sequence[N] = get_element_of_sequence(N-1) * sequence[1] + 2 * get_element_of_sum_of_sequence(N-2);
} 
int get_element_of_sum_of_sequence(const int N) {
    // base
    if (sum_of_sequence[N]) return sum_of_sequence[N];

    // default
    return sum_of_sequence[N] = get_element_of_sum_of_sequence(N-1) + get_element_of_sequence(N);
}

int main() {
    int N; scanf("%d", &N);

    if (N % 2) printf("0\n");
    else {
        printf("%d\n", get_element_of_sequence(N/2));
    }
    
    return 0;
}