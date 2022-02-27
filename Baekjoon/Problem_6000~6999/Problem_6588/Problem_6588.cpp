#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
const int MAXSIZE = 1000001;

class Goldbach_Conjecture
{
private:
    int is_prime[MAXSIZE] = { -1, };
    vector<int> prime_datas;
public:
    void prepare()
    {
        // reset the is_prime array to not specified status //
        fill_n(this->is_prime, MAXSIZE, -1);
        
        // find prime number //
        // -1: not specified, 0: not prime, 1: prime //
        for(int i = 2; i < MAXSIZE; i++)
        {
            if(this->is_prime[i] == 0)
                continue;
            else if(this->is_prime[i] == -1)
                this->is_prime[i] == 1;
            
            for(int j = 2; i*j < MAXSIZE; j++)
            {
                this->is_prime[i*j] = 0;
            }
        }

        // extract prime number //
        for(int i = 3; i < MAXSIZE; i++)
        {
            if(is_prime[i])
                this->prime_datas.push_back(i);
        }
    }
    void solve(const int n)
    {
        for(int item: this->prime_datas)
        {
            if(this->is_prime[n-item])
            {
                printf("%d = %d + %d\n", n, item, n-item);
                return;
            }
        }
        printf("Goldbach's conjecture is wrong.\n");
    }
};

int main(void)
{
    Goldbach_Conjecture problem_solver;
    int n;

    problem_solver.prepare();

    while(scanf("%d", &n))
    {
        if(n == 0) break;

        problem_solver.solve(n);
    }

    return 0;
}