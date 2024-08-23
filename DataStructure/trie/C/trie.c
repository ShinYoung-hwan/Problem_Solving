#include <stdio.h>
#include "trie.h"

int main() {
    init_tree();

    char str1[] = "hello";
    char str2[] = "world";

    insert(str1);
    insert(str2);

    printf("%s\n", search(str1) ? "true": "false");
    printf("%s\n", search("nope") ? "true": "false");
    printf("%s\n", search(str2) ? "true": "false");

    clear_tree(head);
    return 0;
}