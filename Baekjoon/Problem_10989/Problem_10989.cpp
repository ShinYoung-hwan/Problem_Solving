#include <iostream>
#include <cstdio>

const int TABLE_SIZE = 10001;

void setDatas(int *tables, const int N)
{
    int num;
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &num);
        tables[num]++;
    }
}

void printDatas(int *tables)
{
    for(int i = 1; i < TABLE_SIZE; i++)
    {
        for(int j = 0; j < tables[i]; j++)
        {
            printf("%d\n", i);
        }
    }
}

int main(void)
{
    int N; scanf("%d", &N);
    int tables[TABLE_SIZE] = {0, }; setDatas(tables, N);

    printDatas(tables);
    
    return 0;
}