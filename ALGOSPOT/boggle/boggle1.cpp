#include <iostream>
#include <vector>
#include <utility>

using namespace std;

const size_t BOARD_SIZE = 5;
const int posChange[8][2] = {
    {1, 0},
    {1, 1},
    {0, 1},
    {-1, 1},
    {-1, 0},
    {-1, -1},
    {0, -1},
    {1, -1}
};

void setBoard(vector<string> &board)
{   // set Board from input //
    string str;
    for(int i = 0; i < 5; i++)
    {
        cin >> str;
        board.push_back(str);
    }
}

bool outOfRange(const pair<int, int> pos, const int candidate)
{
    if((pos.first + posChange[candidate][0] < 0) || (pos.first + posChange[candidate][0] >= BOARD_SIZE))
    {   // compare the x range //
        return true;
    } else if((pos.second + posChange[candidate][1] < 0) || (pos.second + posChange[candidate][1] >= BOARD_SIZE))
    {   // compare the y range //
        return true;
    }
    return false;
}

char getChar(const vector<string> board, const pair<int, int> pos, const int candidate)
{
    if(outOfRange(pos, candidate)) 
    {   // sanity check //
        return 0;
    }
    return board.at(pos.first+posChange[candidate][0]).at(pos.second+posChange[candidate][1]);
}

bool hasWord(const vector<string> board, pair<int, int> pos, string target, int idx)
{
    if(idx == target.size())
    {   // found //
        return true;
    }
    // during search //
    for(int i = 0; i < 8; i++)
    {
        if(target.at(idx) == getChar(board, pos, i))
        {   // found next word //
            if(hasWord(board, make_pair(pos.first+posChange[i][0], pos.second+posChange[i][1]), target, idx+1))
                return true;
        }
    }
    // not found //
    return false;
}
bool findWord(const vector<string> board, string target)
{   // time complexity O();
    for(int i = 0; i < BOARD_SIZE; i++)
    {
        for(int j = 0; j < BOARD_SIZE; j++)
        {
            if(target.at(0) != board.at(i).at(j))
                continue;
            if(hasWord(board, make_pair(i, j), target, 1))
            {   // found //
                return true;
            }
        }
    }
    // not fount //
    return false;
}
int main(void)
{
    vector<string> board;
    int testCase, numOfWords; cin >> testCase;
    string word;

    for(int i = 0; i < testCase; i++)
    {   // there several testcases //
        setBoard(board);

        cin >> numOfWords;

        for(int j = 0; j < numOfWords; j++)
        {
            cin >> word;
            cout << word;
            if(findWord(board, word))
            {   // word is found //
                cout << " Yes" << '\n';
            } else
            {   // word is not found //
                cout << " No" << '\n';
            }
        }

    }

    return 0;
}

// book style //