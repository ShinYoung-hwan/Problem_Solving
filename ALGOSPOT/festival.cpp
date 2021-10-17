#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

vector<int> setDatas(const int size)
{   /* data를 저장하기 */
    vector<int> datas;
    int tmpStore;
    for(int i = 0; i < size; i++)
    {
        cin >> tmpStore;
        datas.push_back(tmpStore);
    }
    return datas;
}

double getMinMeanCost(const vector<int> &datas, const int M)
{   /* 최소 평균 가격을 구하기 */
    double ret = 987654321;
    const int size = datas.size();
    const int end = size - M;    

    for(int i = 0; i <= end; i++)
    {
        int sum = 0;
        for(int j = i; j < size; j++)
        {
            sum += datas.at(j);
            if(j - i + 1 < M) continue; // sanity check!

            double mean = static_cast<double>(sum) / (j - i + 1);
            ret = min(mean, ret);
        }
    }
    return ret;
}

int main(void)
{
    int testcase; cin >> testcase;
    vector<int> datas;

    for(int i = 0; i < testcase; i++)
    {
        int N, M; cin >> N >> M;

        datas = setDatas(N);

        printf("%.8f\n", getMinMeanCost(datas, M));
    }
    return 0;
}