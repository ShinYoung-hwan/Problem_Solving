#include <cstdio>
#include <cstring>

using namespace std;

char board[5][5];
char keyword[11];
int length = 0;

const int MAXRC = 5;
const int dr[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };
const int dc[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

inline bool isIn(const int r, const int c) {
    return (0 <= r && r < MAXRC) && (0 <= c && c < MAXRC);
}

bool find(const int r0, const int c0, const int idx=1) {
    // base
    if (length == idx) return true;

    // default
    for (int i = 0; i < 8; i++) {
        int r = r0 + dr[i], c = c0 + dc[i];

        if (!isIn(r, c)) continue; // 보드 범위 확인
        if (board[r][c] != keyword[idx]) continue; // 현재 글자 확인
        if (!find(r, c, idx+1)) continue; // 이후 글자 확인
        
        return true;

    }
    return false;
}

bool find_keyword() {
    for (int r = 0; r < MAXRC; r++) {
        for (int c = 0; c < MAXRC; c++) {
            if (board[r][c] != keyword[0]) continue; // 첫글자 확인
            if (!find(r, c)) continue; // 키워드를 발견하지 못함

            return true;
        }
    }

    return false;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);
    getchar();

    for (int t = 0; t < C; t++) {
        
        // set board
        for (int r = 0; r < MAXRC; r++) {
            for (int c = 0; c < MAXRC; c++) {
                board[r][c] = getchar();
            }
            getchar(); // \n 처리
        }
        
        // find keyword
        int N; scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%s", keyword);
            length = strlen(keyword);

            printf("%s %s\n", keyword, find_keyword() ? "YES" : "NO");
        }
    }

    return 0;
}