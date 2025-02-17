#include <iostream>

typedef struct 
{
    bool isUsed;
    int item;
} Data;

Data data[21][21][21] = {0, };

int func_w(const int a, const int b, const int c);
int calculate(const int a, const int b, const int c);

bool isNegOnes(const int a, const int b, const int c)
{
    return (a == -1 && b == -1 && c == -1);
}

int main(void)
{
    int a, b, c;

    while((std::cin >> a >> b >> c))
    {
        if(isNegOnes(a, b, c))
            break;

        printf("w(%d, %d, %d) = %d\n",  a, b, c, func_w(a, b, c));
    }
    return 0;
}

int func_w(const int a, const int b, const int c)
{
    if(a <= 0 || b <= 0 || c <= 0)
    {
        return 1;
    }
    else if(a > 20 || b > 20 || c > 20)
    {
        return calculate(20, 20, 20);
    }
    else if(a < b && b < c)
    {
        return calculate(a, b, c-1) + calculate(a, b-1, c-1) - calculate(a, b-1, c);
    }

    return calculate(a-1, b, c) + calculate(a-1, b-1, c) + calculate(a-1, b, c-1) - calculate(a-1, b-1, c-1);
}

int calculate(const int a, const int b, const int c)
{
    if(!data[a][b][c].isUsed)
    {   // dp technique //
        data[a][b][c].isUsed = true;
        data[a][b][c].item = func_w(a, b, c);
    }
    return data[a][b][c].item;
}