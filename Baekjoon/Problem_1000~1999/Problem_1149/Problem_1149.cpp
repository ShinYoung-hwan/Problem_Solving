#include <iostream>
#include <vector>

using namespace std;

int getMinCost(const vector<vector<int>> &costv, const int numOfHouse)
{   

}

int main(void)
{
    int numOfHouse; cin >> numOfHouse;
    vector<vector<int>> costv;
    int costR, costG, costB;

    for(int i = 0; i < numOfHouse; i++)
    {
        // get i-th cost //
        cin >> costR >> costG >> costB;

        costv.at(i).push_back(costR);
        costv.at(i).push_back(costG);
        costv.at(i).push_back(costB);
    }
    
    cout << getMinCost(costv, numOfHouse) << '\n';

    return 0;
}