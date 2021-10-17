#include <iostream>

using namespace std;

int FindGCD(int x, int y) {
	if (y == 0)
		return x;
	else
		return FindGCD(y, x % y);
}
int FindGCM(const int x, const int y)
{
    return x * y / FindGCD(x, y);
}

int main(void)
{
    int Testcase; cin >> Testcase;

    for(int i = 0; i < Testcase; i++)
    {
        int num1, num2; cin >> num1 >> num2;

        cout << FindGCM(num1, num2) << endl;
    }

    return 0;
}