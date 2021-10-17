#include <iostream>
#include <utility>
#include <cmath>

using namespace std;

int** Set_Planet(const int num)
{
    int** planet = new int*[num];
    for(int i = 0; i < num; i++)
    {
        planet[i] = new int[3];
        for(int j = 0; j < 3; j++) cin >> planet[i][j];
    }

    return planet;
}

double Find_Distance(int x1, int y1, int x2, int y2)
{
    return sqrt( pow(x1 - x2, 2) + pow(y1 - y2, 2) );
}

int Count_Min(int** planet, pair<int, int> start, pair<int, int> end, const int num)
{
    int output = 0;

    for(int i = 0; i < num; i++)
    {
        double d1 = Find_Distance(start.first, start.second, planet[i][0], planet[i][1]);
        double d2 = Find_Distance(end.first, end.second, planet[i][0], planet[i][1]);

        if(d1 > planet[i][2] && d2 < planet[i][2]) output++;
        else if(d1 < planet[i][2] && d2 > planet[i][2]) output++;
    }

    return output;
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        pair<int, int> start; cin >> start.first >> start.second;
        pair<int, int> end; cin >> end.first >> end.second;

        int NumofPlanet; cin >> NumofPlanet;
        int** Planet = Set_Planet(NumofPlanet);
        
        cout << Count_Min(Planet, start, end, NumofPlanet) << endl;
    }

    return 0;
}