#include <stdio.h>
#include "segment_tree.h"

int main() {
    Item arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    build(arr, 0, 10-1, 1);
    printf("%d\n", get_partial_sum(0, 10-1, 4, 5, 1));
    print_segment_tree();

    update(0, 10-1, 5, 15, 1); // arr[5] = 6 => arr[5] = 15
    printf("%d\n", get_partial_sum(0, 10-1, 4, 5, 1));
    print_segment_tree();

    return 0;
}