#include "static_max_heap.h"

typedef MaxHeap PQueue;

void initPQueue(PQueue *ppqueue)
{
    initHeap(ppqueue);
}
bool isPQEmpty(PQueue *ppqueue)
{
    return isHeapEmpty(ppqueue);
}
bool isPQFull(PQueue *ppqueue)
{
    return isHeapFull(ppqueue);
}

void enqueue(PQueue *ppqueue, Data data, int priority)
{   // insert an item to the priority queue //
    insertItem(ppqueue, data, priority);
}
Data dequeue(PQueue *ppqueue)
{   // delete an item to the priority queue //
    return deleteItem(ppqueue);
}

