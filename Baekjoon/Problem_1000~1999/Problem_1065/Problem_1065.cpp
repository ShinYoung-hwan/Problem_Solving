#include <iostream>
#include <cstdio>
/*
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
*/

using namespace std;

int Num_of_Hansu(int num) {
	if (num < 100)
		return num;
	else if (num < 1000) {
		int result = 0;
		for (int i = 100; i <= num; i++) {
			int Nth[3] = { 0, };
			int rest = i;
			for (int j = 0; j < 3; j++) {
				Nth[j] = rest % 10;
				rest /= 10;
			}
			if ((Nth[2] - Nth[1]) == (Nth[1] - Nth[0]))
				result += 1;
		}
        
		return result + Num_of_Hansu(99);
	}
	else {
		int result = 0;
		for (int i = 1000; i <= num; i++) {
			int Nth[4] = { 0, };
			int rest = i;
			for (int j = 0; j < 4; j++) {
				Nth[j] = rest % 10;
				rest /= 10;
			}
			if ((Nth[2] - Nth[1]) == (Nth[3] - Nth[2]) &&(Nth[2] - Nth[1]) == (Nth[1] - Nth[0]))
				result += 1;
		}

		return result + Num_of_Hansu(999);
	}
}

int main(){
	int num;
	cin >> num;
	
	cout << Num_of_Hansu(num) << endl;	

	return 0;
}