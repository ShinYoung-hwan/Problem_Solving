#include <iostream>

using namespace std;

int main(void)
{
    char Chess[8][8];
    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            cin >> Chess[i][j];
        }
    }
    int OnWhite = 0;
    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            if(i % 2 == 0)
            {
                if(j % 2 == 0 && Chess[i][j] == 'F') OnWhite++;
            }
            else
            {
                if(j % 2 == 1 && Chess[i][j] == 'F') OnWhite++;
            }
        }
    }

    cout << OnWhite << endl;

    return 0;
}