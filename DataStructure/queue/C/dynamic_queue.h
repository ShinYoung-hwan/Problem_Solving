#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE 100

typedef enum { false, true } bool;
typedef int Data;

typedef struct {
    int front, rear;
    Data items[MAX_QUEUE];
} Queue;

void initQueue(Queue *pqueue);              // 큐의 초기화 연산
bool isFull(Queue *pqueue);                 // 큐가 가득찼는지 확인
bool isEmpty(Queue *pqueue);                // 큐가 비어있는지 확인

Data peek(Queue *pqueue);                   // 큐의 front 값을 확인
void enqueue(Queue *pqueue, Data element);  // 큐의 rear에 원소 삽입
Data dequeue(Queue *pqueue);                // 큐의 front에서 원소 삭제

// 큐의 초기화. 정적 큐이므로 front와 rear의 초기 위치만 설정해준다.
// 전부 0으로 초기화해주었다는 것은 삽입시 rear++을 사용한다는 의미이고, 삭제시 front++을 사용한다는 의미이다.
void initQueue(Queue *pqueue){
    pqueue->front = pqueue->rear = 0;
}
// 큐가 가득찼는지 확인한다. 순환 큐의 구조로 구현하였으므로 나머지 연산을 이용해 마지막 인덱싱을 넘어가면 0으로 돌아가게 한다.
// 다만 구조적으로 가득찬 것과 비어있는 것을 구분하기 위해 1칸은 공백으로 나둔다.
bool isFull(Queue *pqueue){
    return pqueue->front == (pqueue->rear + 1) % MAX_QUEUE;
}
// 큐가 비어있는지 확인한다. front와 rear의 위치가 같은 경우 큐는 비어있다.
bool isEmpty(Queue *pqueue){
    return pqueue->front == pqueue->rear;
}

// 큐의 front에 있는 원소를 반환한다.
Data peek(Queue *pqueue){
    if (isEmpty(pqueue)){
        exit(1);
    }
    return pqueue->items[pqueue->front];
}
// 큐의 rear에 원소를 삽입한다.
void enqueue(Queue *pqueue, Data element){
    if (isFull(pqueue)){
        exit(1);
    }
    pqueue->items[pqueue->rear] = element;
    pqueue->rear = (pqueue->rear + 1) % MAX_QUEUE;
}
// 큐의 front에서 원소를 삭제한다.
Data dequeue(Queue *pqueue){
    if (isEmpty(pqueue)){
        exit(1);
    }
    Data element = pqueue->items[pqueue->front];
    pqueue->front = (pqueue->front + 1) % MAX_QUEUE;
    return element;
}