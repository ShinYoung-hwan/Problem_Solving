#include <cstdio>
#include <algorithm>

using namespace std;
const int MAXN = 100;
enum { MALE=1, FEMALE=2 };

int main() {
    int N; scanf("%d", &N);
    int switches[MAXN+1] = { 0, };
    for (int i = 1; i <= N; i++) scanf("%d", &switches[i]);

    int C; scanf("%d", &C);
    for (int c = 0; c < C; c++) {
        int gender, n; scanf("%d %d", &gender, &n);

        // 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
        if (gender == MALE) {
            for (int i = n; i <= N; i += n) {
                switches[i] = !switches[i];
            }
        } 
        // 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다
        else { // gender == FEMALE
            switches[n] = !switches[n];
            for (int i = 1; i < min(n, N-n+1); i++) {
                if (switches[n-i] != switches[n+i]) break;
                switches[n-i] = !switches[n-i];
                switches[n+i] = !switches[n+i];
            }
        }
    }

    // print
    for (int i = 1; i <= N; i++) {
        printf("%d%c", switches[i], i % 20 == 0 ? '\n': ' ');
    }

    
    return 0;
}