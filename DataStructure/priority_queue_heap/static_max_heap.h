#define MAX_HEAP 100

typedef enum { False, True } bool;
typedef char Data;

typedef struct 
{
    Data data;
    int priority;
} HNode;
typedef struct
{
    HNode items[MAX_HEAP + 1];
    int num;
} MaxHeap;

void initHeap(MaxHeap *pheap)
{   // make a heap empty //
    pheap->num = 0;
} 
bool isHeapEmpty(MaxHeap *pheap)
{   // check whether a heap is empty //
    return pheap->num == 0;
}
bool isHeapFull(MaxHeap *pheap)
{   // check whether a heap is full //
    return pheap->num == MAX_HEAP;
}

int getParent(int idx)
{   // get a parent index for a given index //
    return idx / 2;
}
int getLChild(int idx)
{   // get a left child index for a given index //
    return idx * 2;
}
int getRChild(int idx)
{   // get a right child index for a given index //
    return idx * 2 + 1;
}
int getHighPriorityChild(MaxHeap *pheap, int idx)
{   // get a child index with high priority between two child nodes //
    if(getLChild(idx) > pheap->num)
    {   // no child nodes exist //
        return 0;
    } else if(getLChild(idx) == pheap->num)
    {   // exish a left child only //
        return getLChild(idx);        
    } else
    {   // choose a child node with the highest priority //
        int left = getLChild(idx), right = getRChild(idx);
        if(pheap->items[left].priority > pheap->items[right].priority)
            return left;
        else
            return right;
    }
}

void insertItem(MaxHeap *pheap, Data data, int priority)
{   // insert a node to the heap //
    HNode newNode;
    int idx = pheap->num + 1;
    if(isHeapFull(pheap)) return;

    // compare the new node with its parents //
    while(idx > 1)
    {
        int parent = getParent(idx);
        if(priority > pheap->items[parent].priority)
        {
            pheap->items[idx] = pheap->items[parent];
            idx = parent;
        }
        else break;
    }
    newNode.data = data;
    newNode.priority = priority;

    pheap->items[idx] = newNode;
    pheap->num++;
}
Data deleteItem(MaxHeap *pheap)
{   // remove the maximum data from the heap //
    Data max = pheap->items[1].data;
    HNode last = pheap->items[pheap->num];
    int parent =1 , child;
    
    // compare the root with its child nodes //
    while (child == getHighPriorityChild(pheap, parent))
    {
        if(last.priority < pheap->items[child].priority)
        {
            pheap->items[parent] = pheap->items[child];
            parent = child;
        }
        else break;
    }

    pheap->items[parent] = last;
    pheap->num--;

    return max;    
}