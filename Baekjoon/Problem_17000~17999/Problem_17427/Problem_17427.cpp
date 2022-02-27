#include <iostream>

using namespace std;

class SumOfFactorization2 
{
private:
    int N;
public:
    void set_N(){ cin >> this->N; }
    int get_N(){ return this->N; }

    long solve()
    {
        long answer = 0;

        for(int i = 1; i <= this->get_N(); i++)
        {
            answer += static_cast<int>(this->get_N() / i) * i;
        }

        return answer;
    }
};

int main(void)
{
    SumOfFactorization2 class_engine;

    class_engine.set_N();

    cout << class_engine.solve() << '\n';

    return 0;
}