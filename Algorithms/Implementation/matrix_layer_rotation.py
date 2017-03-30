############################################
#                                          #
#   HackerRank Implementation Challenges   #
#                                          #
#         Matrix Layer Rotation            # 
#                                          # 
############################################

class Rotating_matrix:
    def __init__(self, row, col, a):
        self.row = row
        self.col = col
        self.a = a
    def matrix_instance(self, number):
        row_num = self.row - 1 - number
        col_num = self.col - 1 - number
        for h in range(number, col_num): yield number, h
        for v in range(number, row_num): yield v, col_num
        for h in range(col_num, number, -1): yield row_num, h
        for v in range(row_num, number, -1): yield v, number
    def rotate_instance(self, number, moves):
        data_instance = [data.a[v][h] for v, h in self.matrix_instance(number)]
        incision = moves % len(data_instance)
        data_instance = data_instance[incision:] + data_instance[:incision]
        pos = 0
        for v, h in self.matrix_instance(number):
            self.a[v][h] = data_instance[pos]
            pos += 1
    def rotate(self, moves):
        for number in range(min(self.row, self.col) // 2): self.rotate_instance(number, moves)
            
row, col, moves = [int(_) for _ in input().split()]
a = []
for i in range(row): a.append([int(_) for _ in input().split()])
data = Rotating_matrix(row, col, a)
data.rotate(moves)
for v in range(row):
    for h in range(col): print(data.a[v][h], end = ' ')
    print('')