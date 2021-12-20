#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void setPair(vector<pair<int, int>> &friendPair, const int N)
{   // store the pair of Friend //
    int p1, p2;
    for(int i = 0; i < N; i++)
    {
        cin >> p1 >> p2;
        friendPair.push_back(make_pair(p1, p2));
    }
}

int getTotalPair(vector<pair<int, int>> &friendPair, const int numOfStudnet, const int numOfFriendPair)
{

}

int main(void)
{
    int testCase; cin >> testCase;
    int numOfStudent, numOfFriendPair;
    vector<pair<int, int>> friendPair;
    for(int i = 0; i < testCase; i++)
    {   // testcase loop //
        cin >> numOfStudent >> numOfFriendPair;

        setPair(friendPair, numOfFriendPair);

        cout << getTotalPair(friendPair, numOfStudent, numOfFriendPair) << '\n';
    }
    return 0;
}