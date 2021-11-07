#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string Resist[10] = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white" };

string* Set_Color()
{
    string* Color = new string[3];

    for(int i = 0; i < 3; i++) cin >> Color[i];

    return Color;
}

int Get_Pos(string color)
{
    for(int i = 0; i < 10; i++)
    {
        if(color == Resist[i]) return i;
    }
}

long long Get_Resistance(string* color)
{
    long long R = 0;

    for(int i = 0; i < 3; i++)
    {
        switch(i)
        {
            case 0:
                R += Get_Pos(color[i]) * 10;
                break;
            case 1:
                R += Get_Pos(color[i]);
                break;
            case 2:
                R *= pow(10, Get_Pos(color[i]));
        }
    }

    return R;
}

int main(void)
{
    string* color = Set_Color();
    
    cout << Get_Resistance(color) << endl;

    delete[] color;
    return 0;
}