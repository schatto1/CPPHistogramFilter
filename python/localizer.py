# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    belief_sum = 0
    for row in range(len(grid)):
        new_belief_row = []
        for column in range(len(grid[row])):
            hit = (color == grid[row][column])
            new_belief_row.append(beliefs[row][column] * (hit*p_hit + (1-hit)*p_miss))
        new_beliefs.append(new_belief_row)
        belief_sum += sum(new_belief_row)
    for row2 in range(len(new_beliefs)):
        for column2 in range(len(new_beliefs[row2])):
            new_beliefs[row2][column2] /= belief_sum
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)