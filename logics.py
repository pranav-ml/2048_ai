import random
from constants import win_score
def add_new_tile(grid):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while grid[r][c]!=0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    grid[r][c]=random.choice([2,2,2,2,2,2,2,2,2,4])
    return grid
def add_new_2(grid):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while grid[r][c]!=0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    grid[r][c]=2
    return grid
def check_state(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==win_score:
                return "w"
    if grid[3][3]==0:
        return "r"
    for i in range(3):
        for j in range(3):
            if grid[i][j]==0:
                return "r"
            if grid[i+1][j]==grid[i][j] or grid[i][j+1]==grid[i][j]:
                return "r"
    for i in range(3):
        if grid[3][i]==0 or grid[i][3]==0:
            return "r"
        if grid[3][i]==grid[3][i+1] or grid[i][3]==grid[i+1][3]:
            return "r"
    return "l"


def up(grid, i, j):
    changed = False
    score=0
    while j > 0 and (grid[j - 1][i] == 0 or grid[j-1][i]==grid[j][i]):
        if grid[j - 1][i] == grid[j][i]:
            grid[j - 1][i] = (2*grid[j - 1][i])+1
            score+=grid[j][i]*2
            grid[j][i] = 0
            changed = True
            continue
        changed = True
        grid[j - 1][i] = grid[j][i]
        grid[j][i] = 0
        j -= 1
    return changed,score
def down(grid, i, j):
    changed = False
    score = 0
    while j < 3 and (grid[j + 1][i] == 0 or grid[j + 1][i] == grid[j][i]):
        if grid[j + 1][i] == grid[j][i]:
            grid[j + 1][i] = (2 * grid[j + 1][i]) + 1
            score += grid[j][i]*2
            grid[j][i] = 0
            changed = True
            continue
        changed = True
        grid[j + 1][i] = grid[j][i]
        grid[j][i] = 0
        j += 1
    return changed,score
def right(grid, i, j):
    changed = False
    score = 0
    while i < 3 and (grid[j][i+1] == 0 or grid[j][i+1] == grid[j][i]):
        if grid[j][i + 1] == grid[j][i]:
            grid[j][i + 1] = (2 * grid[j][i + 1]) + 1
            score += grid[j][i]*2
            grid[j][i] = 0
            changed = True
            continue
        changed = True
        grid[j][i + 1] = grid[j][i]
        grid[j][i] = 0
        i += 1
    return changed,score
def left(grid,i,j):
    changed=False
    score = 0
    while i > 0 and (grid[j][i - 1] == 0 or grid[j][i - 1] == grid[j][i]):
        if grid[j][i - 1] == grid[j][i]:
            grid[j][i - 1] = (2 * grid[j][i - 1]) + 1
            score += grid[j][i]*2
            grid[j][i] = 0
            changed = True
            continue
        changed=True
        grid[j][i - 1] = grid[j][i]
        grid[j][i] = 0
        i -= 1
    return changed,score


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    return mat


def move_up(grid):
    score=0
    changed=False
    for i in range(4):
        for j in range(1, 4):
            if grid[j][i] == 0:
                continue
            chang,sc=up(grid, i, j)
            changed=changed or chang
            score+=sc
        for j in range(0,4):
            if grid[j][i]%2!=0:
                grid[j][i]-=1
    return grid,changed,score


def move_down(grid):
    score = 0
    changed = False
    for i in range(4):
        for j in range(2, -1,-1):
            if grid[j][i] == 0:
                continue
            chang, sc = down(grid, i, j)
            changed = changed or chang
            score += sc
        for j in range(0,4):
            if grid[j][i]%2!=0:
                grid[j][i]-=1
    return grid,changed,score

def move_right(grid):
    score = 0
    changed = False
    for j in range(4):
        for i in range(2, -1, -1):
            if grid[j][i] == 0:
                continue
            chang, sc = right(grid, i, j)
            changed = changed or chang
            score += sc
        for i in range(0,4):
            if grid[j][i]%2!=0:
                grid[j][i]-=1

    return grid,changed,score


def move_left(grid):
    score = 0
    changed = False
    for j in range(4):
        for i in range(1, 4):
            if grid[j][i] == 0:
                continue
            chang, sc = left(grid, i, j)
            changed = changed or chang
            score += sc
        for i in range(0, 4):
            if grid[j][i] % 2 != 0:
                grid[j][i] -= 1
    return grid,changed,score

def random_move(board):
    possible_moves=[move_up,move_right,move_left,move_down]
    played=False
    while not played and len(possible_moves)>0:
        moveind=random.randrange(0,len(possible_moves))
        board,played,score=possible_moves[moveind](board)
        if played:
            return board,played,score
        possible_moves.pop(moveind)
    return board,False,score

