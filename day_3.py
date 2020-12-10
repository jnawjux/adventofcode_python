import numpy as np

grid = np.zeros((10, 10))
a = ['R8', 'U5', 'L5', 'D3']
b = ['U7', 'R6', 'D4', 'L4']

movements = {'L': 'start, move:', 'R': 'start, :move',
             'U': 'move:, start', 'D': ':move, start'}

for i, coord in enumerate(a):
    start = 9
    if i = 0:
    start = 9
    direction = coord[0]
    moves = int(coord[1:])
    if direction == 'R':
        grid[start, :moves] = 1
print(grid)
