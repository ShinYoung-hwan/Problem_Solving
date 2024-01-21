#include <stdio.h>
#include <stdlib.h>

typedef enum { false, true } bool;
typedef int Key;

typedef struct _BSTNode
{
    Key key;
    struct _BSTNode *left_child;
    struct _BSTNode *right_child;
} BSTNode;

// 새 노드를 생성한다.
BSTNode* createNode(Key key){
    BSTNode* node = (BSTNode *)malloc(sizeof(BSTNode));
    node->key = key;
    node->left_child = NULL;
    node->right_child = NULL;

    return node;
} 
// 노드를 삭제한다.
void destroyNode(BSTNode* node){
    free(node);
}

// 주어지는 트리가 이진탐색트리인지 아닌지 확인한다.
// key(모든 왼쪽 서브트리의 노드) < key(현재 노드) < key(모든 오른쪽 서브트리의 노드)를 만족하는지 확인한다.
bool verify(BSTNode* root, int min, int max){
    if(root != NULL){
        // BST 조건 민족 X
        if(root->key < min || root->key > max) return false;
        else
            return verify(root->left_child, min, root->key) &&
                verify(root->right_child, root->key, max);

    } else // 말단 노드일 경우
        return true;
}
// BST에서 원소를 찾는다.
BSTNode* search(BSTNode* root, Key key){
    BSTNode* cur = root;
    while (cur != NULL){
        if (cur->key == key) break;
        else if (cur->key > key) cur = root->left_child;
        else cur = root->right_child;
    }
    return cur;
}
// BST에 원소를 삽입한다.
void insert(BSTNode* root, Key key){
    BSTNode* cur = root;
    while (cur != NULL){
        if (cur->key == key) exit(1);
        else if(cur->key > key){ // left child
            if(cur->left_child == NULL){
                cur->left_child = createNode(key);
                break;
            } else{
                cur = cur->left_child;
            }
        } else{ // right child
            if(cur->right_child == NULL){
                cur->right_child = createNode(key);
                break;
            } else{
                cur = cur->right_child;
            }
        }
    }
}
// BST에서 원소를 삭제한다.
void removeKey(BSTNode* root, Key key){
    BSTNode* cur = root, * parent = NULL;

    // 삭제하려는 노드를 찾는다.
    while(cur != NULL && cur->key != key){
        parent = cur;
        if (cur->key > key) cur = cur->left_child;
        else cur = cur->right_child;
    }

    // 삭제하려는 노드가 존재하지 않는다.
    if(cur == NULL) exit(1);

    // 1. 삭제하려는 노드에 자식 노드가 없는 경우
    if (cur->left_child == NULL && cur->right_child == NULL){
        if(parent != NULL){
            if(parent->left_child == cur) parent->left_child = NULL;
            else parent->right_child = NULL;
        } else{ // 현재 노드가 루트 노드인 경우
            cur = NULL;
        }
    }
    // 2. 삭제하려는 노드에 자식 노드가 1개인 경우
    else if (cur->left_child == NULL || cur->right_child == NULL){
        // child node 가져오기
        BSTNode* child;
        if (cur->left_child != NULL) child = cur->left_child;
        else child = cur->right_child;

        if (parent != NULL){
            if(parent->left_child == cur) parent->left_child = child;
            else parent->right_child = child;
        }
    }
    // 3. 삭제하려는 노드에 자식 노드가 2개인 경우
    else{
        BSTNode* succ_parent = cur, *succ = cur->right_child;

        // successor node를 찾는다.
        while (succ->left_child != NULL){
            succ_parent = succ;
            succ = succ->left_child;
        }

        // successor가 자식 노드를 갖고 있다면 자식 노드들을 최신화한다.
        if (succ_parent->right_child == succ) succ_parent->right_child = succ->right_child;
        else succ_parent->left_child = succ->right_child;

        cur->key = succ->key;
        cur = succ;
    }

    destroyNode(cur);
}