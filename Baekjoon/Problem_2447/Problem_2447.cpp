#include <iostream>

using namespace std;

bool IsStar(const int x, const int y, int num)
{
    if((x / num) % 3 == 1 && (y / num) % 3 == 1)
    {
        return false;
    }
    else
    {
        if(num / 3 == 0) return true;
        else return IsStar(x, y, num / 3);
    }
}

void Print_Star(const int num)
{
    for(int i = 0; i < num; i++)
    {
        for(int j = 0; j < num; j++)
        {
            if(IsStar(i, j, num)) cout << '*';
            else cout << ' ';
        }
        cout << endl;
    }
}

int  main(void)
{
    int num; cin >> num;

    Print_Star(num);
    
    return 0;
}