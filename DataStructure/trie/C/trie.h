#include <stdlib.h>
#include <string.h>

#define MAXALPHABET 26

typedef enum { false, true } bool;

typedef struct _trieNode {
    char key;
    char *data;
    struct _trieNode *children[26];
} TrieNode;

TrieNode *head = NULL;

TrieNode *create_node() {
    TrieNode *node = (TrieNode *)malloc(sizeof(TrieNode));
    node->data = NULL;
    for (int i = 0; i < MAXALPHABET; i++) node->children[i] = NULL;

    return node;
}

void init_tree() {
    head = create_node();
}

void clear_tree(TrieNode *cur) {
    for (int i = 0; i < MAXALPHABET; i++) {
        if (cur->children[i] == NULL) continue;

        clear_tree(cur->children[i]);
    }

    free(cur);
}

void insert(char *str) {
    TrieNode *cur = head;

    int end = strlen(str);
    for (int i = 0; i < end; i++) {
        char c = str[i];

        if (cur->children[c-'a'] == NULL) {
            cur->children[c-'a'] = create_node();
            cur->children[c-'a']->key = c;
        }

        cur = cur->children[c-'a'];
    }
    cur->data = str;
}

bool search(char *str) {
    TrieNode *cur = head;

    int end = strlen(str);
    for (int i = 0; i < end; i++) {
        char c = str[i];

        if (cur->children[c-'a'] == NULL) return false;

        cur = cur->children[c-'a'];
    }
    
    if (cur->data == NULL) return false;
    else if (strcmp(str, cur->data) != 0) return false;
    return true;
}