#include <stdio.h>
#include <stdlib.h>

#define MAX_DEQ 10

typedef enum { false, true } bool;
typedef int Data;

typedef struct{
    Data items[MAX_DEQ];
    int front, rear;
} Deq;

void initDeq(Deq *pdeq){
    pdeq->front = 0;
    pdeq->rear = 1;
}
bool isFull(Deq *pdeq){
    return pdeq->front == pdeq->rear;
}
bool isEmpty(Deq *pdeq){
    return (pdeq->front + 1) % MAX_DEQ == pdeq->rear;
}

void addFront(Deq *pdeq, Data element){
    if (isFull(pdeq)){
        exit(1);
    }
    pdeq->items[pdeq->front--] = element;
    pdeq->front = pdeq->front >= 0 ? pdeq->front : MAX_DEQ - 1;
} void addRear(Deq *pdeq, Data element){
    if (isFull(pdeq)){
        exit(1);
    }
    pdeq->items[pdeq->rear] = element;
    pdeq->rear = (pdeq->rear + 1) % MAX_DEQ;
}
Data removeFront(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    Data item = pdeq->items[pdeq->front + 1];
    pdeq->front = (pdeq->front + 1) % MAX_DEQ;
    return item;
} Data removeRear(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    pdeq->rear -= 1;
    pdeq->rear = pdeq->rear >= 0 ? pdeq->rear : MAX_DEQ - 1;
    Data item = pdeq->items[pdeq->rear];
    return item;
}
Data peekFront(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    return pdeq->items[pdeq->front + 1];
} Data peekRear(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    return pdeq->items[pdeq->rear];
}

void printDeq(Deq *pdeq){
    // front에서 rear까지 하나하나 출력하기
    printf("Front(%d) - ", pdeq->front+1);

    int front = (pdeq->front + 1) % MAX_DEQ;
    while (front != pdeq->rear){
        printf("%d ", pdeq->items[front]);
        front = (front + 1) % MAX_DEQ;
    }

    printf("- Rear(%d)\n", pdeq->rear);
}

int main(){
    Deq deq;
    initDeq(&deq);

    for (int i = 0; i < 9; i++){
        if (i % 2 == 0){
            addFront(&deq, i);
        }
        else {
            addRear(&deq, i);
        }
    }
    printDeq(&deq);

    for (int i = 0; i < 5; i++){
        printf("%d ", removeRear(&deq));
    }
    printDeq(&deq);

    return 0;
}