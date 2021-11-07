#include <stdio.h>
#include <stdlib.h>

typedef enum{ False, True }bool;
typedef int Data;

typedef struct
{	/* This is a data structure that performs like vector in C++ */
	int size;
	int curLen;
	Data *items;
} DynamicList;

void initDynamicList(DynamicList *plist)
{	// initialize the dynamicList //
	plist->size = 1;
	plist->curLen = 0;
	plist->items = (Data *)malloc(sizeof(Data)*plist->size);
}
void destroyDynamicList(DynamicList *plist)
{
	plist->size = 1;
	plist->curLen = 0;
	free(plist->items);
}
bool isListFull(DynamicList *plist)
{	
	return plist->size == plist->curLen;
}
bool isListEmpty(DynamicList *plist)
{
	return plist->curLen == 0;
}

void adjustDynamicList(DynamicList *plist)
{	// double the list size //
	Data *backup = plist->items;
	Data *tmpptr;
	if(tmpptr = realloc(plist->items, 2*sizeof(Data)*(plist->size)))
	{	// none error //
		plist->size = 2 * plist->size;
		plist->items = tmpptr;
	}
	else
	{	// error case //
		printf("Reallocation failed\n");
		plist->items = backup;
	}
}
void addKthItem(DynamicList *plist, Data item, int k)
{	// add item in kth position //
	if(isListFull(plist))
	{
		adjustDynamicList(plist);
	}

	for(int i = plist->curLen; i > k; i--)
	{
		plist->items[i] = plist->items[i-1];
	}
	plist->items[k] = item;
	plist->curLen++;
}
void addLastItem(DynamicList *plist, Data item)
{	// add item in last position //
	if(isListFull(plist))
	{
		adjustDynamicList(plist);
	}

	plist->items[plist->curLen++] = item;
}
void removeKthItem(DynamicList *plist, int k)
{	// remove item in k-th position //
	if(k < 0 || k > plist->curLen)
	{
		printf("Out of range, the current length is %d\n", plist->curLen);
		exit(1);
	}

	for(int i = k; i < (plist->curLen-1); i++)
	{
		plist->items[i] = plist->items[i+1];
	}
	plist->curLen--;
}
void removeLastItem(DynamicList *plist)
{
	plist->curLen--;
}

Data getKthItem(DynamicList *plist, int k)
{	// return kth item is list //
	if(k < 0 || k > plist->curLen)
	{
		printf("Out of range, the current length is %d\n", plist->curLen);
		exit(1);
	}

	return plist->items[k];
}

void printDynamicListInfo(DynamicList *plist)
{	// print dynamic list information //
	printf("Dynamic List\n");
	printf("Size: %d\n", plist->size);
	printf("Current Length: %d\n", plist->curLen);
	printf("Items: ");
	for(int i = 0; i < plist->curLen; i++)
		printf("%d ", getKthItem(plist, i));
	printf("NULL\n");
}