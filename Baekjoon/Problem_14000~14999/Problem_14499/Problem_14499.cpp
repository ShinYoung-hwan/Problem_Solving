#include <cstdio>
#include <deque>

using namespace std;

enum { EAST=1, WEST, NORTH, SOUTH };

const int MAXRC = 20;
int R, C;
int board[MAXRC][MAXRC];
deque<int> dice[4] = { { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } };

int dr[5] = { 0, 0, 0, -1, 1 };
int dc[5] = { 0, 1, -1, 0, 0 };

bool isIn(const int r, const int c) { return (0 <= r && r < R) && (0 <= c && c < C); }

void move_east() {
    dice[1].push_front(dice[3][1]);
    dice[3][1] = dice[1].back();
    dice[1].pop_back();
}

void move_west() {
    dice[1].push_back(dice[3][1]);
    dice[3][1] = dice[1].front();
    dice[1].pop_front();
}

void move_north() {
    int tmp = dice[0][1];
    dice[0][1] = dice[1][1];
    dice[1][1] = dice[2][1];
    dice[2][1] = dice[3][1];
    dice[3][1] = tmp;
}

void move_south() {
    int tmp = dice[3][1];
    dice[3][1] = dice[2][1];
    dice[2][1] = dice[1][1];
    dice[1][1] = dice[0][1];
    dice[0][1] = tmp;
}

void copy_dice_board(const int r, const int c) {
    // 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0
    if (board[r][c]) {
        dice[3][1] = board[r][c];
        board[r][c] = 0;
    }
    // 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
    else {
        board[r][c] = dice[3][1];
    }
}

int main() {
    int r0, c0, K; scanf("%d %d %d %d %d", &R, &C, &r0, &c0, &K);
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            scanf("%d", &board[r][c]);
        }
    }

    for (int i = 0; i < K; i++) {
        int cmd; scanf("%d", &cmd);
        int r = r0 + dr[cmd], c = c0 + dc[cmd];
        if (!isIn(r, c)) continue;

        switch(cmd) {
            case EAST:
                move_east();
                break;
            case WEST:
                move_west();
                break;
            case NORTH:
                move_north();
                break;
            case SOUTH:
                move_south();
                break;
        }
        copy_dice_board(r, c);
        r0 = r, c0 = c;

        printf("%d\n", dice[1][1]);
    }
    
    return 0;
}