#include <iostream>
#include <vector>
#include <string>
#include <utility>

using namespace std;

class Candy_Game
{
private:
    int numOfLines = 0;
    char directs[4] = {'L', 'R', 'U', 'D'};
    vector<string> candies;
public:
    void set_candies()
    {
        cin >> this->numOfLines;
        
        string line;
        for(int i = 0; i < this->numOfLines; i++)
        {
            // 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y //
            cin >> line;
            candies.push_back(line);
        }
    }

    bool is_out(pair<int, int> pos, char direction)
    {
        if(direction == 'L') pos.first -= 1;
        else if(direction == 'R') pos.first += 1;
        else if(direction == 'U') pos.second += 1;
        else // 'D' //
            pos.second -= 1;

        if (
            pos.first < 0 || 
            pos.first > this->numOfLines || 
            pos.second < 0 || 
            pos.second > this->numOfLines
        )
            return false;
            
        return true;
    }
    int switch_candy(pair<int, int> pos, char direction)
    {
        // check is edge case //
        if(is_out(pos, direction)) return 0;


    }
    void solve()
    {
        int max = 0;
        for(int i = 0; i < this->numOfLines; i++)
        {
            for(int j = 0; j < this->numOfLines; j++)
            {
                for(char item: this->directs)
                {
                    int tmp = this->switch_candy(make_pair(i, j), item);
                    max = max? tmp < max: tmp;
                }
                
            }
        }

        printf("%d\n", max);
    }
};

int main(void)
{
    Candy_Game problem_solver; 
    
    problem_solver.set_candies();

    problem_solver.solve();

    return 0;
}