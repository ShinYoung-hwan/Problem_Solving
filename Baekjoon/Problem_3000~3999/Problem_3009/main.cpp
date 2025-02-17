#include <iostream>
#include <map>

using namespace std;
enum { x, y };

template<size_t N>
void Get_Pos(int (&pos1)[N], int (&pos2)[N], int (&pos3)[N])
{
    map<int, int> mapx; map<int, int> mapy;
    int posx = -1, posy = -1;

    if(mapx.find(pos1[x]) == mapx.end()) mapx[pos1[x]] = 1;
    else mapx[pos1[x]] += 1;
    if(mapy.find(pos1[y]) == mapx.end()) mapy[pos1[y]] = 1;
    else mapy[pos1[y]] += 1;

    if(mapx.find(pos2[x]) == mapx.end()) mapx[pos2[x]] = 1;
    else mapx[pos2[x]] += 1;
    if(mapy.find(pos2[y]) == mapx.end()) mapy[pos2[y]] = 1;
    else mapy[pos2[y]] += 1;

    if(mapx.find(pos3[x]) == mapx.end()) mapx[pos3[x]] = 1;
    else mapx[pos3[x]] += 1;
    if(mapy.find(pos3[y]) == mapx.end()) mapy[pos3[y]] = 1;
    else mapy[pos3[y]] += 1;

    map<int, int>::iterator iter;

    for(iter = mapx.begin(); iter != mapx.end(); iter++)
    {
        if(iter->second == 1) posx = iter->first;
    }
    for(iter = mapy.begin(); iter != mapy.end(); iter++)
    {
        if(iter->second == 1) posy = iter->first;
    }

    cout << posx << ' ' << posy << endl;
}

int main(void)
{
    int pos1[2]; cin >> pos1[x] >> pos1[y];
    int pos2[2]; cin >> pos2[x] >> pos2[y];
    int pos3[2]; cin >> pos3[x] >> pos3[y];

    Get_Pos(pos1, pos2, pos3);
    return 0;
}