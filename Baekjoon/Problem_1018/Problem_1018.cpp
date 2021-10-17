#include <iostream>
#include <string>

using namespace std;

string* Set_Board(size_t N)
{
    string* Board = new string[N];
    for(int i = 0; i < N; i++)
    {
        cin >> Board[i];
    }

    return Board;
}

int Get_MinErr(string* Board, int N, int M)
{
    int min1 = 0, min2 = 0;

    for(int i = 0; i < N; i++)
    {
        if(i % 2 == 0)
        {
            for(int j = 0; j < M; j++)
            {
                if(j % 2 == 0)
                {
                    if(Board[i].at(j) == 'B') min1++;
                }
                else
                {
                    if(Board[i].at(j) == 'W') min1++;
                }
            }
        }
        else
        {
            for(int j = 0; j < M; j++)
            {
                if(j % 2 == 0)
                {
                    if(Board[i].at(j) == 'W') min1++;
                }
                else
                {
                    if(Board[i].at(j) == 'B') min1++;
                }
            }
        }
    }

    for(int i = 0; i < N; i++)
    {
        if(i % 2 == 0)
        {
            for(int j = 0; j < M; j++)
            {
                if(j % 2 == 0)
                {
                    if(Board[i].at(j) == 'W') min2++;
                }
                else
                {
                    if(Board[i].at(j) == 'B') min2++;
                }
            }
        }
        else
        {
            for(int j = 0; j < M; j++)
            {
                if(j % 2 == 0)
                {
                    if(Board[i].at(j) == 'B') min2++;
                }
                else
                {
                    if(Board[i].at(j) == 'W') min2++;
                }
            }
        }
    }

    return (min1 > min2 ? min2 : min1);
}

int main(void)
{
    int N, M; cin >> N >> M;

    string* Board = Set_Board(N);

    cout << Get_MinErr(Board, N, M) << endl;

    return 0;
}