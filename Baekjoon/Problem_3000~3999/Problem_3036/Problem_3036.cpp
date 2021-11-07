#include <iostream>
#include <string>

using namespace std;

void swap(int *num1, int *num2)
{/* Xor Swap */
    *num1 ^= *num2;
    *num2 ^= *num1;
    *num1 ^= *num2;
}

int getGCD(int num1, int num2)
{/* 유클리드 호제법 */
    /* make that num1 > num2 */
    if(num1 < num2) swap(num1, num2);

    int remainder = num1 % num2;

    while(remainder != 0)
    {
        num1 = num2;
        num2 = remainder;
        remainder = num1 % num2;
    }

    return num2;
}

string change2Fraction(int numerator, int denominator)
{
    int gcd = getGCD(numerator, denominator);

    return to_string(numerator / gcd) + '/' + to_string(denominator / gcd);
}

int main(void)
{
    int numOfRings; cin >> numOfRings;
    int baseRing; cin >> baseRing;

    for(int i = 1; i < numOfRings; i++)
    {
        int curRing; cin >> curRing;

        /* 분모 분자를 최대공약수로 나눠버리기! */
        cout << change2Fraction(baseRing, curRing) << endl;
    }

    return 0;
}