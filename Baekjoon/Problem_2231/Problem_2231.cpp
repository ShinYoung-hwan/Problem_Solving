#include <iostream>
#include <string>

using namespace std;

string Get_Decomposition(string num)
{
    int output = stoi(num);

    for(int i = 0; i < num.length(); i++)
    {
        output += static_cast<int>(num.at(i) - '0');
    }

    return to_string(output);
}

string Get_MinProducer(string snum)
{
    int inum = stoi(snum);

    for(int i = inum - 9 * snum.length(); i < inum; i++)
    {
        if(Get_Decomposition(to_string(i)) == snum) return to_string(i);
    }

    return "0";
}

int main(void)
{
    string N; cin >> N;

    cout << Get_MinProducer(N) << endl;

    return 0;
}