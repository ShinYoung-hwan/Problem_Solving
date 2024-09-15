#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
const int MAXRC = 8;
int R, C;
int board[MAXRC][MAXRC];
vector<pair<int, pair<int, int> >> cctvs; // [ ( cctv, (r, c) ), ... ]

int answer = 64;

int count_blanks() {
    int cnt = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            cnt += (board[r][c] == 0);
        }
    }
    return cnt;
}

void set_right(const int r0, const int c0, vector<pair<int, int> > &converted) {
    for (int c = c0+1; c < C; c++) {
        if (board[r0][c] == 6) break; // 벽 만남
        else if (board[r0][c] != 0) continue; // 이미 커버한 구역

        converted.push_back({ r0, c });
        board[r0][c] = -1;
    }
}
void set_up(const int r0, const int c0, vector<pair<int, int> > &converted) {
    for (int r = r0-1; r > -1; r--) {
        if (board[r][c0] == 6) break;
        else if (board[r][c0] != 0) continue;

        converted.push_back({ r, c0 });
        board[r][c0] = -1;
    }
}
void set_left(const int r0, const int c0, vector<pair<int, int> > &converted) {
    for (int c = c0-1; c > -1; c--) {
        if (board[r0][c] == 6) break;
        else if (board[r0][c] != 0) continue;

        converted.push_back({ r0, c });
        board[r0][c] = -1;
    }
}
void set_down(const int r0, const int c0, vector<pair<int, int> > &converted) {
    for (int r = r0+1; r < R; r++) {
        if (board[r][c0] == 6) break;
        else if (board[r][c0] != 0) continue;

        converted.push_back({ r, c0 });
        board[r][c0] = -1;
    }
}
void (*set_direction[4])(const int, const int, vector<pair<int, int> >&) = { set_right, set_up, set_left, set_down };

void cctv1(const int dir, const int r0, const int c0, vector<pair<int, int> > &converted) {
    set_direction[dir](r0, c0, converted);
}
void cctv2(const int dir, const int r0, const int c0, vector<pair<int, int> > &converted) {
    set_direction[dir](r0, c0, converted);
    set_direction[dir+2](r0, c0, converted);
}
void cctv3(const int dir, const int r0, const int c0, vector<pair<int, int> > &converted) {
    set_direction[dir](r0, c0, converted);
    set_direction[(dir+1)%4](r0, c0, converted);
}
void cctv4(const int dir, const int r0, const int c0, vector<pair<int, int> > &converted) {
    set_direction[dir](r0, c0, converted);
    set_direction[(dir+1)%4](r0, c0, converted);
    set_direction[(dir+2)%4](r0, c0, converted);
}
void cctv5(const int dir, const int r0, const int c0, vector<pair<int, int> > &converted) {
    set_direction[dir](r0, c0, converted);
    set_direction[(dir+1)%4](r0, c0, converted);
    set_direction[(dir+2)%4](r0, c0, converted);
    set_direction[(dir+3)%4](r0, c0, converted);
}
void (*cctv_direction[6])(const int, const int, const int, vector<pair<int, int> >&) = { cctv1, cctv1, cctv2, cctv3, cctv4, cctv5 };

void DFS(const int depth=0) {
    // base
    if (depth == cctvs.size()) {
        answer = min(answer, count_blanks());
        return;
    }

    // default
    int cctv = cctvs[depth].first, r0 = cctvs[depth].second.first, c0 = cctvs[depth].second.second;
    if (cctv == 2) {
        for (int dir = 0; dir < 2; dir++) {
            vector<pair<int, int> > converted;
            cctv2(dir, r0, c0, converted);
            DFS(depth+1);
            for (auto e: converted) {
                board[e.first][e.second] = 0;
            }
        }
    } else if (cctv == 5) {
        vector<pair<int, int> > converted;
        cctv5(0, r0, c0, converted);
        DFS(depth+1);
        for (auto e: converted) {
            board[e.first][e.second] = 0;
        }
    } else {
        for (int dir = 0; dir < 4; dir++) {
            vector<pair<int, int> > converted;
            cctv_direction[cctv](dir, r0, c0, converted);
            DFS(depth+1);
            for (auto e: converted) {
                board[e.first][e.second] = 0;
            }
        }
    }

}

int main() {
    scanf("%d %d", &R, &C);
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            scanf("%d", &board[r][c]);
            if (board[r][c] == 0 || board[r][c] == 6) continue;
            cctvs.push_back({ board[r][c], { r, c } });
        }
    }

    DFS();
    printf("%d\n", answer);
    
    return 0;
}