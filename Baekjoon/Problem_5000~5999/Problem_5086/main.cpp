#include <iostream>
#include <string>

using namespace std;

/*
첫 번째 숫자가 두 번째 숫자의 약수이다.
첫 번째 숫자가 두 번째 숫자의 배수이다.
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
*/

bool IsFactor(const int x, const int y)
{
    if(x % y == 0) return true;
    else return false;
}

string CompareNumbers(const int x, const int y)
{
    if(IsFactor(x, y)) return "multiple";
    else if(IsFactor(y, x)) return "factor";
    else return "neither";
}

int main(void)
{
    int num1, num2; cin >> num1 >> num2;

    while(!(num1 == 0 && num2 == 0))
    {
        cout << CompareNumbers(num1, num2) << endl;

        cin >> num1 >> num2;
    }

    return 0;
}