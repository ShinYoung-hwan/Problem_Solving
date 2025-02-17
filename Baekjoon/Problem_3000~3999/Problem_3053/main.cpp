#include <iostream>
#include <cmath>
using namespace std;

double GetArea_of_EucliGeo(int r)
{
    const double PI = 3.14159265358979;

    return pow(r, 2) * PI;
}
double GetArea_of_TaxiGeo(int r)
{
    return 2.0 * pow(r, 2);
}

int main(void)
{
    int r; cin >> r;
    
    cout << fixed;
    cout.precision(6);
    cout << GetArea_of_EucliGeo(r) << endl;
    cout << GetArea_of_TaxiGeo(r) << endl;
    return 0;
}