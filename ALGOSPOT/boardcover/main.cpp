#include <cstdio>

using namespace std;

const int MAXRC = 20;

int R, C;
bool board[MAXRC][MAXRC] = { false, };
int cnt = 0;
const int pieces[4][3][2] = {
    { { 0, 0 }, { 1, 0 }, { 1, 1 } },
    { { 0, 0 }, { 0, 1 }, { 1, 0 } },
    { { 0, 0 }, { 0, 1 }, { 1, 1 } },
    { { 0, 0 }, { 1, 0 }, { 1, -1 } }
};

inline bool is_in(const int r, const int c) {
    return (0 <= r && r < R) && (0 <= c && c < C);
}

void find_uncovered(int &r0, int &c0) {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (board[r][c]) continue; // 벽인 경우

            r0 = r, c0 = c;
            return;
        }
    }
}

bool is_valid_piece(const int r0, const int c0, const int piece) {
    for (int i = 0; i < 3; i++) {
        int r = r0 + pieces[piece][i][0], c = c0 + pieces[piece][i][1];
        
        if (!is_in(r, c)) return false;
        if (board[r][c]) return false;

    }
    return true;
}

void cover(const int r0, const int c0, const int piece, const bool is_cover=false) {
    for (int i = 0; i < 3; i++) {
        int r = r0 + pieces[piece][i][0], c = c0 + pieces[piece][i][1];

        board[r][c] = !is_cover;
    }
}

void visit() {
    int r0 = -1, c0 = -1;
    find_uncovered(r0, c0);

    // base: 커버 완료
    if (r0 == -1 && c0 == -1) {
        cnt++;
        return;
    }

    // default: cover
    for (int piece = 0; piece < 4; piece++) {
        if (!is_valid_piece(r0, c0, piece)) continue;

        cover(r0, c0, piece);
        visit();
        cover(r0, c0, piece, true);
    }
}

int main(int argc, char **argv) {
    int T; scanf("%d", &T);

    for (int t = 0; t < T; t++) {
        scanf("%d %d", &R, &C); getchar(); 

        // set board
        int n_empty = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                board[r][c] = getchar() == '#' ? true : false ;
                n_empty += board[r][c] ? 0 : 1;
            }
            getchar(); // \n handling
        }

        // search
        cnt = 0;
        if (!(n_empty % 3)) visit();

        printf("%d\n", cnt);
    }

    return 0;
}