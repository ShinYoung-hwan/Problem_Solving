#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Statistics
{
private:
    float mean;
    int median;
    int mode;
    int range;

public:
    void setMean(float mean){ this->mean = mean; }
    float getMean(){ return this->mean; }
    void setMedian(int median){ this->median = median; }
    int getMedian(){ return this->median; }
    void setMode(int mode){ this->mode = mode; }
    int getMode(){ return this->mode; }
    void setRange(int range){ this->range = range; }
    int getRange(){ return this->range; }
};

void setDatas(vector<int> &datas, Statistics &statistics, const int N)
{   // store input datas - O(N) //
    // to be efficient, set mean in this part //
    int num;
    int sum = 0;
    for(int i = 0; i < N; i++)
    {
        cin >> num;
        sum += num;
        datas.push_back(num);
    }
    statistics.setMean(round(static_cast<float>(sum) / N));
}

void setStatistics(Statistics &statistics, const vector<int> &datas, const int N)
{    // set median, mode, range - O(N) //
    int mode = 0, max = 0, pos = 0;
    int table[8001] = {0, };
    vector<int> modeCandidate(8001);

    // set median - O(1) //
    statistics.setMedian(datas.at(static_cast<int>(N/2)));

    // set mode - O(N) //
    // traverse datas and find frequency //
    // find max frequent data for second frequent data //
    for(auto item : datas)
    {
        table[item+4000]++;
    }
    for(int i = 0; i < 8001; i++)
    {
        if(max <= table[i])
        {
            if(max != table[i])
            {
                pos = 0;
                max = table[i];
            }
            modeCandidate.at(pos++) = i - 4000;
        }
    }
    if(pos == 1)
        mode = modeCandidate.at(0);
    else
    {
        sort(modeCandidate.begin(), (modeCandidate.begin()+pos));
        mode = modeCandidate.at(1);
    }
    statistics.setMode(mode);

    // set Range - O(1) //
    statistics.setRange(datas.at(N-1) - datas.at(0));
}

void printStatistics(Statistics &statistics)
{   // print statistic datas - O(1) //
    cout << statistics.getMean() << endl;
    cout << statistics.getMedian() << endl;
    cout << statistics.getMode() << endl;
    cout << statistics.getRange() << endl;
}

int main(void)
{
    Statistics statistics;
    int N; scanf("%d", &N);
    vector<int> datas; setDatas(datas, statistics, N);
    sort(datas.begin(), datas.end());

    setStatistics(statistics, datas, N);

    printStatistics(statistics);

    return 0;
}