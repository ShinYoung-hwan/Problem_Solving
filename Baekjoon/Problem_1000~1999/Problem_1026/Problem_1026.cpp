#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void setArray(vector<int> &array, const size_t N)
{
    int tmp;
    for(int i = 0; i < N; i++)
    {
        cin >> tmp;
        array.push_back(tmp);
    }
}

int getS(const vector<int> A, const vector<int> B, const size_t N)
{
    int ret = 0;
    for(int i = 0; i < N; i++)
    {
        ret += A.at(i) * B.at(i);
    }
    return ret;
}

int main(void)
{
    size_t N; cin >> N; // size of array //
    vector<int> A, B, S; // two arrays //

    setArray(A, N);
    setArray(B, N);

    // sort A acending order //
    sort(A.begin(), A.end());

    // sort B decending order //
    sort(B.rbegin(), B.rend());

    cout << getS(A, B, N) << '\n';
    return 0;
}