#include <iostream>

using namespace std;

int cost[1000] = {0, };

void initCost()
{
    cost[0] = 0;
    cost[1] = 3;
}

int getMinCost(const int numOfHouse, const int R, const int G, const int B)
{
    if(numOfHouse == 1)
    {
        return cost[1];
    }

    return cost[numOfHouse];
}

int main(void)
{
    int numOfHouse; cin >> numOfHouse;
    int costR, costG, costB; cin >> costR >> costG >> costB;

    initCost();

    cout << getMinCost(numOfHouse, costR, costG, costB) << '\n';

    return 0;
}