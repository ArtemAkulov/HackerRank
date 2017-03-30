############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#               Cavity Map                 # 
#                                          # 
############################################

grid = [list(str(input())) for _ in range(int(input()))]
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if False not in map(lambda x, y: grid[i][j] > grid[x][y], (i - 1, i + 1, i, i), (j, j, j - 1, j + 1)):
            grid[i][j] = 'X'
for row in grid: print(''.join(row))