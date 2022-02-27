#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Seven_Dwarfs
{
private:
    int sumH = 0;
    vector<int> nine_dwarfs;
    vector<int> seven_dwarfs;
public:
    void prepare()
    {
        int h = 0;
        for(int i = 0; i < 9; i++)
        {
            scanf("%d", &h);
            this->nine_dwarfs.push_back(h);
            this->sumH += h;
        }
    }

    pair<int, int> find_not_seven()
    {
        for(int i = 0; i < 9; i++)
        {
            for(int j = 0; j < 9; j++)
            {
                if(i == j) continue;

                if(sumH - this->nine_dwarfs[i] - this->nine_dwarfs[j] == 100)
                {
                    return make_pair(this->nine_dwarfs[i], this->nine_dwarfs[j]);
                }
            }
        }
        // always return in loop //
    }

    void set_seven_dwarfs(const int n1, const int n2)
    {
        for(int item: this->nine_dwarfs)
        {
            if(item == n1 || item == n2)
                continue;

            this->seven_dwarfs.push_back(item);
        }
    }

    void solve()
    {
        pair<int, int> not_seven = this->find_not_seven();

        this->set_seven_dwarfs(not_seven.first, not_seven.second);
                    
        
        sort(this->seven_dwarfs.begin(), this->seven_dwarfs.end());
        for(int item: this->seven_dwarfs)
            printf("%d\n", item);
    }
};

int main(void)
{
    Seven_Dwarfs problem_solver;

    problem_solver.prepare();

    problem_solver.solve();

    return 0;
}