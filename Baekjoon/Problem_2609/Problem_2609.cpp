#include <iostream>

using namespace std;

int FindGCD(int x, int y) {
	if (y == 0)
		return x;
	else
		return FindGCD(y, x % y);
}
int FindGCM(const int x, const int y, const int GCD)
{
    return x * y / GCD;
}

int main(void)
{
    int num1, num2; cin >> num1 >> num2;
    
    int GCD = FindGCD(num1, num2);
    cout << GCD << endl;
    cout << FindGCM(num1, num2, GCD) << endl;

    return 0;
}