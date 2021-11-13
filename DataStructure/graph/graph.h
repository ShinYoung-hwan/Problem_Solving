#include <stdio.h>
#include <stdlib.h>
#include <static_stack.h>
#include <static_queue.h>

typedef struct _GNode
{   // node of graph //
    int id;
    struct _GNode *next;
} GNode;

typedef struct
{   // graph struct //
    int num;
    GNode ** heads;
} Graph;

// Basic operation of graph //
void createGraph(Graph *pgraph, const int num)
{   // create a graph //
    pgraph->num = num;
    pgraph->heads = (GNode **)malloc(sizeof(GNode *) * num);
    for(int i = 0; i < num; i++)
    {   // make a dummy node //
        pgraph->heads[i] = (GNode *)malloc(sizeof(GNode));
        pgraph->heads[i]->next = NULL;
    }
}
void destroyGraph(Graph *pgraph)
{   // destory a graph //
    for(int i = 0; i < pgraph->num; i++)
    {
        GNode *cur = pgraph->heads[i];
        while(cur != NULL)
        {
            GNode *tmp = cur;
            cur = cur->next;
            free(tmp);
        }
    }
    free(pgraph->heads);
}
void addEdge(Graph *pgraph, const int src, const int dst)
{   // add an undirected edge from src to dst //
    GNode *newNode1, *newNode2, *cur;

    newNode1 = (GNode *)malloc(sizeof(GNode));
    newNode1->id = dst;
    newNode1->next = NULL;

    cur = pgraph->heads[src];
    while(cur->next != NULL)
        cur = cur->next;
    cur->next = newNode1;

    newNode2 = (GNode *)malloc(sizeof(GNode));
    newNode2->id = src;
    newNode2->next = NULL;

    cur = pgraph->heads[dst];
    while(cur->next != NULL)
        cur = cur->next;
    cur->next = newNode2;
}
void printGraph(Graph *pgraph)
{   // print a graph for each vertex //
    for(int i = 0; i < pgraph->num; i++)
    {
        GNode *cur = pgraph->heads[i];
        while(cur != NULL)
        {
            printf("%d ", cur->id);
            cur = cur->next;
        }
        printf("\n");
    }
}

// Graph traversal //
void DFS(Graph *pgraph)
{   // depth first search //
    Stack stack;
    bool *visited = (bool *)malloc(sizeof(bool) * pgraph->num);
    for(int i = 0; i < pgraph->num; i++)
    {   // make all vertices unvisited //
        visited[i] = False;
    }

    initStack(&stack);
    pushStack(&stack , 0); // push the initial vertex //
    while(isStackEmpty(&stack))
    {
        GNode *cur;
        int vtx = popStack(&stack);
        
        // skip if the vertex has been visited //
        if(visited[vtx]) continue;
        else{
            visited[vtx] = True;
            printf("%d ", vtx);
        }

        // push the vertex if it has not been visited //
        cur = pgraph->heads[vtx]->next;
        while(cur != NULL)
        {
            if(!visited[cur->id])
                pushStack(&stack, cur->id);
            cur = cur->next;
        }
    }
}
void BFS(Graph *pgraph)
{   // breadth first search //
    Queue queue;
    bool *visited = (bool *)malloc(sizeof(bool) * pgraph->num);
    for(int i = 0; i < pgraph->num; i++)
    {   // make all vertices unvisited //
        visited[i] = False;
    }

    initQueue(&queue);
    enqueue(&queue, 0);
    while(!isQueueEmpty(&queue))
    {
        GNode *cur;
        int vtx = dequeue(&queue);

        // skip if the vertex has been visited //
        if(visited[vtx]) continue;
        else{
            visited[vtx] = True;
            printf("%d ", vtx);
        }

        // enqueue the vertex if it has not been visited //
        cur = pgraph->heads[vtx]->next;
        while(cur != NULL)
        {
            if(!visited[cur->id])
                enqueue(&queue, cur->id);
            cur = cur->next;
        }
    }
}