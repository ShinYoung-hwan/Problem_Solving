#include <iostream>
#include <vector>
#include <utility>

using namespace std;

bool isSameRow(const vector<vector<int>> board, const pair<int, int> pos, const int size)
{
    for(int j = 0; j < size; j++)
    {
        if(board[pos.first][j])
            return true;
    }
    return false;
}
bool isSameCol(const vector<vector<int>> board, const pair<int, int> pos, const int size)
{
    for(int i = 0; i < size; i++)
    {
        if(board[i][pos.second])
            return true;
    }
    return false;
}
bool isSameDiagonal(const vector<vector<int>> board, const pair<int, int> pos, const int size)
{

}
bool isPossible(const vector<vector<int>> board, const pair<int, int> pos, const int size)
{
    return !(isSameRow(board, pos, size) || isSameCol(board, pos, size) || isSameDiagonal(board, pos, size));
}

void setQueen(vector<vector<int>> &board, const pair<int, int> pos, const int toSet, const int size, int &ret)
{
    if(toSet == 0)
    {   // finish case //
        ret++;
        return ;
    }

    for(int i = 0; i < size; i++)
    {   // row //
        for(int j = 0; j < size; j++)
        {   // col //
            

            setQueen(board, make_pair(i, j), toSet-1, size, ret);
        }
    }
}

int main(void)
{
    int N, ret = 0; cin >> N;
    vector<vector<int>> board;

    // resize to NxN //
    board.resize(N);
    for(int i = 0; i < N; i++)
    {
        board.at(i).resize(N);
    }

    setQueen(board, make_pair(0, 0), N, N, ret);

    cout << ret << '\n';

    return 0;
}