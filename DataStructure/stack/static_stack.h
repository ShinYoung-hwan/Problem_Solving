#define MAX_STACK 100

typedef enum { False, True } bool;
typedef int Data;

typedef struct
{
    Data items[MAX_STACK];
    int top
} Stack;

void initStack(Stack *pstack)
{   // Make stack empty //
    pstack->top = -1;
}
bool isStackEmpty(Stack *pstack)
{   // Check whether stack is empty //
    return pstack->top == -1;
}
bool isStackFull(Stack *pstack)
{   // Check whether stack is full //
    return pstack->top == MAX_STACK - 1; 
}

Data peekStack(Stack *pstack)
{   // Read the item at the top
    if(isStackEmpty(pstack))
    {
        perror("The stack is empty!\n");
        exit(1);
    }
    return pstack->items[pstack->top];
}
void pushStack(Stack *pstack, Data item)
{
    if(isStackFull(pstack))
    {
        perror("The stack is full!\n");
        exit(1);
    }
    pstack->items[++(pstack->top)] = item;
}
Data popStack(Stack *pstack)
{
    Data item = peekStack(pstack);
    if(isStackEmpty(pstack))
    {
        perror("The stack is empty!\n");
        exit(1);
    }
    (pstack->top)--;
    return item;
}
void popMultiStack(Stack *pstack, int times)
{
	if(times <= 0)
		perror("Can not pop smaller than 1 times");

	for(int i = 0; i < times; i++)
		popStack(pstack);
}
