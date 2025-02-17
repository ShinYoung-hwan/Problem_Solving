#include <iostream>

using namespace std;
const int MAXSIZE = 1000001;

class SumOfFactorization 
{
private:
    int N;
    long datas[MAXSIZE] = { 0, };

public:
    void set_N(){ scanf("%d", &this->N); }
    int get_N(){ return this->N; }

    void prepare()
    {   // 에라토스테네스의 체 원리로 값 준비 //
        datas[1] = 1;

        for(int i = 2; i < MAXSIZE; i++)
        {
            for(int j = 1; i*j < MAXSIZE; j++)
            {
                this->datas[i*j] += i;
            }
            this->datas[i] += this->datas[i-1]+1;
        }
    }

    long solve()
    {
        return this->datas[this->get_N()];
    }
};

int main(void)
{
	int testcase;
	scanf("%d", &testcase);

    SumOfFactorization class_engine;
    class_engine.prepare();

	for(int i = 0; i < testcase; i++)
	{
		class_engine.set_N();

        printf("%ld\n", class_engine.solve());
	}

    return 0;
}