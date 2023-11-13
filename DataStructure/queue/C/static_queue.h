/* It is a circular queue based on array
 */
#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE 100

typedef enum{ False, True } bool;
typedef int Data;

typedef struct
{
    int front, rear;
    Data items[MAX_QUEUE];
} Queue;

void initQueue(Queue *pqueue)
{   // make a queue empty //
    pqueue->front = pqueue->rear = 0;
}
bool inQueueFull(Queue *pqueue)
{   // check whether a queue is full //
    return pqueue->front == ((pqueue->rear + 1) % MAX_QUEUE);
}
bool isQueueEmpty(Queue *pqueue)
{   // check whether a queue is empty
    return pqueue->front == pqueue->rear;
}

Data peekQueue(Queue *pqueue)
{   // read the item at the front //
    if(isQueueEmpty(pqueue))
    {
        perror("error: empty queue");
        exit(1);
    }
    return pqueue->items[pqueue->front];
}
void enqueue(Queue *pqueue, Data item)
{   // insert an item at the rear //
    if(inQueueFull(pqueue))
    {
        perror("error: full queue");
        exit(1);
    }
    pqueue->items[pqueue->rear] = item;
    pqueue->rear = (pqueue->rear+1) % MAX_QUEUE;
}
Data dequeue(Queue *pqueue)
{   // remove an item from the front //
    Data item = peekQueue(pqueue);
    pqueue->front = (pqueue->front+1) % MAX_QUEUE;
    return item;
}
