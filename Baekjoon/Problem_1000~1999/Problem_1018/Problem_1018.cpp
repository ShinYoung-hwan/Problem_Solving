#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class ChessData
{
private:
    int row;
    int col;
    vector<string> chessBoard;
public:
    void setRow(const int row){ this->row = row; }
    int getRow(){ return this->row; }
    void setCol(const int col){ this->col = col; }
    int getCol(){ return this->col; }
    void setChessBoard(const string str){ this->chessBoard.push_back(str); }
    vector<string> getChessBoard(){ return this->chessBoard; }
    string getChessBoardRow(const int index){ return this->chessBoard.at(index); }
    char getChessBoardChar(const int row, const int col){ return this->chessBoard.at(row).at(col); }
};

void setData(ChessData &chessData)
{
    int N, M;
    string str;

    cin >> N >> M;
    chessData.setRow(N); chessData.setCol(M);
    for(int i = 0; i < N; i++)
    {
        cin >> str;
        chessData.setChessBoard(str);
    }
}

int compare8X8(ChessData &chessData, int x, int y)
{
    int ret1 = 0, ret2 = 0;
    string str1 = "WBWBWBWB";
    string str2 = "BWBWBWBW";

    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8; j++)
        {
            if(i % 2 == 0)
            {
                if(chessData.getChessBoardChar(x+i, j+y) != str1.at(j)) ret1++;
                if(chessData.getChessBoardChar(x+i, j+y) != str2.at(j)) ret2++;
            } else
            {
                if(chessData.getChessBoardChar(x+i, j+y) != str2.at(j)) ret1++;
                if(chessData.getChessBoardChar(x+i, j+y) != str1.at(j)) ret2++;
            }
            
        }
    }
    return min(ret1, ret2);
}

int getMinChangeNum(ChessData &chessData)
{
    int ret = 64;

    for(int i = 0; i <= chessData.getRow()-8; i++)
    {
        for(int j = 0; j <= chessData.getCol()-8; j++)
        {
            ret = min(ret, compare8X8(chessData, i, j));
        }
    }

    return ret;
}

int main(void)
{
    ChessData chessData; setData(chessData);

    cout << getMinChangeNum(chessData) << endl;

    return 0;
}