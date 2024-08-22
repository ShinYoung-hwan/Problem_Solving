#include <cstdio>

const int MAXNM = 50;

enum { NORTH, EAST, SOUTH, WEST };

using namespace std;
int R, C;
int isWall[MAXNM][MAXNM];

bool isNearClear(bool isClear[MAXNM][MAXNM], const int r0, const int c0) {
    // NORTH
    if (!isClear[r0-1][c0]) return false;
    // EAST
    else if (!isClear[r0][c0+1]) return false;
    // SOUTH
    else if (!isClear[r0+1][c0]) return false;
    // WEST
    else if (!isClear[r0][c0-1]) return false;

    return true;
}

void get_position(int &r, int &c, const int d, const bool front) {
    int dr, dc;
    if (front) {
        dr = 1, dc = 1;
    } else {
        dr = -1, dc = -1;
    }

    switch (d) {
        case NORTH:
            r -= dr;
            break;
        case EAST:
            c += dc;
            break;
        case SOUTH:
            r += dr;
            break;
        case WEST:
            c -= dc;
            break;
    }
}

inline int turn_cclockwise_90(const int d) {
    return (d+3) % 4;
}

int solve(int r0, int c0, int d) {
    int cnt = 0;
    bool isClear[MAXNM][MAXNM];
    for (int r = 0; r <= R; r++) {
        for (int c = 0; c <= C; c++) {
            isClear[r][c] = isWall[r][c] ? true : false;
        }
    }

    while (true) {
        // 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if (!isClear[r0][c0]) {
            isClear[r0][c0] = true;
            cnt += 1;
        }

        // 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
        if (isNearClear(isClear, r0, c0)) {
            int r = r0, c = c0; 
            get_position(r, c, d, false); 
            // 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if (!isWall[r][c]) {
                r0 = r, c0 = c;
            }
            // 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else break;
        }
        // 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
        else {
            // 반시계 방향으로 $90^\circ$ 회전한다.
            d = turn_cclockwise_90(d);
            // 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            int r = r0, c = c0; get_position(r, c, d, true);
            if (!isWall[r][c] && !isClear[r][c]) {
                r0 = r, c0 = c;
            }
            // 1번으로 돌아간다.
        }
    }

    return cnt;
}

int main() {
    scanf("%d %d", &R, &C);
    int r0, c0, d; scanf("%d %d %d", &r0, &c0, &d);

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            scanf("%d", &isWall[r][c]);
        }
    }

    printf("%d\n", solve(r0, c0, d));

    return 0;
}