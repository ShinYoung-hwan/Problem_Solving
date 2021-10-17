#include <iostream>

using namespace std;

int Get_Min(int x, int y, int w, int h)
{
    int min = x;
    if(y < min) min = y;
    if(w - x < min) min = w - x;
    if(h - y < min) min = h - y;

    return min;
}

int main(void)
{
    int x, y; cin >> x >> y;
    int w, h; cin >> w >> h;

    cout << Get_Min(x, y ,w, h) << endl;

    return 0;
}
