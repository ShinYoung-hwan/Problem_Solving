#include <stdio.h>
#include <stdlib.h>

#define MAX_DEQ 100

typedef enum { false, true } bool;
typedef int Data;

typedef struct{
    Data items[MAX_DEQ];
    int front, rear;
} Deq;

// 덱 초기화 연산
// 각 원소를 넣어야할 위치를 지정. 조회 및 삭제 연산시에는 1칸 옆의 값을 조회, 삭제해야함.
void initDeq(Deq *pdeq){
    
    pdeq->front = 0;
    pdeq->rear = 1;
}
// 덱 가득찼는지 확인하는 연산
bool isFull(Deq *pdeq){
    return pdeq->front == pdeq->rear;
}
// 덱이 비어있는지 확인하는 연산
bool isEmpty(Deq *pdeq){
    return (pdeq->front + 1) % MAX_DEQ == pdeq->rear;
}

// 덱의 front에 원소를 삽입하는 연산
void addFront(Deq *pdeq, Data element){
    if (isFull(pdeq)){
        exit(1);
    }
    pdeq->items[pdeq->front--] = element;
    pdeq->front = pdeq->front >= 0 ? pdeq->front : MAX_DEQ - 1;
} 
// 덱의 rear에 원소를 삽입하는 연산
void addRear(Deq *pdeq, Data element){
    if (isFull(pdeq)){
        exit(1);
    }
    pdeq->items[pdeq->rear] = element;
    pdeq->rear = (pdeq->rear + 1) % MAX_DEQ;
}
// 덱의 front에서 원소를 삭제하는 연산
Data removeFront(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    pdeq->front = (pdeq->front + 1) % MAX_DEQ;
    Data item = pdeq->items[pdeq->front];
    return item;
} 
// 덱의 rear에서 원소를 삭제하는 연산
Data removeRear(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    pdeq->rear -= 1;
    pdeq->rear = pdeq->rear >= 0 ? pdeq->rear : MAX_DEQ - 1;
    Data item = pdeq->items[pdeq->rear];
    return item;
}
// 덱의 front 원소를 조회하는 연산
Data peekFront(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    return pdeq->items[(pdeq->front + 1) % MAX_DEQ];
}
// 덱의 rear 원소를 조회하는 연산
Data peekRear(Deq *pdeq){
    if (isEmpty(pdeq)){
        exit(1);
    }
    return pdeq->items[(pdeq->rear) > 0 ? pdeq->rear - 1 : MAX_DEQ - 1];
}