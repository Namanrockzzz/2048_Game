import random
def start_game():
    mat = [[0 for i in range(4)] for j in range(4)]
    return mat

def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c]!=0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

def reverse(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][3-j] = mat[i][j]
    return new_mat
    
def transpose(mat):
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[j][i] = mat[i][j]
    return new_mat
    
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = 2*mat[i][j]
                mat[i][j+1] = 0
                changed = True
    return mat,changed
    
def compress(mat):
    changed = False
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        k=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][k] = mat[i][j]
                if k != j:
                    changed = True
                k+=1
    return new_mat,changed

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

def move_right(grid):
    reversed_grid = reverse(grid)
    # Move left and then reverse again
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed
            
    
def get_current_state(mat):
    # Is there any 2048 present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "WON"
            
    # Is there a zero present anywhere
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"
    # Is there any number same to its adjacent number in between
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]:
                return "GAME NOT OVER"
    # Is there any number same to its adjacent number in last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "GAME NOT OVER"
    # Is there any number same to its adjacent number in last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
        
        
    return "LOST"