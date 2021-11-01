#include <stdio.h>
#include <stdlib.h>

typedef enum{ False, True } bool;
typedef int Data;

typedef struct _Node
{
    Data item;
    struct _Node *next;
} Node;

typedef struct
{
    Node *head;
    int len;
} LinkedList;

void initLinkedList(LinkedList *plist)
{   // Make a list empty //
    // create a dummy node //
    plist->head = (Node *)malloc(sizeof(Node));
    plist->head->next = NULL;
    plist->len = 0;
}
bool isLinkedListEmpty(LinkedList *plist)
{   // check whether the list is empty //
    return plist->len == 0;
}

void insertMiddle(LinkedList *plist, int pos, Data item)
{   // insert an item at the k-th position
    Node *cur, *newNode;
    if(pos < 0 || pos > plist->len)
    {
        perror("out of range of list");
        exit(1);
    }

    // create a new node //
    newNode = (Node *)malloc(sizeof(Node));
    newNode->item = item;
    newNode->next = NULL;

    // Move the cur pointer to the (k-1)-th position
    cur = plist->head;
    for(int i = 0; i < pos; i++)
        cur = cur->next;
    
    // insert the new node to the k-th position
    newNode->next = cur->next;
    cur->next = newNode;
    plist->len++;
}
void removeMiddle(LinkedList *plist, int pos)
{   // remove an item at the k-th position //
    Node *cur, *temp;
    if(isLinkedListEmpty(plist) || pos < 0 || pos >= plist->len)
    {
        perror("out of range of list");
        exit(1);
    }

    // move the cur pointer to the (k-1)-th position //
    for(int i = 0; i < pos; i++)
        cur = cur->next;
    
    // remove the node to the k-th position //
    temp = cur->next;
    temp->next = cur->next->next;
    plist->len--;
    free(temp);
}
Data readItem(LinkedList *plist, int pos)
{   // read an item at the k-th position //
    Node *cur;
    if(isLinkedListEmpty(plist) || pos < 0 || pos >= plist->len)
    {
        perror("out of range of list");
        exit(1);
    }

    // move the cur pointer to the k-th position //
    cur = plist->head->next;
    for(int i = 0; i < pos; i++)
        cur = cur->next;
    
    return cur->item;
}

void printLinkedList(LinkedList *plist)
{
    Node *cur;
    if(isLinkedListEmpty(plist))
    {
        perror("out of range of list");
        exit(1);
    }

    cur = plist->head;
    for(int i = 0; i < plist->len; i++)
        printf("%dth: %d -> ", i+1, cur->item);
    //for(Node *cur = plist->head->next; cur != NULL; cur = cur->next)
    //    printf("%d -> ", cur->item);
    printf("NULL");    
}
void clearList(LinkedList *plist)
{
    while(plist->head->next != NULL)
        removeMiddle(plist, 0);
    free(plist->head);
}

LinkedList *concatenate(LinkedList *plist1, LinkedList *plist2)
{
    if(plist1->head->next == NULL) return plist2;
    else if(plist2->head->next == NULL) return plist1;
    else
    {   // move the current pointer to the last position //
        Node *cur = plist1->head->next;
        while(cur->next != NULL)
            cur = cur->next;

        // link the curent poointer to the second list;
        cur->next = plist2->head->next;

        // remove the dummy node from the second list //
        free(plist2->head);
        return plist1;;
    }
}